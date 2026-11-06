from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import textwrap

ROOT = Path(r"C:\salunic-app")
OUT = ROOT / "docs" / "capturas" / "codigo"
OUT.mkdir(parents=True, exist_ok=True)

FONT_PATH = r"C:\Windows\Fonts\consola.ttf"
FONT_BOLD = r"C:\Windows\Fonts\consolab.ttf"

def load_font(path, size):
    try:
        return ImageFont.truetype(path, size)
    except Exception:
        return ImageFont.load_default()

FONT = load_font(FONT_PATH, 15)
FONT_SM = load_font(FONT_PATH, 13)
FONT_TITLE = load_font(FONT_BOLD, 16)

BG = (30, 30, 30)
BG_HEADER = (45, 45, 48)
FG = (212, 212, 212)
FG_LN = (110, 110, 110)
FG_TITLE = (86, 156, 214)
ACCENT = (78, 201, 176)

def read_lines(path, start=1, end=None):
    text = Path(path).read_text(encoding="utf-8-sig", errors="replace")
    lines = text.splitlines()
    s = max(1, start) - 1
    e = end if end is not None else len(lines)
    return lines[s:e], start

def render_code(title, subtitle, source_path, start, end, out_name, max_width_chars=110):
    lines, ln_start = read_lines(source_path, start, end)
    # wrap long lines
    rendered = []
    for i, line in enumerate(lines):
        ln = ln_start + i
        line = line.replace("\t", "    ")
        if len(line) <= max_width_chars:
            rendered.append((ln, line, True))
        else:
            chunks = textwrap.wrap(line, width=max_width_chars, replace_whitespace=False, drop_whitespace=False) or [""]
            for j, ch in enumerate(chunks):
                rendered.append((ln if j == 0 else None, ch, j == 0))

    # measure
    dummy = Image.new("RGB", (10, 10))
    d = ImageDraw.Draw(dummy)
    def tw(fs, s):
        b = d.textbbox((0,0), s, font=fs)
        return b[2]-b[0], b[3]-b[1]
    ch_w, ch_h = tw(FONT, "M")
    line_h = ch_h + 6
    gutter_w = 54
    pad_x = 18
    pad_y = 14
    header_h = 56
    max_text_w = max([tw(FONT, txt)[0] for _, txt, _ in rendered] + [400])
    img_w = gutter_w + pad_x + max_text_w + pad_x
    img_h = header_h + pad_y + len(rendered) * line_h + pad_y
    img_w = min(max(img_w, 900), 1600)
    img = Image.new("RGB", (img_w, img_h), BG)
    draw = ImageDraw.Draw(img)

    # header
    draw.rectangle([0, 0, img_w, header_h], fill=BG_HEADER)
    draw.text((pad_x, 8), title, font=FONT_TITLE, fill=FG_TITLE)
    sub = f"{subtitle}  |  {Path(source_path).as_posix().replace('C:/salunic-app/','')}  (líneas {start}-{end})"
    draw.text((pad_x, 32), sub, font=FONT_SM, fill=ACCENT)

    y = header_h + pad_y
    for ln, txt, is_first in rendered:
        if y + line_h > img_h - 4:
            break
        if ln is not None:
            lns = str(ln).rjust(4)
            draw.text((8, y), lns, font=FONT, fill=FG_LN)
        draw.text((gutter_w + pad_x, y), txt, font=FONT, fill=FG)
        y += line_h

    out = OUT / out_name
    img.save(out)
    print("OK", out)
    return out

# 1. Entidades / DataClass (4)
ent_txt = []
for fn in ["usuario.py","cita_medica.py","medicamento.py","almacen_medicamento.py"]:
    ent_txt.append(f"# Entidades/{fn}")
    ent_txt.append((ROOT/"Entidades"/fn).read_text(encoding="utf-8-sig", errors="replace").strip())
    ent_txt.append("")
# render combined from temp
tmp = OUT/"_tmp_ent.txt"; tmp.write_text("\n".join(ent_txt), encoding="utf-8")
render_code("1) Módulos y DataClass", "Entidades (4 modelos con @dataclass)", tmp, 1, 999, "01_codigo_entidades_dataclass.png", 100)
tmp.unlink(missing_ok=True)

# 2. Datos + JSON
render_code("2) Datos y Persistencia JSON", "Listas, asdict() y cargar/guardar (manejo de excepciones)", ROOT/"Datos/datos.py", 1, 78, "02_codigo_datos_json.png")

# 3. Validación y manejo de excepciones
render_code("3) Validación y Manejo de Excepciones", "Validadores (ValueError) y pedir_campo() con try/except", ROOT/"Funciones/validaciones.py", 1, 82, "03_codigo_validaciones_excepciones.png")

# 4. CRUD (ejemplo Usuario)
render_code("4) Operaciones CRUD (ej. Usuario)", "Crear, buscar, listar, actualizar, eliminar (Funciones/usuario.py)", ROOT/"Funciones/usuario.py", 1, 70, "04_codigo_crud_usuario.png")

# 5. Búsqueda lineal
render_code("5) Algoritmo de Búsqueda Lineal", "Recorrido secuencial elemento por elemento", ROOT/"Funciones/busqueda_lineal.py", 1, 60, "05_codigo_busqueda_lineal.png")

# 6. Cola con prioridad / heapq
render_code("6) Cola con Prioridad (heapq)", "Adulto mayor prioridad 0, normal 1, turno_global (ordenamiento)", ROOT/"Funciones/cola_atencion.py", 1, 56, "06_codigo_cola_prioridad_heapq.png")

# 7. Interfaz Tkinter (app)
render_code("7) Interfaz Tkinter - App principal", "Carga de datos (Funciones.sistema) y navegación de pantallas", ROOT/"app/main.py", 1, 58, "07_codigo_tkinter_app.png")

# 8. Consola integrada
render_code("8) Módulo Consola integrado", "Usa Entidades, Datos y Funciones (menú, cola con prioridad, JSON)", ROOT/"consola/main.py", 1, 52, "08_codigo_consola_integrada.png")

print("DONE", OUT)
