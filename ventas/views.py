# ventas/views.py
"""Vistas de la app ventas — W07.

Lectura: VentaListView y VentaDetailView.
Escritura (crear_venta): W08.
PDF de factura (venta_pdf): W12 — WeasyPrint.
"""
import mimetypes
from decimal import ROUND_HALF_UP, Decimal
from pathlib import Path
from urllib.parse import unquote, urlparse

from django.conf import settings
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.staticfiles import finders
from core.mixins import LoginPermisoRequeridoMixin
from django.http import HttpResponse
from django.http.request import validate_host
from django.shortcuts import get_object_or_404, redirect, render
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import DeleteView, DetailView, ListView
from configuracion.models import ConfiguracionERP
from .forms  import DetalleVentaForm, VentaForm
from .models import DetalleVenta, Venta


class VentaListView(ListView):
    """Lista paginada de ventas en orden cronológico inverso."""

    model               = Venta
    template_name       = 'ventas/lista.html'
    context_object_name = 'ventas'
    paginate_by         = 20

    def get_queryset(self):
        """Pre-carga cliente para evitar N+1 en la tabla de ventas."""
        return (
            Venta.objects
            .select_related('cliente')
            .order_by('-fecha')
        )


class VentaDetailView(DetailView):
    """Detalle de una venta con todas sus líneas de producto."""

    model               = Venta
    template_name       = 'ventas/detalle.html'
    context_object_name = 'venta'
    pk_url_kwarg        = 'venta_id'

    def get_queryset(self):
        """Pre-carga cliente y prefetch líneas de detalle."""
        return (
            Venta.objects
            .select_related('cliente')
            .prefetch_related('detalles__producto')
        )

@login_required
@permission_required('ventas.add_venta', raise_exception=True)
def crear_venta(request):
    """Crea un encabezado de venta con una línea de detalle.

    GET  → muestra los dos formularios vacíos.
    POST → valida ambos, guarda si correctos, muestra errores si no.

    Protección: redirige a login si no autenticado.
    Nota: para múltiples líneas usar formsets (implementar en Espiral 5).
    """


    venta_form   = VentaForm(request.POST or None)
    detalle_form = DetalleVentaForm(request.POST or None)

    if request.method == 'POST':
        if venta_form.is_valid() and detalle_form.is_valid():
            venta          = venta_form.save()
            detalle        = detalle_form.save(commit=False)
            detalle.venta  = venta
            # precio_unitario se auto-captura en save() si es None
            detalle.save()
            messages.success(
                request,
                f'Venta #{venta.pk} registrada. '
                f'Total: ${venta.total:.2f}'
            )
            return redirect('ventas:detalle', venta_id=venta.pk)

    return render(request, 'ventas/crear.html', {
        'venta_form':   venta_form,
        'detalle_form': detalle_form,
    })


class VentaDeleteView(LoginPermisoRequeridoMixin, DeleteView):
    model               = Venta
    template_name       = 'ventas/eliminar.html'
    pk_url_kwarg        = 'venta_id'
    success_url         = reverse_lazy('ventas:lista')
    permission_required = 'ventas.delete_venta'

    def form_valid(self, form):
        pk       = self.object.pk
        response = super().form_valid(form)
        messages.success(self.request, f'Venta #{pk} eliminada.')
        return response


# ── W12: PDF de factura con WeasyPrint ────────────────────────────────

def _ruta_local(url_path: str) -> Path | None:
    """Traduce /static/... o /media/... a un archivo en disco (o None)."""
    static_prefix = "/" + settings.STATIC_URL.lstrip("/")
    media_prefix = "/" + settings.MEDIA_URL.lstrip("/")

    if url_path.startswith(static_prefix):
        relativa = url_path[len(static_prefix):]
        candidata = Path(settings.STATIC_ROOT) / relativa
        if candidata.is_file():
            return candidata
        encontrada = finders.find(relativa)  # útil en desarrollo, sin collectstatic
        return Path(encontrada) if encontrada else None

    if url_path.startswith(media_prefix):
        raiz = Path(settings.MEDIA_ROOT).resolve()
        candidata = (raiz / url_path[len(media_prefix):]).resolve()
        # Evita salir de MEDIA_ROOT con rutas tipo ../
        if raiz in candidata.parents and candidata.is_file():
            return candidata
    return None


def _url_fetcher_local(url: str, timeout: int = 10, ssl_context=None):
    """url_fetcher de WeasyPrint que lee /static/ y /media/ desde disco.

    Evita que WeasyPrint haga peticiones HTTP al propio servidor (lento y
    puede bloquear a los workers de Gunicorn). Si el archivo no existe
    (p. ej. un logo perdido por el disco efímero de Render), se lanza
    FileNotFoundError: WeasyPrint solo registra un aviso y omite la imagen.
    Las URLs externas (p. ej. media en S3) usan el fetcher por defecto.
    """
    import weasyprint  # import perezoso: solo se necesita al generar el PDF
    parsed = urlparse(url)
    if parsed.scheme in ("http", "https", "file"):
        ruta = _ruta_local(unquote(parsed.path))
        if ruta is not None:
            return {
                "string": ruta.read_bytes(),
                "mime_type": mimetypes.guess_type(ruta.name)[0],
                "filename": ruta.name,
            }
        propio = validate_host(
            parsed.hostname or "", ["localhost", "127.0.0.1", *settings.ALLOWED_HOSTS]
        )
        if parsed.scheme == "file" or propio:
            raise FileNotFoundError(url)
    return weasyprint.default_url_fetcher(url, timeout=timeout, ssl_context=ssl_context)


def calcular_totales(subtotal, iva_porcentaje) -> dict:
    """Subtotal, IVA y total con 2 decimales (redondeo comercial).

    Venta.total es la suma de las líneas SIN IVA; el IVA se suma aparte.
    Ejemplo: calcular_totales(Decimal("3000"), Decimal("16"))
             -> subtotal 3000.00, iva 480.00, total 3480.00
    """
    centavos = Decimal("0.01")
    subtotal = Decimal(subtotal).quantize(centavos, ROUND_HALF_UP)
    iva = (subtotal * Decimal(iva_porcentaje) / 100).quantize(centavos, ROUND_HALF_UP)
    return {"subtotal": subtotal, "iva": iva, "total_con_iva": subtotal + iva}


@login_required
def venta_pdf(request, venta_id: int) -> HttpResponse:
    """Genera y descarga la factura de una venta en formato PDF.

    Motor: WeasyPrint (requiere entorno Linux o contenedor Docker).

    Args:
        request: HttpRequest de Django.
        venta_id: ID de la venta a generar.

    Returns:
        HttpResponse con Content-Type application/pdf y descarga directa.
    """

    venta = get_object_or_404(
        Venta.objects.select_related("cliente").prefetch_related(
            "detalles__producto__categoria"
        ),
        pk=venta_id,
    )
    config = ConfiguracionERP.get_instance()
    context = {
        "venta": venta,
        "config": config,
        "hoy": timezone.localdate(),  # fecha en TIME_ZONE (America/Mexico_City)
        **calcular_totales(venta.total, config.iva_porcentaje),
    }

    html_string = render_to_string("ventas/factura_pdf.html", context, request=request)

    # ── WeasyPrint: conversión HTML → PDF ─────────────────────────────
    # base_url resuelve rutas relativas como /media/... o /static/...
    # y _url_fetcher_local las lee del disco en vez de pedirlas por HTTP.
    import weasyprint  # import perezoso
    pdf_bytes = weasyprint.HTML(
        string=html_string,
        base_url=request.build_absolute_uri("/"),
        url_fetcher=_url_fetcher_local,
    ).write_pdf()

    response = HttpResponse(pdf_bytes, content_type="application/pdf")
    response["Content-Disposition"] = (
        f'attachment; filename="factura_{venta.pk:05d}.pdf"'
    )
    return response
