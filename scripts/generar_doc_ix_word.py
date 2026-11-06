from pathlib import Path
from docx import Document
from docx.shared import Pt, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.style import WD_STYLE_TYPE
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

REPO = "https://github.com/chrissaraviagomez-lab/salunic-app"
CAPTURAS = Path(r"C:\salunic-app\docs\capturas")
CODIGO = CAPTURAS / "codigo"

doc = Document()

# base styles
style = doc.styles['Normal']
style.font.name = 'Calibri'
style._element.rPr.rFonts.set(qn('w:eastAsia'), 'Calibri')
style.font.size = Pt(11)

def add_title(text):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run(text)
    r.bold = True
    r.font.size = Pt(18)

def add_subtitle(text):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run(text)
    r.bold = True
    r.font.size = Pt(14)

def h1(text):
    p = doc.add_heading(text, level=1)

def h2(text):
    p = doc.add_heading(text, level=2)

def para(text):
    doc.add_paragraph(str(text))

def bullet(text):
    doc.add_paragraph(str(text), style='List Bullet')

def code_block(text):
    p = doc.add_paragraph()
    p.paragraph_format.left_indent = Inches(0.2)
    r = p.add_run(str(text))
    r.font.name = 'Consolas'
    r._element.rPr.rFonts.set(qn('w:eastAsia'), 'Consolas')
    r.font.size = Pt(9)

def _set_cell_border(cell, **kwargs):
    tc = cell._tc
    tcPr = tc.get_or_add_tcPr()
    tcBorders = OxmlElement('w:tcBorders')
    for edge in ('top', 'left', 'bottom', 'right'):
        edge_data = kwargs.get(edge)
        if edge_data:
            tag = OxmlElement(f'w:{edge}')
            for key, val in edge_data.items():
                tag.set(qn(f'w:{key}'), str(val))
            tcBorders.append(tag)
    tcPr.append(tcBorders)

def screenshot_placeholder(n, title, desc, image_path=None):
    """Inserta una imagen si existe; si no, deja un recuadro placeholder."""
    img = None
    if image_path:
        pth = Path(image_path)
        if pth.exists():
            img = pth
    if img:
        p = doc.add_paragraph()
        r = p.add_run(f"[CAPTURA {n}] {title}")
        r.bold = True
        r.font.size = Pt(11)
        pic_p = doc.add_paragraph()
        pic_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        run = pic_p.add_run()
        # Ajustar ancho (app es angosta; consola puede ser más ancha)
        try:
            run.add_picture(str(img), width=Inches(3.2) if "panel_atencion" in img.name or "citas" in img.name or "home" in img.name or "login" in img.name or "registro" in img.name or "inicio" in img.name else Inches(5.8))
        except Exception:
            run.add_picture(str(img), width=Inches(4.5))
        cap = doc.add_paragraph(desc)
        cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
        if cap.runs:
            cap.runs[0].font.size = Pt(9)
            cap.runs[0].italic = True
        doc.add_paragraph("")
        return
    table = doc.add_table(rows=1, cols=1)
    cell = table.rows[0].cells[0]
    _set_cell_border(cell,
        top={"sz": "12", "val": "single", "color": "666666"},
        bottom={"sz": "12", "val": "single", "color": "666666"},
        left={"sz": "12", "val": "single", "color": "666666"},
        right={"sz": "12", "val": "single", "color": "666666"},
    )
    p = cell.paragraphs[0]
    r = p.add_run(f"[CAPTURA {n}] {title}\n")
    r.bold = True
    r.font.size = Pt(11)
    r2 = p.add_run(f"Insertar aquí la captura: {desc}")
    r2.font.size = Pt(10)
    r2.font.color.rgb = RGBColor(80, 80, 80)
    doc.add_paragraph("")  # spacing


def code_shot(label, image_path, caption):
    img = Path(image_path)
    if not img.exists():
        para(f"[Falta captura de c?digo: {img.name}]")
        return
    p = doc.add_paragraph()
    r = p.add_run(label)
    r.bold = True
    r.font.size = Pt(10)
    pic_p = doc.add_paragraph()
    pic_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    try:
        pic_p.add_run().add_picture(str(img), width=Inches(6.2))
    except Exception:
        pic_p.add_run().add_picture(str(img), width=Inches(5.5))
    cap = doc.add_paragraph(caption)
    cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
    if cap.runs:
        cap.runs[0].font.size = Pt(9)
        cap.runs[0].italic = True
        cap.runs[0].font.color.rgb = RGBColor(70, 70, 70)
    doc.add_paragraph("")

# Portada
add_title('SALUNIC - Sistema de Salud y Bienestar')
add_subtitle('IX. Desarrollo del prototipo en Python')
doc.add_paragraph('')
p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = p.add_run('Proyecto: SALUNIC (App Tkinter + Módulo Consola integrados)\n')
r.add_break(); p.add_run('Lenguaje: Python 3  |  Interfaz gráfica: Tkinter\n')
p.add_run(f'Repositorio: {REPO}')
doc.add_paragraph('')
para('Documento de entrega que describe los módulos implementados, la validación de datos y el manejo de excepciones, las operaciones CRUD, los algoritmos de búsqueda y ordenamiento, y la interfaz en Tkinter, con espacios para capturas de pantalla y el enlace al repositorio.')
doc.add_page_break()

# 1
h1('1. Módulos implementados')
para('El prototipo se organizó con una arquitectura modular para separar modelos, datos, lógica e interfaces, cumpliendo la estructura requerida (Entidades, Datos, Funciones) e integrando el módulo por consola y la aplicación gráfica.')
h2('1.1 Entidades/ (modelos - DataClass)')
para('Contiene las 4 clases de datos del sistema, implementadas con @dataclass:')
bullet('usuario.py -> Usuario (id, nombre, email, password, telefono)')
bullet('cita_medica.py -> CitaMedica (id, paciente_id, medico_id, especialidad, fecha, hora, lugar)')
bullet('medicamento.py -> Medicamento (id, nombre, dosis, frecuencia, presentacion)')
bullet('almacen_medicamento.py -> AlmacenMedicamento (id, medicamento_id, cantidad, fecha_vencimiento)')
bullet('__init__.py -> exporta las entidades.')
h2('1.2 Datos/ (almacenamiento en memoria y persistencia)')
bullet('datos.py: listas globales (usuarios, citas, medicamentos, almacen), datos iniciales, cargar_datos_iniciales(), guardar_datos(), cargar_datos().')
bullet('Persistencia en salunic_datos.json (raíz del proyecto), compartido entre app y consola.')
bullet('Serialización con dataclasses.asdict() y reconstrucción con Clase(**dict).')
h2('1.3 Funciones/ (lógica de negocio)')
para('Regla aplicada: Funciones solo usa Datos y Entidades.')
bullet('Por cada DataClass: usuario.py, cita_medica.py, medicamento.py, almacen_medicamento.py (CRUD/consultas).')
bullet('validaciones.py: validación de entradas (ValueError).')
bullet('busqueda_lineal.py: algoritmos de búsqueda lineal.')
bullet('cola_atencion.py: cola con prioridad usando heapq.')
bullet('sistema.py: servicios de alto nivel para la app (autenticación, registro, citas, cola) sin exponer Datos a la UI.')
h2('1.4 app/ (interfaz gráfica Tkinter)')
para('Regla aplicada: screens/ solo usa Funciones y Entidades.')
bullet('app/main.py: inicializa la app, precarga datos (Funciones.sistema.iniciar_sistema) y gestiona navegación (show_screen/frames).')
bullet('app/screens/: Login, Registro, Home, Citas, Panel de Atención (atencion_screen.py), Historial, Medicamentos, Estadísticas, formularios.')
bullet('app/data/users_data.py: adaptador de compatibilidad sobre la estructura unificada.')
bullet('app/screens/styles.py: estilos/colores/utilidades visuales.')
h2('1.5 consola/ (módulo por consola)')
bullet('consola/main.py: menús (Usuarios, Citas, Medicamentos, Almacén/Inventario, Cola de Atención con Prioridad, Archivo de Datos). Usa Entidades, Datos y Funciones; comparte salunic_datos.json.')
h2('1.6 Otros módulos de apoyo')
bullet('core/: compatibilidad que delega a Entidades/Datos/Funciones (estado unificado).')
bullet('docs/pdfs/ y scripts/: documentación/guías y scripts auxiliares (generación de PDFs).')
bullet('salunic_datos.json: archivo de persistencia compartido (raíz).')
h2('1.7 Evidencia de c?digo (m?dulos)')
code_shot('C?digo 1 - Entidades (DataClass)', CODIGO/'01_codigo_entidades_dataclass.png', 'Modelos @dataclass: Usuario, CitaMedica, Medicamento, AlmacenMedicamento.')
code_shot('C?digo 2 - Datos y persistencia JSON', CODIGO/'02_codigo_datos_json.png', 'Listas, asdict(), cargar/guardar JSON y manejo de excepciones.')

# 2
h1('2. Validación de datos y manejo de excepciones')
h2('2.1 Validación de datos (Funciones/validaciones.py)')
para('Funciones implementadas (lanzan ValueError cuando el dato no cumple):')
bullet('validar_nombre: no vacío; solo letras/espacios (incluye acentos); normaliza.')
bullet('validar_email: formato válido (expresión regular).')
bullet('validar_password: mínimo 4 caracteres.')
bullet('validar_fecha: formato DD/MM/AAAA con fecha real (datetime.strptime).')
bullet('validar_hora: formato HH:MM válido (datetime.strptime).')
bullet('validar_dosis: no vacía.')
bullet('validar_celular: formato/longitud controlada.')
bullet('validar_cantidad: entero positivo.')
bullet('validar_descripcion: no vacía; normaliza.')
bullet('pedir_campo(etiqueta, validador): reintenta hasta valor válido, capturando ValueError.')
h2('2.2 Manejo de excepciones')
bullet('Consola: validación de opciones numéricas; pedir_campo captura ValueError y muestra [Error].')
bullet('Persistencia JSON (Datos/datos.py): try/except al guardar/cargar (archivo, formato/decodificación), mensajes [OK]/[ERROR]/[INFO].')
bullet('App Tkinter: validaciones en formularios (campos vacíos, correo, contraseña) con messagebox.showerror; try/except en carga inicial y acciones (citas/cola) para evitar cierres inesperados.')
bullet('Reglas de negocio: prevención de duplicados (usuario por email) y retornos seguros (None/False).')
code_block('''# Ejemplo: validación + manejo de excepción
def pedir_campo(etiqueta, validador):
    while True:
        try:
            valor = input(etiqueta)
            return validador(valor)      # puede lanzar ValueError
        except ValueError as e:
            print(f"  [Error] {e}")      # reintento controlado''')
h2('2.3 Evidencia de c?digo (validaci?n/excepciones)')
code_shot('C?digo 3 - Validaciones y excepciones', CODIGO/'03_codigo_validaciones_excepciones.png', 'Validadores (ValueError) y pedir_campo() con try/except/reintento.')

# 3
h1('3. Operaciones CRUD')
para('Operaciones CRUD (Crear, Leer/Buscar/Listar, Actualizar, Eliminar) organizadas en un archivo de funciones por cada DataClass (Funciones/), más conteos.')
h2('3.1 Usuario (Funciones/usuario.py)')
bullet('Crear: registrar_usuario() | Leer: buscar_usuario(email), listar_usuarios() | Actualizar: actualizar_usuario(email) | Eliminar: eliminar_usuario(email) | Conteo: contar_usuarios().')
h2('3.2 Cita Médica (Funciones/cita_medica.py)')
bullet('Crear: registrar_cita() | Leer: buscar_cita(medico_id), listar_citas() | Actualizar: actualizar_cita(medico_id) | Eliminar: eliminar_cita(medico_id) | Conteo: contar_citas().')
h2('3.3 Medicamento (Funciones/medicamento.py)')
bullet('Crear: registrar_medicamento() | Leer: buscar_medicamento(nombre), listar_medicamentos() | Actualizar: actualizar_medicamento(nombre) | Eliminar: eliminar_medicamento(nombre) | Conteo: contar_medicamentos().')
h2('3.4 Almacén / Inventario (Funciones/almacen_medicamento.py)')
bullet('Crear: registrar_stock() | Leer: buscar_stock(medicamento_id), listar_stock() | Actualizar: actualizar_stock(medicamento_id) | Eliminar: eliminar_stock(medicamento_id) | Conteo: contar_stock().')
h2('3.5 Integración')
bullet('Consola: submenús invocan CRUD por entidad y permiten guardar/cargar JSON.')
bullet('App: usa Funciones.sistema/Funciones para autenticación, registro, citas y cola, respetando reglas de acceso.')
h2('3.6 Evidencia de c?digo (CRUD)')
code_shot('C?digo 4 - Ejemplo CRUD', CODIGO/'04_codigo_crud_usuario.png', 'Operaciones CRUD por entidad (ejemplo: Funciones/usuario.py).')

# 4
h1('4. Algoritmos de búsqueda y ordenamiento')
h2('4.1 Búsqueda lineal (Funciones/busqueda_lineal.py)')
para('Búsqueda secuencial: recorre la lista elemento por elemento comparando el criterio hasta encontrar coincidencia(s).')
code_block('''def busqueda_lineal(lista, criterio, atributo):
    resultados = []
    for elemento in lista:  # recorrido secuencial
        valor = getattr(elemento, atributo, None)
        if str(valor).lower() == str(criterio).lower():
            resultados.append(elemento)
    return resultados''')
bullet('busqueda_lineal_por_email: usada para localizar usuarios/autenticación (login).')
bullet('Variantes: busqueda_lineal_citas_por_medico, busqueda_lineal_medicamento_por_nombre.')
h2('4.2 Ordenamiento / atención por prioridad (heapq)')
para('Cola con PRIORIDAD (no FIFO puro) usando heapq. La selección del siguiente se basa en la clave (prioridad, turno_global, item):')
bullet('Adulto mayor: prioridad 0 (se atiende primero). Normal: prioridad 1.')
bullet('turno_global: desempate por orden de llegada dentro del mismo nivel.')
bullet('heapq.heappop() extrae el menor (prioridad, turno) -> adulto mayor primero aunque llegue después.')
code_block('''import heapq
prioridad = 0 if es_adulto_mayor else 1
heapq.heappush(self.cola, (prioridad, self.turno_global, item))
prioridad, turno, atendido = heapq.heappop(self.cola)  # atiende por prioridad''')
para('La vista de la cola se muestra ordenada con sorted por (prioridad, turno) sin alterar la extracción del heap.')
h2('4.3 Evidencia de c?digo (b?squeda y prioridad)')
code_shot('C?digo 5 - B?squeda lineal', CODIGO/'05_codigo_busqueda_lineal.png', 'Recorrido secuencial elemento por elemento.')
code_shot('C?digo 6 - Cola con prioridad (heapq)', CODIGO/'06_codigo_cola_prioridad_heapq.png', 'Adulto mayor (prioridad 0) atendido primero; desempate por turno_global.')

# 5
h1('5. Interfaz en Tkinter')
para('Interfaz gráfica desarrollada con Tkinter (app/), con navegación por pantallas (Frames) y estilo consistente (styles.py).')
h2('5.1 Estructura y navegación')
bullet('app/main.py (SalunicApp): ventana 375x812, contenedor y show_screen() para cambiar vistas.')
bullet('Pantallas: Splash/Inicio, Login, Registro, Home, Citas, Panel de Atención, Historial, Medicamentos, Estadísticas, formularios.')
bullet('Carga inicial: Funciones.sistema.iniciar_sistema().')
h2('5.2 Funcionalidades visibles')
bullet('Login: validación y autenticación (búsqueda lineal por email vía Funciones/Datos).')
bullet('Registro: crea Usuario (DataClass) y guarda en JSON.')
bullet('Citas: listar/agregar citas y encolar indicando si es adulto mayor (prioridad).')
bullet('Panel de Atención: muestra EN ATENCIÓN y COLA DE ESPERA ordenada por prioridad; ATENDER SIGUIENTE usa desencolado por prioridad (heapq).')
h2('5.3 Evidencia de c?digo (Tkinter y consola)')
code_shot('C?digo 7 - Interfaz Tkinter', CODIGO/'07_codigo_tkinter_app.png', 'app/main.py: inicializaci?n, carga (Funciones.sistema) y navegaci?n por pantallas.')
code_shot('C?digo 8 - Consola integrada', CODIGO/'08_codigo_consola_integrada.png', 'consola/main.py usa Entidades/Datos/Funciones (men?s, cola con prioridad, JSON).')
h2('5.4 Capturas de pantalla de ejecuci?n (evidencias)')
para('A continuación se incluyen las capturas disponibles. Las capturas de consola (5, 6 y 7) deben tomarse al ejecutar `py consola/main.py` (Win+Shift+S) y guardarse como docs/capturas/08_consola_menu.png, 09_consola_cola_prioridad.png y 10_consola_json.png para que se inserten automáticamente, o insertarse manualmente.')
screenshot_placeholder(1, 'Inicio / Login (App Tkinter)', 'Ventana de la app mostrando la pantalla de inicio o login (interfaz Tkinter).', CAPTURAS / '01_inicio_login.png')
screenshot_placeholder(2, 'Home (App Tkinter)', 'Pantalla Home con accesos del sistema (navegación).', CAPTURAS / '04_home.png')
screenshot_placeholder(3, 'Gestión de Citas (App)', 'Pantalla de Citas: listado y/o flujo para agregar cita y agregar a cola con prioridad.', CAPTURAS / '05_citas.png')
screenshot_placeholder(4, 'Panel de Atención - Cola con prioridad (App)', 'Panel con EN ATENCIÓN y COLA DE ESPERA; evidencia de prioridad (adulto mayor primero) y botón ATENDER SIGUIENTE.', CAPTURAS / '06_panel_atencion_prioridad.png')
screenshot_placeholder(5, 'Módulo por consola - Menú principal', 'Terminal `py consola/main.py`: menú principal con opciones (Usuarios, Citas, Medicamentos, Almacén, Cola con Prioridad, Archivo de Datos).', CAPTURAS / '08_consola_menu.png')
screenshot_placeholder(6, 'Consola - Cola con prioridad (evidencia)', 'Submenú Cola de Atención: adulto mayor (PRIORITARIO) atendido primero aunque llegó después.', CAPTURAS / '09_consola_cola_prioridad.png')
screenshot_placeholder(7, 'Consola - Archivo de Datos (JSON)', 'Guardado/carga exitosa de salunic_datos.json (mensajes [OK]).', CAPTURAS / '10_consola_json.png')

# 6
h1('6. Enlace al repositorio')
para('Código fuente del prototipo:')
p = doc.add_paragraph()
r = p.add_run(REPO)
r.bold = True
r.font.size = Pt(11)
para('Contenido relevante: Entidades/, Datos/, Funciones/, app/, consola/, docs/pdfs/, scripts/, salunic_datos.json, README.md.')
h2('Cómo ejecutar')
code_block('''# Aplicación gráfica (Tkinter)
py app/main.py

# Módulo por consola
py consola/main.py''')
h2('Resumen de cumplimiento (indicación IX)')
bullet('Módulos implementados: descritos por responsabilidades/capas.')
bullet('Validación de datos y manejo de excepciones: validadores, reintentos y try/except.')
bullet('Operaciones CRUD: por entidad (Usuario, Cita, Medicamento, Almacén/Stock).')
bullet('Búsqueda y ordenamiento: búsqueda lineal; prioridad/orden con heapq (turno de desempate).')
bullet('Interfaz Tkinter: navegación y pantallas funcionales (incl. Panel de Atención).')
bullet('Capturas de pantalla: espacios indicados para evidencias.')
bullet(f'Enlace al repositorio: {REPO}')

out = Path(r'C:\salunic-app\docs\pdfs\IX_Desarrollo_del_prototipo_en_Python_SALUNIC.docx')
out.parent.mkdir(parents=True, exist_ok=True)
doc.save(str(out))
print('ok')
print(out)
