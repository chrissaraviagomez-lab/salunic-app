from fpdf import FPDF
from pathlib import Path
from datetime import datetime
from PIL import Image

CODIGO = Path(r"C:\salunic-app\docs\capturas\codigo")

class PDF(FPDF):
    def header(self):
        self.set_font('Helvetica', 'B', 8.5)
        self.cell(0, 6, 'SALUNIC - Guia de Estudio Final (Estructura Requerida por el Profesor)', align='C', new_x='LMARGIN', new_y='NEXT')
        self.ln(1)
    def footer(self):
        self.set_y(-15)
        self.set_font('Helvetica', 'I', 8)
        self.cell(0, 10, f'Pagina {self.page_no()}', align='C')

pdf = PDF()
pdf.set_auto_page_break(auto=True, margin=14)

def h1(t):
    pdf.set_font('Helvetica','B',15); pdf.ln(2); pdf.cell(0,9,t,new_x='LMARGIN', new_y='NEXT'); pdf.ln(1)
def h2(t):
    pdf.set_font('Helvetica','B',12); pdf.ln(1); pdf.cell(0,7,t,new_x='LMARGIN', new_y='NEXT'); pdf.ln(1)
def p(txt, size=10):
    pdf.set_font('Helvetica','',size)
    # prevent fpdf2 hard breaks on long tokens
    safe = txt.replace('\t','    ')
    pdf.set_x(pdf.l_margin)
    pdf.multi_cell(0,5,safe)
    pdf.ln(1)
def code(txt):
    pdf.set_font('Courier','',7.8); pdf.set_fill_color(245,245,245)
    pdf.set_x(pdf.l_margin)
    for line in txt.split('\n'):
        safe = line.replace('\t','  ')
        # hard-wrap very long lines to avoid horizontal-space exceptions
        while len(safe) > 105:
            chunk, safe = safe[:105], safe[105:]
            pdf.set_x(pdf.l_margin)
            pdf.multi_cell(0,4.0, chunk, fill=True, new_x='LMARGIN', new_y='NEXT')
        if safe == '':
            safe = ' '
        pdf.set_x(pdf.l_margin)
        pdf.multi_cell(0,4.0, safe, fill=True, new_x='LMARGIN', new_y='NEXT')
    pdf.ln(1)

# Portada
pdf.add_page()
pdf.set_font('Helvetica','B',20); pdf.ln(18)
pdf.cell(0,10,'SALUNIC', align='C', ln=True)
pdf.set_font('Helvetica','B',14)
pdf.cell(0,8,'Sistema de Salud y Bienestar', align='C', ln=True)
pdf.ln(4)
pdf.set_font('Helvetica','',12)
pdf.cell(0,7,'GUIA DE ESTUDIO FINAL - EXPLICATIVA', align='C', ln=True)
pdf.cell(0,7,'App Tkinter + Modulo Consola (Integrados)', align='C', ln=True)
pdf.ln(8)
pdf.set_font('Helvetica','B',11)
pdf.cell(0,7,'Estructura requerida por el profesor:', align='C', ln=True)
pdf.set_font('Helvetica','',11)
pdf.cell(0,6,'Entidades/  +  Datos/  +  Funciones/  +  screens/ (app)  +  consola/', align='C', ln=True)
pdf.ln(6)
pdf.cell(0,6,'Temas: DataClass | Cola con Prioridad (heapq) | Busqueda Lineal | Archivo JSON', align='C', ln=True)
pdf.ln(4)
pdf.set_font('Helvetica','I',9)
pdf.cell(0,6,f'Actualizado: {datetime.now().strftime("%d/%m/%Y")} | Codigo fuente: GitHub (salunic-app)', align='C', ln=True)
pdf.ln(16)
pdf.set_font('Helvetica','',10)
pdf.multi_cell(0,5,'Objetivo de este PDF: que puedas estudiar y entender TODO el proyecto (estructura, reglas, conexion entre partes, codigo clave y capturas del codigo real) para explicarlo y defenderlo con seguridad.', align='C')

# Indice
pdf.add_page(); h1('INDICE')
items=[
'1. Que pide el profesor y que cumple el proyecto',
'2. Estructura FINAL de carpetas (arbol) y para que sirve cada una',
'3. Reglas de acceso (MUY IMPORTANTE)',
'4. Entidades/ - Las 4 DataClass (modelos de datos)',
'5. Datos/ - Listas en memoria + datos iniciales + JSON (persistencia)',
'6. Funciones/ - Una por cada DataClass + utilidades (logica)',
'7. Cola con Prioridad (heapq): como funciona y por que adulto mayor va primero',
'8. Busqueda Lineal: como funciona y donde se usa',
'9. Archivo de Datos JSON: guardar y cargar (asdict / reconstruccion)',
'10. App Tkinter (app/): como usa solo Funciones y Entidades',
'11. Modulo Consola (consola/): como usa Entidades, Datos y Funciones',
'12. Conexion App <-> Consola <-> Datos compartidos (flujo completo)',
'13. Archivos clave explicados (que hace cada uno)',
'14. Como ejecutar y probar',
'15. Tips para exponer y defender (guion + respuestas tipicas)',
'16. Checklist final',
'17. Capturas del codigo real (evidencias para estudiar)']
for it in items: pdf.set_font('Helvetica','',10); pdf.cell(0,6,it,ln=True)

# 1
pdf.add_page(); h1('1. Que pide el profesor y que cumple el proyecto')
p('El profesor indico una estructura y reglas claras para organizar el codigo, ademas de los temas de programacion solicitados. SALUNIC cumple con lo siguiente:')
h2('Temas / requisitos funcionales')
p('- Lista de DataClass (4 clases de entidad).')
p('- Uso de Cola con PRIORIDAD (no FIFO puro): el adulto mayor se atiende antes aunque llegue despues.')
p('- Busqueda lineal (recorrer elemento por elemento).')
p('- Archivo de datos (persistencia en JSON).')
p('- App Tkinter y modulo por consola funcionando e integrados con la misma logica/datos.')
h2('Estructura requerida')
p('- Entidades/: DataClass (modelos).')
p('- Datos/ (o Datos/Data): listas con datos guardados + carga/guardado.')
p('- Funciones/: un archivo por cada DataClass (y utilidades relacionadas).')
p('- screens/: pantallas de la app (Tkinter).')
h2('Idea central')
p('Separar responsabilidades: Entidades define "que es" cada dato, Datos guarda "los datos", Funciones define "que se puede hacer" con esos datos, y las interfaces (screens de app y consola) usan esas funciones. Asi el codigo es ordenado, reutilizable y facil de defender.')

# 2
pdf.add_page(); h1('2. Estructura FINAL de carpetas (arbol)')
code('''C:\\salunic-app\\
|-- Entidades/                 # DataClass (4)
|   |-- __init__.py
|   |-- usuario.py             # Usuario
|   |-- cita_medica.py         # CitaMedica
|   |-- medicamento.py         # Medicamento
|   `-- almacen_medicamento.py # AlmacenMedicamento
|
|-- Datos/                     # Listas + persistencia JSON
|   |-- __init__.py
|   `-- datos.py               # listas, datos iniciales, cargar/guardar JSON
|
|-- Funciones/                 # Logica (1 por dataclass) + utilidades
|   |-- __init__.py
|   |-- usuario.py             # CRUD/ops de Usuario
|   |-- cita_medica.py         # CRUD/ops de CitaMedica
|   |-- medicamento.py         # CRUD/ops de Medicamento
|   |-- almacen_medicamento.py # CRUD/ops de Almacen/Stock
|   |-- sistema.py             # funciones de alto nivel para la app
|   |-- busqueda_lineal.py     # busqueda lineal
|   |-- cola_atencion.py       # cola con prioridad (heapq)
|   `-- validaciones.py        # validaciones/reutilizacion
|
|-- app/                       # App grafica Tkinter
|   |-- main.py
|   |-- data/
|   `-- screens/               # UI (usa Funciones y Entidades)
|
|-- consola/                   # Modulo por consola (usa Entidades, Datos, Funciones)
|   `-- main.py
|
|-- core/                      # Compatibilidad / version previa (no requerida)
|-- docs/                      # Documentacion y PDFs
|-- scripts/                   # Scripts auxiliares
|-- salunic_datos.json         # Archivo de datos compartido (persistencia)
`-- README / .bat''')
p('Nota: "core/" se conserva SOLO por compatibilidad y delega a Entidades/Datos/Funciones; no es la estructura principal. La estructura que se debe mostrar/defender es Entidades + Datos + Funciones, con app/screens y consola consumiendo esa logica.')
p('Archivos de apoyo actuales: app/data/users_data.py (adaptador de compatibilidad de la app) y scripts/ (generacion de capturas y documentos). No forman parte de la logica principal.')

# 3
pdf.add_page(); h1('3. Reglas de acceso (MUY IMPORTANTE)')
p('Estas reglas evitan el desorden y demuestran buena arquitectura:')
h2('Regla A - screens/ (interfaz grafica)')
p('Los archivos dentro de screens/ SOLO pueden usar: Funciones y Entidades.')
p('NO deben acceder directamente a Datos/ (ni leer/modificar listas desde la UI). La UI pide acciones a Funciones (ej: sistema.autenticar_usuario, sistema.agregar_cita, sistema.agregar_a_cola).')
h2('Regla B - Funciones/')
p('Los archivos de Funciones SOLO pueden usar: Datos y Entidades.')
p('Aqui vive la logica: validaciones, CRUD, busqueda, cola, y operaciones que modifican las listas de Datos.')
h2('Regla C - consola/')
p('El modulo consola usa Datos y Funciones (las Entidades se crean/usan dentro de Funciones) para cumplir lo requerido y compartir la misma logica. Importa menus/acciones desde Funciones y puede leer listas de Datos para flujos interactivos (ej: encolar una cita existente).')
p('En el codigo actual consola/main.py importa: Datos (listas y cargar/guardar), Funciones.usuario/cita_medica/medicamento/almacen_medicamento y Funciones.cola_atencion.')
h2('Por que importa')
p('Si la UI tocara Datos directamente, se duplicaria logica y seria mas dificil mantener. Centralizar en Funciones permite que app y consola se comporten igual y usen el mismo archivo JSON.')

# 4
pdf.add_page(); h1('4. Entidades/ - Las 4 DataClass')
p('Una DataClass (@dataclass) es una clase de Python que simplifica crear "modelos" para guardar datos (genera automaticamente __init__, representacion, etc.). Cada entidad representa algo real del sistema.')
code('''# Entidades/usuario.py
from dataclasses import dataclass

@dataclass
class Usuario:
    id: int
    nombre: str
    email: str
    password: str
    telefono: str = "+505 00000000"''')
p('Explicacion: Usuario guarda identificacion y credenciales/contacto. Se usa para login/registro y para relacionar citas (paciente/medico por id).')
code('''# Entidades/cita_medica.py
@dataclass
class CitaMedica:
    id: int
    paciente_id: int
    medico_id: int
    especialidad: str
    fecha: str   # DD/MM/AAAA
    hora: str    # HH:MM
    lugar: str = "Hospital"''')
p('Explicacion: CitaMedica conecta un paciente con un medico y guarda cuando/donde es la cita. Las citas son las que se pueden enviar a la cola de atencion.')
code('''# Entidades/medicamento.py / almacen_medicamento.py
@dataclass
class Medicamento:
    id: int; nombre: str; dosis: str; frecuencia: str; presentacion: str = "Tabletas"

@dataclass
class AlmacenMedicamento:
    id: int; medicamento_id: int; cantidad: int; fecha_vencimiento: str''')
p('Explicacion: Medicamento describe el producto; AlmacenMedicamento representa el stock/inventario (cantidad y vencimiento) asociado a un medicamento_id. Esto separa catalogo vs inventario.')
p('Las 4 DataClass pedidas estan presentes: Usuario, CitaMedica, Medicamento, AlmacenMedicamento. Se exportan desde Entidades/__init__.py para importarlas facil: from Entidades import Usuario, ...')

# 5
pdf.add_page(); h1('5. Datos/ - Listas en memoria + JSON')
p('Datos/datos.py cumple el rol de "almacen de datos" del programa:')
p('1) Define listas en memoria (mientras corre el programa): usuarios, citas, medicamentos, almacen.')
p('2) Define datos iniciales de ejemplo para pruebas.')
p('3) Implementa persistencia con Archivo JSON: cargar_datos() y guardar_datos().')
code('''# Datos/datos.py (idea)
from dataclasses import asdict
from Entidades import Usuario, CitaMedica, Medicamento, AlmacenMedicamento
import json, os

usuarios = []
citas = []
medicamentos = []
almacen = []

ARCHIVO_DATOS = ... "salunic_datos.json" (ruta en la raiz del proyecto)

def guardar_datos():
    data = {"usuarios":[asdict(u) for u in usuarios], ...}
    json.dump(data, f, ensure_ascii=False, indent=4)

def cargar_datos():
    data = json.load(f)  # utf-8-sig para tolerar BOM
    usuarios.clear(); ...
    usuarios.append(Usuario(**u))  # reconstruccion desde dict''')
p('Puntos clave para explicar:')
p('- "Listas de las dataclass": cada lista contiene objetos de su DataClass correspondiente.')
p('- Se guarda en JSON con asdict() (convierte el objeto DataClass a diccionario).')
p('- Se carga reconstruyendo objetos con Clase(**diccionario).')
p('- El JSON se guarda en la raiz (salunic_datos.json) para que app y consola compartan los mismos datos.')

# 6
pdf.add_page(); h1('6. Funciones/ - Una por cada DataClass + utilidades')
p('La carpeta Funciones contiene la logica del sistema. Cumple la regla: usa solo Datos y Entidades.')
h2('Un archivo por cada DataClass (requisito)')
p('- Funciones/usuario.py -> operaciones de Usuario (registrar, buscar, listar, actualizar, eliminar, contar).')
p('- Funciones/cita_medica.py -> operaciones de CitaMedica.')
p('- Funciones/medicamento.py -> operaciones de Medicamento.')
p('- Funciones/almacen_medicamento.py -> operaciones de AlmacenMedicamento (stock).')
h2('Utilidades / modulos de apoyo')
p('- Funciones/busqueda_lineal.py -> implementa busqueda lineal (requisito).')
p('- Funciones/cola_atencion.py -> cola con prioridad usando heapq (requisito).')
p('- Funciones/validaciones.py -> valida entradas (nombre, email, fecha, hora, etc.).')
p('- Funciones/sistema.py -> funciones de alto nivel para la app (iniciar/guardar, autenticar, registrar, agregar cita, cola) respetando reglas desde la UI.')
code('''# Ejemplo (idea): Funciones/usuario.py
from Entidades import Usuario
from Datos import usuarios
from .validaciones import ...

def buscar_usuario(email):
    for u in usuarios:           # acceso a Datos (lista)
        if u.email == email:
            return u
    return None''')
p('Para la defensa: "Cada DataClass tiene su archivo de funciones, y las funciones operan sobre las listas de Datos usando las Entidades".')

# 7
pdf.add_page(); h1('7. Cola con Prioridad (heapq)')
p('Requisito clave: NO es una cola FIFO pura. Si llega un adulto mayor despues, debe atenderse antes que un paciente normal que llego antes (prioridad).')
h2('Como se implementa')
p('Se usa el modulo heapq de Python (cola de prioridad / heap). Guardamos elementos como tuplas: (prioridad, turno_global, item). heapq siempre extrae el elemento con MENOR valor en la primera posicion.')
code('''import heapq

# encolar
if es_adulto_mayor:
    prioridad = 0   # MAYOR prioridad
    tipo = "ADULTO MAYOR (PRIORITARIO)"
else:
    prioridad = 1   # NORMAL

heapq.heappush(self.cola, (prioridad, self.turno_global, item))

# desencolar (atiende al de mayor prioridad)
prioridad, turno, atendido = heapq.heappop(self.cola)''')
h2('Por que funciona')
p('- prioridad=0 (adulto mayor) es menor que prioridad=1 (normal), por eso heapq lo saca primero.')
p('- turno_global es un contador incremental: desempata cuando dos pacientes tienen la misma prioridad (conserva orden de llegada dentro del mismo nivel).')
p('- Resultado: adulto mayor primero, sin importar el orden de llegada frente a normales.')
h2('Donde se ve')
p('- Consola: menu "Cola de Atencion con Prioridad" (agregar, atender, mostrar).')
p('- App: pantalla Citas (agregar a cola) y pantalla "Panel de Atencion" (visualiza cola y atiende siguiente).')

# 8
pdf.add_page(); h1('8. Busqueda Lineal')
p('La busqueda lineal recorre una lista elemento por elemento, comparando hasta encontrar el/los que coinciden. Es simple y clara para explicar.')
code('''# Funciones/busqueda_lineal.py (idea)
def busqueda_lineal(lista, criterio, atributo):
    resultados = []
    for elemento in lista:                 # recorre uno por uno
        valor = getattr(elemento, atributo, None)
        if str(valor).lower() == str(criterio).lower():
            resultados.append(elemento)
    return resultados

def busqueda_lineal_por_email(usuarios, email):
    for u in usuarios:
        if u.email.lower() == email.lower():
            return u
    return None''')
h2('Donde se usa')
p('- Login de la app: autentica buscando el usuario por email con busqueda lineal (via Funciones.sistema / busqueda_lineal_por_email) y comparando password.')
p('- Puede usarse tambien para filtrar citas/medicamentos por criterio (segun funciones disponibles).')
p('Para la defensa: "Uso un ciclo for, reviso cada elemento y comparo; si coincide, lo retorno/agrego. Eso es busqueda lineal".')

# 9
pdf.add_page(); h1('9. Archivo de Datos JSON (persistencia)')
p('La persistencia permite que los datos no se pierdan al cerrar el programa. Se usa un archivo JSON compartido: salunic_datos.json (en la raiz del proyecto).')
h2('Guardar (serializar)')
p('- Tomamos las listas de DataClass (usuarios, citas, medicamentos, almacen).')
p('- Convertimos cada objeto a diccionario con asdict(obj).')
p('- Escribimos el JSON con json.dump(..., ensure_ascii=False, indent=4).')
h2('Cargar (deserializar)')
p('- Leemos el JSON con json.load (usando utf-8-sig por compatibilidad).')
p('- Limpiamos las listas actuales (clear) para evitar duplicados.')
p('- Reconstruimos objetos DataClass: Usuario(**u), CitaMedica(**c), etc., y los agregamos a las listas.')
h2('Integracion')
p('Como app y consola usan la misma estructura de Datos/Funciones y el mismo archivo JSON en la raiz, ambos pueden trabajar sobre los mismos datos guardados.')

# 10
pdf.add_page(); h1('10. App Tkinter (app/) - usa solo Funciones y Entidades')
p('La app grafica esta en app/ (Tkinter). Las pantallas importantes fueron ajustadas para cumplir la regla del profesor.')
h2('Regla aplicada en screens/')
p('app/screens/* importa y usa Funciones (ej: Funciones.sistema) y puede usar Entidades si es necesario; NO accede directamente a Datos/.')
h2('Ejemplos reales en el proyecto')
p('- app/screens/login_screen.py: llama sistema.autenticar_usuario(email, password). La busqueda lineal ocurre dentro de Funciones.')
p('- app/screens/registro_screen.py: llama sistema.registrar_usuario_app(...) para crear el usuario (DataClass) y guardar.')
p('- app/screens/citas_screen.py: obtiene/agrega citas via sistema.obtener_citas()/agregar_cita() y encola con sistema.agregar_a_cola(..., es_adulto_mayor).')
p('- app/screens/atencion_screen.py: "Panel de Atencion" muestra la cola (sistema.obtener_cola()) y atiende con sistema.atender_siguiente() usando la cola con prioridad.')
h2('app/main.py')
p('Precarga datos con Funciones.sistema.iniciar_sistema() y gestiona navegacion entre pantallas. La UI es visual (Tkinter), pero la logica de negocio viene de Funciones/Datos/Entidades.')

# 11
pdf.add_page(); h1('11. Modulo Consola (consola/) - alineado a la estructura')
p('El modulo por consola ofrece menus para gestionar Usuarios, Citas, Medicamentos, Almacen, Cola de Atencion y Archivo de Datos.')
h2('Como cumple la estructura requerida')
p('consola/main.py importa desde:')
p('- Datos: listas (usuarios, citas, medicamentos, almacen) y Datos.datos (cargar_datos, guardar_datos, cargar_datos_iniciales).')
p('- Funciones por dataclass: usuario, cita_medica, medicamento, almacen_medicamento (CRUD).')
p('- Funciones.cola_atencion (cola_atencion con heapq).')
p('Las Entidades se usan dentro de Funciones (por ejemplo, Funciones/usuario.py crea Usuario). La consola no duplica esa logica.')
h2('Que demuestra la consola')
p('- CRUD por entidad (a traves de Funciones).')
p('- Cola con prioridad: permite marcar adulto mayor y atiende por prioridad.')
p('- Archivo JSON: guardar/cargar desde el menu.')
p('- Comparte el mismo salunic_datos.json que la app, por lo que la integracion es real.')

# 12
pdf.add_page(); h1('12. Conexion App <-> Consola <-> Datos compartidos')
p('Este es el punto mas importante para defender la integracion:')
h2('Flujo de datos y logica')
p('1) Entidades definen la forma de los objetos (DataClass).')
p('2) Datos mantiene las listas (usuarios, citas, etc.) y el JSON compartido (salunic_datos.json).')
p('3) Funciones implementa la logica (validar, buscar lineal, encolar con prioridad, CRUD, guardar/cargar).')
p('4) La App (screens) llama a Funciones.sistema / Funciones.* sin tocar Datos directamente.')
p('5) La Consola llama a Funciones y usa Datos segun el flujo interactivo del menu.')
p('6) Ambos leen/escriben el MISMO archivo JSON -> los cambios persisten y se comparten.')
h2('Ejemplo de flujo (login en app)')
p('Usuario ingresa email/password en pantalla -> login_screen llama sistema.autenticar_usuario -> Funciones usa busqueda_lineal_por_email sobre Datos.usuarios -> retorna el Usuario (DataClass) si coincide.')
h2('Ejemplo de flujo (cola con prioridad)')
p('En Citas (app) o en Consola se indica si es adulto mayor -> se llama encolar(..., es_adulto_mayor=True/False) -> heapq ordena por (prioridad, turno) -> "Atender siguiente" siempre saca primero prioridad 0 (adulto mayor). El Panel de Atencion de la app lo muestra visualmente.')

# 13
pdf.add_page(); h1('13. Archivos clave explicados')
h2('Entidades/')
p('- usuario.py, cita_medica.py, medicamento.py, almacen_medicamento.py: definen las 4 DataClass. Son modelos simples y claros.')
h2('Datos/datos.py')
p('- Listas globales del sistema + cargar_datos_iniciales() + guardar_datos()/cargar_datos() con JSON. Punto unico de persistencia compartida.')
h2('Funciones/ (por dataclass)')
p('- usuario.py, cita_medica.py, medicamento.py, almacen_medicamento.py: CRUD y operaciones basicas. Usan Datos (listas) y Entidades (crear objetos).')
h2('Funciones/sistema.py')
p('- Capa de servicios para la app: iniciar_sistema, autenticar_usuario (busqueda lineal), registrar_usuario_app, agregar_cita, agregar_a_cola/atender_siguiente/obtener_cola. Facilita que screens no toquen Datos.')
h2('Funciones/busqueda_lineal.py')
p('- Implementa recorrido elemento por elemento. Incluye helpers como busqueda por email.')
h2('Funciones/cola_atencion.py')
p('- Clase ColaAtencion con heapq, prioridad adulto mayor, turno_global, encolar/desencolar/mostrar_cola. Instancia global cola_atencion.')
h2('app/screens/atencion_screen.py')
p('- Panel visual de atencion: muestra "EN ATENCION" y "COLA DE ESPERA", y boton para atender siguiente (demostracion fuerte de la cola con prioridad).')
h2('consola/main.py')
p('- Menu interactivo que integra todas las funciones requeridas (DataClass via modelo, cola, busqueda lineal en login/logica relacionada, JSON) usando la estructura Entidades/Datos/Funciones.')

# 14
pdf.add_page(); h1('14. Como ejecutar y probar')
h2('Requisitos')
p('- Python 3 instalado. Tkinter suele venir incluido. (Para generar PDFs se uso fpdf en scripts; no es necesario para correr la app/consola.)')
h2('Ejecutar app (Tkinter)')
p('Desde la carpeta del proyecto: ejecutar el lanzador .bat de la app o: py app/main.py (segun configuracion del entorno).')
h2('Ejecutar consola')
p('Ejecutar run_consola.bat o: py consola/main.py')
h2('Pruebas rapidas sugeridas')
p('1) Consola -> cargar/guardar JSON y listar entidades (verifica Datos/JSON).')
p('2) Consola -> Cola de atencion: agregar normal y adulto mayor; atender y confirmar que el adulto mayor sale primero (verifica heapq/prioridad).')
p('3) App -> Login/Registro (verifica busqueda lineal/autenticacion y uso de Funciones).')
p('4) App -> Citas: agregar cita y agregar a cola con prioridad.')
p('5) App -> Panel de Atencion: ver cola ordenada y atender siguiente (demostracion visual).')
p('6) Verificar que salunic_datos.json se actualiza en la raiz del proyecto.')

# 15
pdf.add_page(); h1('15. Tips para exponer y defender (guion)')
h2('Guion corto (1-2 minutos)')
p('"SALUNIC esta organizado con la estructura que pidio el profesor: Entidades (las 4 DataClass), Datos (listas y archivo JSON compartido) y Funciones (una por cada dataclass y utilidades). Las pantallas de la app solo usan Funciones y Entidades, y las Funciones solo usan Datos y Entidades. La consola tambien usa la misma estructura, por eso app y consola comparten la misma logica y el mismo salunic_datos.json."')
h2('Puntos que debes mencionar si o si')
p('- 4 DataClass: Usuario, CitaMedica, Medicamento, AlmacenMedicamento.')
p('- Cola con prioridad con heapq: adulto mayor prioridad 0, normal 1, turno_global desempata; heapq saca el menor -> adulto mayor primero.')
p('- Busqueda lineal: for elemento por elemento; usada en autenticacion/busquedas.')
p('- Archivo JSON: asdict para guardar, Clase(**dict) para cargar; archivo compartido.')
p('- Reglas de acceso: screens -> Funciones/Entidades; Funciones -> Datos/Entidades.')
h2('Respuestas tipicas')
p('P: "Por que no FIFO?" R: "Porque el requisito exige prioridad para adulto mayor; uso heapq con (prioridad, turno) para que se atienda antes aunque llegue despues."')
p('P: "Como se conectan app y consola?" R: "Comparten Entidades, Datos y Funciones, y el mismo JSON en la raiz; la logica no esta duplicada."')
p('P: "Donde esta la busqueda lineal?" R: "En Funciones/busqueda_lineal.py y se aplica en la autenticacion/consultas recorriendo la lista completa."')
p('P: "Que hace asdict?" R: "Convierte un objeto DataClass en diccionario para poder guardarlo en JSON."')

# 16
pdf.add_page(); h1('16. Checklist final')
checks=[
'[ ] Puedo mostrar las carpetas Entidades/, Datos/, Funciones/, app/screens/, consola/',
'[ ] Puedo explicar las 4 DataClass y donde estan',
'[ ] Puedo explicar que screens solo usan Funciones y Entidades',
'[ ] Puedo explicar que Funciones solo usan Datos y Entidades',
'[ ] Puedo mostrar/explicar la cola con prioridad (heapq, adulto mayor primero)',
'[ ] Puedo explicar la busqueda lineal y donde se usa',
'[ ] Puedo explicar guardar/cargar JSON (asdict y reconstruccion)',
'[ ] Puedo demostrar la app (login/citas/panel de atencion)',
'[ ] Puedo demostrar la consola (menus, cola, JSON)',
'[ ] Puedo explicar que app y consola comparten salunic_datos.json']
pdf.set_font('Helvetica','',10)
for c in checks: pdf.cell(0,6,c,ln=True)

pdf.ln(4)
pdf.set_font('Helvetica','B',11)
pdf.multi_cell(0,6,'Conclusion: si entiendes la separacion Entidades-Datos-Funciones, las reglas de acceso, y los 4 temas (DataClass, cola con prioridad, busqueda lineal, JSON), puedes explicar y defender el proyecto completo con confianza.')

# 17 - Capturas del codigo real
pdf.add_page(); h1('17. Capturas del codigo real (evidencias)')
p('Estas capturas corresponden al codigo actual del proyecto y sirven para estudiar/ensayar la defensa mostrando archivos y lineas concretas. Se generan con: py scripts/generar_capturas_codigo.py')
p('Carpeta: docs/capturas/codigo/')

def code_image(path, caption):
    path = Path(path)
    if not path.exists():
        p(f'[Falta captura: {path.name}]')
        return
    with Image.open(path) as im:
        iw, ih = im.size
    max_w, max_h = 180.0, 225.0
    scale = min(max_w / iw, max_h / ih)
    pdf.add_page()
    pdf.set_font('Helvetica','B',10)
    pdf.multi_cell(0,6,caption)
    pdf.ln(1)
    pdf.image(str(path), x=pdf.l_margin, w=iw * scale)
    pdf.ln(2)

for img, cap in [
    ('01_codigo_entidades_dataclass.png', 'Codigo 1 - Entidades (4 DataClass con @dataclass)'),
    ('02_codigo_datos_json.png', 'Codigo 2 - Datos y persistencia JSON (asdict, cargar/guardar, excepciones)'),
    ('03_codigo_validaciones_excepciones.png', 'Codigo 3 - Validaciones (ValueError) y manejo de excepciones'),
    ('04_codigo_crud_usuario.png', 'Codigo 4 - Operaciones CRUD (ejemplo Usuario)'),
    ('05_codigo_busqueda_lineal.png', 'Codigo 5 - Busqueda lineal (recorrido elemento por elemento)'),
    ('06_codigo_cola_prioridad_heapq.png', 'Codigo 6 - Cola con prioridad (heapq): adulto mayor primero'),
    ('07_codigo_tkinter_app.png', 'Codigo 7 - Interfaz Tkinter (app/main.py)'),
    ('08_codigo_consola_integrada.png', 'Codigo 8 - Consola integrada (Entidades/Datos/Funciones)'),
]:
    code_image(CODIGO / img, cap)

out1 = Path(r'C:\salunic-app\docs\pdfs\GUIA_COMPLETA_INTEGRACION_APP_CONSOLA_CORE_TIPS_DEFENSA.pdf')
out2 = Path(r'C:\salunic-app\docs\pdfs\GUIA_ESTUDIO_FINAL_SALUNIC_ESTRUCTURA_REQUERIDA.pdf')
pdf.output(str(out1))
# save a second copy with final name
pdf.output(str(out2))
print('ok')
print(out1)
print(out2)
