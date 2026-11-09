import weasyprint

# Generar un PDF de prueba (paso 11.2 de la guía)
html = '''
<html>
<head>
<style>
@page { size: A4; margin: 2cm; }
body { font-family: Arial; }
h1 { color: #0A2342; border-bottom: 3px solid #B8860B; padding-bottom: .5rem; }
p.num::after { content: counter(page) ' de ' counter(pages); }
</style>
</head>
<body>
<h1>ERP Django — UTEC Celaya</h1>
<p>Prueba de generación PDF con WeasyPrint 60.x</p>
<p>Página: <span class=num></span></p>
</body>
</html>
'''
pdf = weasyprint.HTML(string=html).write_pdf()
with open('/tmp/prueba_weasyprint.pdf', 'wb') as f:
    f.write(pdf)
print('PDF guardado en /tmp/prueba_weasyprint.pdf')
print('Tamaño:', len(pdf), 'bytes')
