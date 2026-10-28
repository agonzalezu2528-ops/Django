"""Mixin de acceso: login obligatorio + permiso por rol."""
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.views import redirect_to_login
from django.core.exceptions import PermissionDenied


class LoginPermisoRequeridoMixin(LoginRequiredMixin, PermissionRequiredMixin):
    """Sin sesión → redirige al login. Con sesión sin permiso → 403."""

    raise_exception = True

    def handle_no_permission(self):
        if not self.request.user.is_authenticated:
            return redirect_to_login(
                self.request.get_full_path(),
                self.get_login_url(),
                self.get_redirect_field_name(),
            )
        raise PermissionDenied