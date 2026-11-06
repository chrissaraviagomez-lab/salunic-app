from fpdf import FPDF
from pathlib import Path

REPO = "https://github.com/chrissaraviagomez-lab/salunic-app"

class PDF(FPDF):
    def header(self):
        self.set_font('Helvetica', 'B', 9)
        self.cell(0, 6, 'SALUNIC - Entrega del Proyecto | Seccion IX. Desarrollo del prototipo en Python', align='C', new_x='LMARGIN', new_y='NEXT')
        self.ln(1)
    def footer(self):
        self.set_y(-15)
        self.set_font('Helvetica', 'I', 8)
        self.cell(0, 10, f'Pagina {self.page_no()}', align='C')

pdf = PDF()
pdf.set_auto_page_break(auto=True, margin=14)

def _break_long_tokens(s, n=60):
    s = str(s).replace('\t','  ')
    # insert soft breaks into very long tokens (URLs/paths)
    out = []
    for tok in s.split(' '):
        while len(tok) > n:
            out.append(tok[:n]); tok = tok[n:]
        out.append(tok)
    return ' '.join(out)

def _mc(w, h, txt, **kw):
    pdf.set_x(pdf.l_margin if w == 0 else pdf.get_x())
    pdf.multi_cell(w, h, _break_long_tokens(txt), **kw)

def h1(t):
    pdf.set_font('Helvetica','B',15); pdf.ln(2); _mc(0,8,t); pdf.ln(1)
def h2(t):
    pdf.set_font('Helvetica','B',11.5); pdf.ln(1); _mc(0,6.5,t); pdf.ln(0.5)
def h3(t):
    pdf.set_font('Helvetica','B',10.5); pdf.ln(0.5); _mc(0,6,t)
def p(t, size=10):
    pdf.set_font('Helvetica','',size); _mc(0,5,t); pdf.ln(1)
def bullet(t, size=10):
    pdf.set_font('Helvetica','',size); _mc(0,5,'- ' + str(t)); pdf.ln(0.3)
def code(txt):
    pdf.set_font('Courier','',7.4); pdf.set_fill_color(245,245,245)
    for line in str(txt).split('\n'):
        s = _break_long_tokens(line.replace('\t','  '), n=95)
        while len(s) > 105:
            chunk, s = s[:105], s[105:]
            pdf.set_x(pdf.l_margin); pdf.multi_cell(0,3.8,chunk, fill=True, new_x='LMARGIN', new_y='NEXT')
        if s == '': s = ' '
        pdf.set_x(pdf.l_margin); pdf.multi_cell(0,3.8,s, fill=True, new_x='LMARGIN', new_y='NEXT')
    pdf.ln(1)

def screenshot(title, desc, h=38):
    pdf.ln(1)
    pdf.set_font('Helvetica','B',9.5)
    pdf.set_x(pdf.l_margin)
    pdf.multi_cell(0,5,_break_long_tokens(f'[CAPTURA DE PANTALLA] {title}'))
    pdf.set_font('Helvetica','',9)
    pdf.set_x(pdf.l_margin)
    x = pdf.l_margin; y = pdf.get_y(); w = pdf.w - pdf.l_margin - pdf.r_margin
    if y + h > pdf.h - pdf.b_margin:
        pdf.add_page(); y = pdf.get_y()
    pdf.rect(x, y, w, h)
    pdf.set_xy(x+3, y+4)
    pdf.multi_cell(w-6,4.5, _break_long_tokens(f'Insertar aqui la captura: {desc}', n=50))
    pdf.set_xy(x, y+h+2)

# Portada
pdf.add_page()
pdf.set_font('Helvetica','B',18); pdf.ln(18)
pdf.cell(0,10,'SALUNIC - Sistema de Salud y Bienestar', align='C', new_x='LMARGIN', new_y='NEXT')
pdf.set_font('Helvetica','B',14); pdf.ln(4)
pdf.cell(0,8,'IX. Desarrollo del prototipo en Python', align='C', new_x='LMARGIN', new_y='NEXT')
pdf.ln(10)
pdf.set_font('Helvetica','',11)
info = [
    ('Proyecto:', 'SALUNIC (App Tkinter + Modulo Consola integrados)'),
    ('Lenguaje:', 'Python 3'),
    ('Interfaz grafica:', 'Tkinter'),
    ('Repositorio:', REPO),
]
for k,v in info:
    pdf.set_font('Helvetica','B',11); pdf.cell(45,7,k, new_x='END', new_y='TOP')
    pdf.set_font('Helvetica','',11); _mc(0,7,v)
pdf.ln(8)
p('Documento de entrega que describe los modulos implementados, la validacion de datos y el manejo de excepciones, las operaciones CRUD, los algoritmos de busqueda y ordenamiento, y la interfaz en Tkinter, con espacios para capturas de pantalla y el enlace al repositorio.', 10.5)

# 1. Modulos implementados
pdf.add_page(); h1('1. Modulos implementados')
p('El prototipo se organizo con una arquitectura modular para separar modelos, datos, logica e interfaces, cumpliendo la estructura requerida (Entidades, Datos, Funciones) y manteniendo integrados el modulo por consola y la aplicacion grafica.')

h2('1.1 Entidades/ (modelos - DataClass)')
p('Contiene las 4 clases de datos del sistema, implementadas con @dataclass (dataclasses de Python):')
bullet('usuario.py -> clase Usuario (id, nombre, email, password, telefono)')
bullet('cita_medica.py -> clase CitaMedica (id, paciente_id, medico_id, especialidad, fecha, hora, lugar)')
bullet('medicamento.py -> clase Medicamento (id, nombre, dosis, frecuencia, presentacion)')
bullet('almacen_medicamento.py -> clase AlmacenMedicamento (id, medicamento_id, cantidad, fecha_vencimiento)')
bullet('__init__.py -> exporta las entidades para importacion centralizada.')

h2('1.2 Datos/ (almacenamiento en memoria y persistencia)')
p('Gestiona las listas de objetos y el archivo JSON compartido:')
bullet('datos.py: define listas globales (usuarios, citas, medicamentos, almacen), datos iniciales de prueba, y funciones cargar_datos_iniciales(), guardar_datos() y cargar_datos().')
bullet('Persistencia en salunic_datos.json (raiz del proyecto), compartido entre app y consola.')
bullet('Serializacion con dataclasses.asdict() y reconstruccion con Clase(**dict).')

h2('1.3 Funciones/ (logica de negocio, una por DataClass + utilidades)')
p('Implementa la logica del sistema. Regla aplicada: Funciones solo usa Datos y Entidades.')
bullet('usuario.py, cita_medica.py, medicamento.py, almacen_medicamento.py: operaciones CRUD y consultas por cada entidad.')
bullet('validaciones.py: validacion de entradas y manejo de errores de datos (ValueError).')
bullet('busqueda_lineal.py: algoritmos de busqueda lineal.')
bullet('cola_atencion.py: cola de atencion con prioridad usando heapq.')
bullet('sistema.py: servicios de alto nivel para la app (iniciar/guardar, autenticacion, registro, citas, cola) sin exponer Datos directamente a la UI.')

h2('1.4 app/ (interfaz grafica Tkinter)')
p('Aplicacion de escritorio con navegacion entre pantallas. Regla aplicada: screens/ solo usa Funciones y Entidades.')
bullet('app/main.py: inicializa la app, precarga datos (Funciones.sistema.iniciar_sistema) y gestiona el cambio de pantallas (frames).')
bullet('app/screens/: pantallas como Login, Registro, Home, Citas, Panel de Atencion, Historial, Medicamentos, Estadisticas y formularios.')
bullet('app/data/users_data.py: adaptador de compatibilidad para operaciones de usuarios sobre la estructura unificada.')
bullet('app/screens/styles.py: estilos/colores y utilidades visuales (gradientes, componentes).')

h2('1.5 consola/ (modulo por consola)')
p('Interfaz interactiva por menus para demostrar la logica requerida usando la misma estructura:')
bullet('consola/main.py: menu principal y submenus (Usuarios, Citas, Medicamentos, Almacen/Inventario, Cola de Atencion con Prioridad, Archivo de Datos). Usa Entidades, Datos y Funciones.')

h2('1.6 Otros modulos/carpetas de apoyo')
bullet('core/: capa de compatibilidad que delega a Entidades/Datos/Funciones (estado unificado), conservada para no romper referencias previas.')
bullet('docs/pdfs/: documentacion y guias/PDFs de estudio y entrega.')
bullet('scripts/: scripts auxiliares (generacion de PDFs).')
bullet('salunic_datos.json: archivo de persistencia compartido.')

# 2. Validacion de datos y manejo de excepciones
pdf.add_page(); h1('2. Validacion de datos y manejo de excepciones')
p('Se implementaron validaciones para asegurar la calidad de los datos ingresados (especialmente en consola y en operaciones de registro/edicion) y manejo de excepciones para evitar fallos ante entradas invalidas o errores de E/S.')

h2('2.1 Validacion de datos (Funciones/validaciones.py)')
p('Funciones implementadas (lanzan ValueError cuando el dato no cumple):')
bullet('validar_nombre(texto): no vacio; solo letras/espacios (incluye acentos); normaliza formato (title).')
bullet('validar_email(email): no vacio; formato valido (expresion regular usuario@dominio).')
bullet('validar_password(password): minimo 4 caracteres.')
bullet('validar_fecha(fecha): formato DD/MM/AAAA con fecha real (datetime.strptime).')
bullet('validar_hora(hora): formato HH:MM valido (datetime.strptime).')
bullet('validar_dosis(dosis): no vacia.')
bullet('validar_celular(texto): no vacio; digitos/simbolos permitidos (+, -, espacio), longitud controlada.')
bullet('validar_cantidad(cantidad): no vacia; entero positivo (isdigit / conversion).')
bullet('validar_descripcion(texto): no vacia; normaliza texto.')
bullet('pedir_campo(etiqueta, validador): bucle interactivo que reintenta hasta recibir un valor valido, capturando ValueError y mostrando el mensaje de error.')

h2('2.2 Manejo de excepciones')
p('Se utilizan bloques try/except en puntos criticos:')
bullet('Entrada de datos en consola: pedir_opcion() valida que la opcion sea numerica; pedir_campo() captura ValueError por validaciones.')
bullet('Persistencia JSON (Datos/datos.py y capas relacionadas): try/except al guardar y cargar (errores de archivo, formato JSON, decodificacion); se informa al usuario con mensajes [OK]/[ERROR]/[INFO].')
bullet('Interfaz Tkinter (app): validaciones basicas en formularios (campos vacios, formato de correo, longitud de contrasena) con messagebox.showerror; y try/except en acciones que interactuan con datos/sistema para evitar cierres inesperados (ej. carga inicial, agregar cita/cola).')
bullet('Reglas de negocio: se previenen duplicados (ej. usuario por email) y se retornan valores/estados seguros (None/False) cuando corresponde.')
code('''# Ejemplo de validacion + manejo de excepcion (consola/Funciones)
def pedir_campo(etiqueta, validador):
    while True:
        try:
            valor = input(etiqueta)
            return validador(valor)      # puede lanzar ValueError
        except ValueError as e:
            print(f"  [Error] {e}")      # manejo controlado y reintento''')

# 3. Operaciones CRUD
pdf.add_page(); h1('3. Operaciones CRUD')
p('Se implementaron operaciones CRUD (Crear, Leer/Buscar/Listar, Actualizar, Eliminar) para las entidades principales, organizadas en un archivo de funciones por cada DataClass dentro de Funciones/. Ademas se incluyen conteos/listados y operaciones sobre el inventario (almacen/stock).')

h2('3.1 Usuario (Funciones/usuario.py)')
bullet('Crear: registrar_usuario() - solicita datos, valida, verifica duplicado por email, asigna ID y agrega a la lista.')
bullet('Leer/Buscar: buscar_usuario(email), listar_usuarios().')
bullet('Actualizar: actualizar_usuario(email) - permite modificar campos (con validacion).')
bullet('Eliminar: eliminar_usuario(email).')
bullet('Conteo: contar_usuarios().')

h2('3.2 Cita Medica (Funciones/cita_medica.py)')
bullet('Crear: registrar_cita() - registra cita con paciente, medico, especialidad, fecha, hora y lugar (validaciones de fecha/hora).')
bullet('Leer/Buscar: buscar_cita(medico_id), listar_citas(lista=None).')
bullet('Actualizar: actualizar_cita(medico_id).')
bullet('Eliminar: eliminar_cita(medico_id).')
bullet('Conteo: contar_citas().')

h2('3.3 Medicamento (Funciones/medicamento.py)')
bullet('Crear: registrar_medicamento().')
bullet('Leer/Buscar: buscar_medicamento(nombre), listar_medicamentos(lista=None).')
bullet('Actualizar: actualizar_medicamento(nombre).')
bullet('Eliminar: eliminar_medicamento(nombre).')
bullet('Conteo: contar_medicamentos().')

h2('3.4 Almacen / Inventario (Funciones/almacen_medicamento.py)')
bullet('Crear: registrar_stock() (asocia stock a medicamento_id, cantidad, vencimiento).')
bullet('Leer/Buscar: buscar_stock(medicamento_id), listar_stock(lista=None).')
bullet('Actualizar: actualizar_stock(medicamento_id).')
bullet('Eliminar: eliminar_stock(medicamento_id).')
bullet('Conteo: contar_stock().')

h2('3.5 Integracion de CRUD con la app y consola')
bullet('Consola: submenus invocan directamente las funciones CRUD por entidad y permiten guardar/cargar JSON.')
bullet('App: utiliza Funciones.sistema y funciones asociadas para operaciones como autenticacion/registro, consulta y agregado de citas, respetando la regla de acceso (screens no accede directo a Datos).')

# 4. Algoritmos de busqueda y ordenamiento
pdf.add_page(); h1('4. Algoritmos de busqueda y ordenamiento')

h2('4.1 Busqueda lineal (Funciones/busqueda_lineal.py)')
p('Se implemento busqueda lineal (secuencial), que recorre la lista elemento por elemento comparando el criterio hasta encontrar coincidencia(s). Es clara, didactica y adecuada para las estructuras en memoria del prototipo.')
code('''def busqueda_lineal(lista, criterio, atributo):
    resultados = []
    for elemento in lista:                         # recorrido secuencial
        valor = getattr(elemento, atributo, None)
        if isinstance(valor, str) and isinstance(criterio, str):
            if valor.lower() == criterio.lower():
                resultados.append(elemento)
        elif valor == criterio:
            resultados.append(elemento)
    return resultados''')
bullet('busqueda_lineal_por_email(usuarios, email): busqueda especifica usada para localizar usuarios (y en la autenticacion/login via la logica del sistema).')
bullet('busqueda_lineal_citas_por_medico(citas, medico_id) y busqueda_lineal_medicamento_por_nombre(medicamentos, nombre): variantes de filtrado lineal.')

h2('4.2 Ordenamiento / atencion por prioridad (heapq)')
p('Para la gestion de atencion se implemento una cola con PRIORIDAD (no FIFO puro), utilizando el modulo heapq de Python. El ordenamiento/seleccion del siguiente elemento se basa en una clave de prioridad:')
bullet('Adulto mayor: prioridad 0 (mayor prioridad).')
bullet('Normal: prioridad 1.')
bullet('turno_global: contador incremental para desempate (mantiene orden de llegada dentro del mismo nivel de prioridad).')
bullet('Estructura en heap: tuplas (prioridad, turno_global, item); heapq.heappop() extrae siempre la tupla de menor prioridad/turno, por lo que el adulto mayor se atiende primero aunque haya llegado despues.')
code('''import heapq
# encolar
prioridad = 0 if es_adulto_mayor else 1
heapq.heappush(self.cola, (prioridad, self.turno_global, item))
# atender (ordenado por prioridad)
prioridad, turno, atendido = heapq.heappop(self.cola)''')
p('Adicionalmente, para mostrar la cola en pantalla/consola se presenta una vista ordenada (sorted) por (prioridad, turno) sin alterar la logica de extraccion del heap.')

# 5. Interfaz en Tkinter
pdf.add_page(); h1('5. Interfaz en Tkinter')
p('La interfaz grafica se desarrollo con Tkinter (app/). La app utiliza un contenedor principal y muestra pantallas (Frames) segun la navegacion. El diseno visual mantiene un estilo consistente (fondos/gradientes, tarjetas, colores, tipografia) definido en app/screens/styles.py.')

h2('5.1 Estructura y navegacion')
bullet('app/main.py (clase SalunicApp): crea la ventana (375x812, no redimensionable), contenedor de pantallas y metodo show_screen() para cambiar de vista.')
bullet('Pantallas principales: Splash/Inicio, Login, Registro, Home, Citas, Panel de Atencion, Historial, Medicamentos, Estadisticas y formularios (ej. FormMedicamento, FormRegistro, flujo OTP de recuperacion).')
bullet('Carga inicial de datos: Funciones.sistema.iniciar_sistema() al iniciar, para trabajar con la persistencia compartida.')

h2('5.2 Funcionalidades visibles en la GUI')
bullet('Login: validacion de campos y autenticacion mediante la logica del sistema (busqueda lineal por email en la capa de Funciones/Datos).')
bullet('Registro de usuario: crea el usuario (DataClass) a traves de Funciones.sistema y guarda en JSON.')
bullet('Citas: visualiza citas desde la logica compartida, permite agregar nuevas citas y enviar pacientes a la cola indicando si es adulto mayor (prioridad).')
bullet('Panel de Atencion: muestra el paciente "EN ATENCION" y la "COLA DE ESPERA" ordenada por prioridad; boton "ATENDER SIGUIENTE" ejecuta el desencolado por prioridad (heapq).')

h2('5.3 Capturas de pantalla (insertar en los espacios indicados)')
screenshot('1. Pantalla de inicio/login', 'Ventana principal de la app Tkinter mostrando acceso/login (y/o splash/inicio).', 36)
screenshot('2. Registro / Home', 'Formulario de registro o pantalla Home con opciones del sistema.', 36)
pdf.add_page()
screenshot('3. Gestion de Citas', 'Pantalla de Citas: listado y opcion para agregar nueva cita / agregar a cola con prioridad.', 40)
screenshot('4. Panel de Atencion (cola con prioridad)', 'Panel mostrando EN ATENCION y COLA DE ESPERA; evidencia de prioridad (adulto mayor primero) y boton Atender Siguiente.', 42)
screenshot('5. Modulo por consola', 'Ejecucion de py consola/main.py: menu principal y/o submenu de Cola de Atencion con Prioridad y Archivo de Datos (JSON).', 42)
p('Nota: inserte las capturas reales tomadas durante la ejecucion de la app (py app/main.py) y la consola (py consola/main.py). Las imagenes deben evidenciar el funcionamiento de login/registro, CRUD/citas, cola con prioridad, y persistencia JSON.', 9.5)

# 6. Enlace al repositorio
pdf.add_page(); h1('6. Enlace al repositorio')
p('El codigo fuente del prototipo se encuentra en el siguiente repositorio:')
pdf.set_font('Helvetica','B',11)
pdf.set_x(pdf.l_margin)
pdf.multi_cell(0,7, REPO)
pdf.ln(2)
p('Contenido relevante en el repositorio: carpetas Entidades/, Datos/, Funciones/, app/, consola/, docs/pdfs/, scripts/, archivo salunic_datos.json y README.md con instrucciones de ejecucion y estructura.')

h2('Como ejecutar (referencia)')
code('''# Aplicacion grafica (Tkinter)
py app/main.py

# Modulo por consola
py consola/main.py''')

h2('Resumen de cumplimiento de la indicacion IX')
bullet('Modulos implementados: descritos por carpetas/responsabilidades (Entidades, Datos, Funciones, app, consola, core compatibilidad).')
bullet('Validacion de datos y manejo de excepciones: validadores (ValueError), reintentos en consola, try/except en JSON e interfaz.')
bullet('Operaciones CRUD: implementadas por entidad (Usuario, CitaMedica, Medicamento, Almacen/Stock).')
bullet('Algoritmos de busqueda y ordenamiento: busqueda lineal; cola con prioridad/orden por prioridad mediante heapq (turno de desempate).')
bullet('Interfaz en Tkinter: navegacion por pantallas, login/registro/citas/panel de atencion.')
bullet('Capturas de pantalla: espacios indicados para insercion de evidencias.')
bullet(f'Enlace al repositorio: {REPO}')

out = Path(r'C:\salunic-app\docs\pdfs\IX_Desarrollo_del_prototipo_en_Python_SALUNIC.pdf')
out.parent.mkdir(parents=True, exist_ok=True)
pdf.output(str(out))
print('ok')
print(out)
