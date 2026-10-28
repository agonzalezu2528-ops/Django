import pathlib

SKIP = {'env_erp', '.git', 'staticfiles', 'node_modules', '__pycache__'}

def fix_line(s):
    for _ in range(2):  # por si está dañado dos veces
        out = bytearray()
        for ch in s:
            try:
                out += ch.encode('cp1252')
            except UnicodeEncodeError:
                if ord(ch) < 256:
                    out.append(ord(ch))
                else:
                    return s
        try:
            nuevo = out.decode('utf-8')
        except UnicodeDecodeError:
            return s
        if nuevo == s:
            break
        s = nuevo
    return s

for p in pathlib.Path('.').rglob('*'):
    if p.is_file() and p.suffix in {'.html', '.py', '.md', '.css', '.js'} \
            and not (SKIP & set(p.parts)):
        try:
            lineas = p.read_bytes().decode('utf-8').splitlines(keepends=True)
        except UnicodeDecodeError:
            print('SALTADO (no es UTF-8):', p)
            continue
        nuevas = [fix_line(l) for l in lineas]
        if nuevas != lineas:
            p.write_bytes(''.join(nuevas).encode('utf-8'))
            print('Reparado:', p)