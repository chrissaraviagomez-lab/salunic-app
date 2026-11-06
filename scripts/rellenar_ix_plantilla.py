from pathlib import Path
from docx import Document
from docx.shared import Pt, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
import shutil

TPL = Path(r"D:\Defensa\Plantilla Informe Final Integrador II.docx")
OUT = Path(r"D:\Defensa\Plantilla Informe Final Integrador II - SALUNIC IX.docx")
OUT_PROJ = Path(r"C:\salunic-app\docs\pdfs\Plantilla Informe Final Integrador II - SALUNIC IX.docx")
CAPTURAS = Path(r"C:\salunic-app\docs\capturas")
CODIGO = CAPTURAS / "codigo"
REPO = "https://github.com/chrissaraviagomez-lab/salunic-app"

doc = Document(str(TPL))

# Find IX indication and next heading (Conclusiones)
ix_idx = None
end_idx = None
for i, p in enumerate(doc.paragraphs):
    t = p.text.strip()
    tl = t.lower()
    if ix_idx is None and 'indicaci' in tl and ('modulos implementados' in tl or 'módulos implementados' in tl):
        ix_idx = i
    if ix_idx is not None and i > ix_idx and (p.style.name or '').lower().startswith('heading'):
        end_idx = i
        break
if ix_idx is None or end_idx is None:
    raise SystemExit(f'No se encontro seccion IX: ix={ix_idx} end={end_idx}')

# remove any existing content between indication and next heading (keep template clean)
body = doc.element.body
to_remove = []
for i in range(ix_idx + 1, end_idx):
    to_remove.append(doc.paragraphs[i]._element)
for el in to_remove:
    try:
        body.remove(el)
    except Exception:
        pass

last = doc.paragraphs[ix_idx]._element

def _insert_after(el):
    global last
    last.addnext(el)
    last = el
    return el

def insert_para(text, bold=False, size=11, italic=False):
    p = OxmlElement('w:p')
    r = OxmlElement('w:r')
    rPr = OxmlElement('w:rPr')
    if bold:
        rPr.append(OxmlElement('w:b'))
    if italic:
        rPr.append(OxmlElement('w:i'))
    sz = OxmlElement('w:sz'); sz.set(qn('w:val'), str(int(size * 2))); rPr.append(sz)
    szCs = OxmlElement('w:szCs'); szCs.set(qn('w:val'), str(int(size * 2))); rPr.append(szCs)
    r.append(rPr)
    t = OxmlElement('w:t'); t.set(qn('xml:space'), 'preserve'); t.text = str(text)
    r.append(t)
    p.append(r)
    _insert_after(p)
    return p

def insert_bullet(text):
    insert_para('• ' + str(text), size=10.5)

def insert_picture(path, width_inches=2.8, caption=''):
    path = Path(path)
    if not path.exists():
        insert_para(f'[Falta captura: {path.name}]', italic=True, size=10)
        if caption:
            insert_para(caption, italic=True, size=9)
        return
    # create at end, then move
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run()
    try:
        run.add_picture(str(path), width=Inches(width_inches))
    except Exception:
        run.add_text(f'[No se pudo insertar imagen: {path.name}]')
    _insert_after(p._element)
    if caption:
        c = doc.add_paragraph(caption)
        c.alignment = WD_ALIGN_PARAGRAPH.CENTER
        if c.runs:
            c.runs[0].font.size = Pt(9)
            c.runs[0].italic = True
            c.runs[0].font.color.rgb = RGBColor(70, 70, 70)
        _insert_after(c._element)

# Contenido RESUMIDO para sección IX (incluye capturas de código Python)
insert_para('')
insert_para('1. Módulos implementados', bold=True)
insert_bullet('Entidades/ (4 DataClass, @dataclass): Usuario, CitaMedica, Medicamento, AlmacenMedicamento.')
insert_bullet('Datos/: listas en memoria (usuarios, citas, medicamentos, almacen) y persistencia JSON compartida (salunic_datos.json, raíz) con cargar/guardar (asdict y reconstrucción Clase(**dict)).')
insert_bullet('Funciones/ (una por DataClass): usuario.py, cita_medica.py, medicamento.py, almacen_medicamento.py (CRUD); utilidades: validaciones.py, busqueda_lineal.py, cola_atencion.py (heapq), sistema.py. Regla: Funciones usa solo Datos y Entidades.')
insert_bullet('app/ (Tkinter): main.py + screens/ (Login, Registro, Home, Citas, Panel de Atención, etc.). Regla: screens usa solo Funciones y Entidades.')
insert_bullet('consola/: main.py con menús (Usuarios, Citas, Medicamentos, Almacén, Cola con Prioridad, Archivo de Datos), integrado con Entidades/Datos/Funciones.')
insert_picture(CODIGO/'01_codigo_entidades_dataclass.png', width_inches=5.8, caption='Código 1. Entidades (DataClass @dataclass): 4 modelos del sistema.')
insert_picture(CODIGO/'02_codigo_datos_json.png', width_inches=5.8, caption='Código 2. Datos y persistencia JSON (listas, asdict, cargar/guardar, manejo de excepciones).')

insert_para('2. Validación de datos y manejo de excepciones', bold=True)
insert_bullet('Validaciones (ValueError): nombre, email, contraseña, fecha (DD/MM/AAAA), hora (HH:MM), celular, cantidad, dosis; pedir_campo() reintenta y muestra errores.')
insert_bullet('Excepciones: try/except en JSON ([OK]/[ERROR]/[INFO]), validación de opciones en consola y controles/messagebox + try-except en la app.')
insert_picture(CODIGO/'03_codigo_validaciones_excepciones.png', width_inches=5.8, caption='Código 3. Validaciones (ValueError) y manejo de excepciones (try/except).')

insert_para('3. Operaciones CRUD', bold=True)
insert_bullet('CRUD (crear, buscar/listar, actualizar, eliminar, contar) por entidad: Usuario, CitaMedica, Medicamento y Almacén/Stock (Funciones/*), disponible en consola y usado por la app vía Funciones/sistema.')
insert_picture(CODIGO/'04_codigo_crud_usuario.png', width_inches=5.8, caption='Código 4. Ejemplo de operaciones CRUD (Funciones/usuario.py).')

insert_para('4. Algoritmos de búsqueda y ordenamiento', bold=True)
insert_bullet('Búsqueda lineal: recorrido secuencial elemento por elemento (Funciones/busqueda_lineal.py), usada en autenticación/consultas (ej. por email).')
insert_bullet('Ordenamiento por prioridad (cola, heapq): adulto mayor = prioridad 0, normal = 1, turno_global desempata; heapq atiende primero al de mayor prioridad (adulto mayor antes aunque llegue después).')
insert_picture(CODIGO/'05_codigo_busqueda_lineal.png', width_inches=5.8, caption='Código 5. Algoritmo de búsqueda lineal (recorrido secuencial).')
insert_picture(CODIGO/'06_codigo_cola_prioridad_heapq.png', width_inches=5.8, caption='Código 6. Cola con prioridad (heapq): adulto mayor atendido primero.')

insert_para('5. Interfaz en Tkinter', bold=True)
insert_bullet('Ventana 375x812 con navegación por pantallas (SalunicApp/show_screen). Incluye login/registro, citas, encolado con prioridad y Panel de Atención (EN ATENCIÓN, COLA DE ESPERA, ATENDER SIGUIENTE).')
insert_picture(CODIGO/'07_codigo_tkinter_app.png', width_inches=5.8, caption='Código 7. Interfaz Tkinter (app/main.py): carga de datos y navegación.')
insert_picture(CODIGO/'08_codigo_consola_integrada.png', width_inches=5.8, caption='Código 8. Módulo consola integrado (Entidades/Datos/Funciones, cola con prioridad, JSON).')

insert_para('6. Capturas de pantalla (ejecución de la aplicación)', bold=True)
for img, cap, w in [
    (CAPTURAS/'01_inicio_login.png', 'Captura 1. App: inicio/login.', 2.4),
    (CAPTURAS/'04_home.png', 'Captura 2. App: Home.', 2.4),
    (CAPTURAS/'05_citas.png', 'Captura 3. App: citas.', 2.4),
    (CAPTURAS/'06_panel_atencion_prioridad.png', 'Captura 4. App: Panel de Atención (cola con prioridad).', 2.4),
    (CAPTURAS/'08_consola_menu.png', 'Captura 5. Consola: menú principal.', 5.8),
    (CAPTURAS/'09_consola_cola_prioridad.png', 'Captura 6. Consola: cola con prioridad (adulto mayor primero).', 5.8),
    (CAPTURAS/'10_consola_json.png', 'Captura 7. Consola: archivo JSON ([OK]).', 5.8),
]:
    insert_picture(img, width_inches=w, caption=cap)
insert_para('Nota: si faltan capturas 5-7 (consola), guárdalas en docs/capturas/ con esos nombres y vuelve a ejecutar el script para insertarlas automáticamente.', italic=True, size=9)

insert_para('7. Enlace al repositorio', bold=True)
insert_para(REPO)

OUT_PROJ.parent.mkdir(parents=True, exist_ok=True)
# Guardar primero en el proyecto (evita bloqueo si el Word en D:\Defensa está abierto)
doc.save(str(OUT_PROJ))
print('ok', OUT_PROJ)
try:
    shutil.copy2(OUT_PROJ, OUT)
    print('ok', OUT)
except Exception as e:
    print(f'[AVISO] No se pudo actualizar {OUT} (posiblemente abierto en Word): {e}')
    print('  -> Cierra el archivo en Word y ejecuta de nuevo, o usa la copia en docs/pdfs/.')
