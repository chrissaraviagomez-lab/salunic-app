from pathlib import Path
from docx import Document
from docx.shared import Pt, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.style import WD_STYLE_TYPE
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

REPO = "https://github.com/chrissaraviagomez-lab/salunic-app"

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

def screenshot_placeholder(n, title, desc):
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
h2('5.3 Capturas de pantalla (insertar evidencia)')
para('Inserte las capturas reales tomadas al ejecutar la app (py app/main.py) y la consola (py consola/main.py).')
screenshot_placeholder(1, 'Inicio / Login (App Tkinter)', 'Ventana de la app mostrando la pantalla de inicio o login con campos de correo/contraseña y botones.')
screenshot_placeholder(2, 'Registro de usuario o Home', 'Formulario de registro completado/confirmación o pantalla Home con accesos (Citas, Atención, etc.).')
screenshot_placeholder(3, 'Gestión de Citas (App)', 'Pantalla de Citas mostrando listado y/o el flujo para agregar una nueva cita y la opción de agregar a cola con prioridad (adulto mayor).')
screenshot_placeholder(4, 'Panel de Atención - Cola con prioridad (App)', 'Pantalla "Panel de Atención" con secciones EN ATENCIÓN y COLA DE ESPERA, evidenciando que un ADULTO MAYOR aparece/atiende antes; botón "ATENDER SIGUIENTE".')
screenshot_placeholder(5, 'Módulo por consola - Menús principales', 'Terminal ejecutando `py consola/main.py`: menú principal de SALUNIC con opciones (Usuarios, Citas, Medicamentos, Almacén, Cola de Atención con Prioridad, Archivo de Datos).')
screenshot_placeholder(6, 'Consola - Cola con prioridad (evidencia)', 'Submenú de Cola de Atención: pacientes agregados (normal y adulto mayor) y resultado de "Atender siguiente" mostrando que se atiende primero el ADULTO MAYOR (PRIORITARIO).')
screenshot_placeholder(7, 'Consola - Archivo de Datos (JSON)', 'Submenú Archivo de Datos mostrando guardado/carga exitosa de salunic_datos.json (mensajes [OK]) o listado que evidencie persistencia.')

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
