from fpdf import FPDF
from pathlib import Path

class PDF(FPDF):
    def header(self):
        self.set_font('Helvetica', 'B', 9)
        self.cell(0, 7, 'SALUNIC - Guía Completa para Exposición y Defensa | Integración App + Consola con core/', align='C', ln=True)
        self.ln(1)

    def footer(self):
        self.set_y(-15)
        self.set_font('Helvetica', 'I', 8)
        self.cell(0, 10, f'Página {self.page_no()}', align='C')

pdf = PDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()

# Portada
pdf.set_font('Helvetica', 'B', 20)
pdf.ln(15)
pdf.cell(0, 10, 'SALUNIC - Sistema de Salud y Bienestar', align='C', ln=True)
pdf.set_font('Helvetica', 'B', 16)
pdf.cell(0, 10, 'App Tkinter + Módulo por Consola Integrados', align='C', ln=True)
pdf.ln(5)
pdf.set_font('Helvetica', '', 12)
pdf.cell(0, 10, 'DataClass | Cola con Prioridad | Búsqueda Lineal | Archivo JSON', align='C', ln=True)
pdf.ln(20)
pdf.set_font('Helvetica', 'B', 12)
pdf.cell(0, 10, 'Guía para Estudio, Exposición y Defensa', align='C', ln=True)
pdf.ln(40)
pdf.set_font('Helvetica', '', 11)
pdf.cell(0, 10, 'Elaborado para comprensión y apropiación del código', align='C', ln=True)

# Índice
pdf.add_page()
pdf.set_font('Helvetica', 'B', 16)
pdf.cell(0, 10, 'ÍNDICE', ln=True)
pdf.ln(3)
pdf.set_font('Helvetica', '', 11)
idx = [
    "1. Objetivo de esta guía",
    "2. Estructura actual del proyecto",
    "3. ¿Cómo se conectan App, Consola y core/?",
    "4. DataClass (entidades.py)",
    "5. Cola con Prioridad con heapq (cola_atencion.py)",
    "6. Búsqueda Lineal (busqueda_lineal.py)",
    "7. Persistencia con Archivo JSON (archivo_datos.py)",
    "8. Integración en la App Tkinter",
    "9. Panel de Atención (Integración visual de la Cola)",
    "10. Flujo completo: Agregar a cola -> Ver -> Atender",
    "11. Tips para exponer y defender el código",
    "12. Checklist antes de exponer",
    "13. Conclusión"
]
for i, it in enumerate(idx):
    pdf.cell(0, 7, it, ln=True)
pdf.ln(2)

# 1
pdf.add_page()
pdf.set_font('Helvetica', 'B', 14)
pdf.cell(0, 10, '1. Objetivo de esta guía', ln=True)
pdf.ln(1)
pdf.set_font('Helvetica', '', 11)
pdf.multi_cell(0, 6, 'Esta guía tiene como finalidad entender paso a paso cómo está estructurado el proyecto SALUNIC ahora, cómo se unificó el módulo por consola con la aplicación gráfica Tkinter mediante la carpeta core/, y cómo explicar cada parte con seguridad al momento de exponer o defenderlo.')

# 2
pdf.ln(4)
pdf.set_font('Helvetica', 'B', 14)
pdf.cell(0, 10, '2. Estructura actual del proyecto', ln=True)
pdf.ln(1)
pdf.set_font('Helvetica', '', 10)
pdf.multi_cell(0, 5, 'Raiz del proyecto:\n\n- app/        -> Interfaz grafica Tkinter (Login, Registro, Citas, Home, Panel de Atencion)\n- consola/    -> Modulo por consola (menu, pruebas de logica)\n- core/       -> LOGICA COMPARTIDA (DataClass, Cola con Prioridad, Busqueda Lineal, Archivo JSON)\n- docs/       -> Documentacion, diagramas, capturas, PDFs\n- scripts/    -> Scripts auxiliares\n- run_app.bat / run_consola.bat / README.md')

pdf.ln(2)
pdf.set_font('Helvetica', 'B', 11)
pdf.cell(0, 8, 'Clave:', ln=True)
pdf.set_font('Helvetica', '', 10)
pdf.multi_cell(0, 5, 'core/ es el corazón del proyecto. Tanto app/ como consola/ importan desde ahí. Así evitamos duplicar código y demostramos reutilización.')

# 3
pdf.add_page()
pdf.set_font('Helvetica', 'B', 14)
pdf.cell(0, 10, '3. ¿Cómo se conectan App, Consola y core/?', ln=True)
pdf.ln(1)
pdf.set_font('Helvetica', '', 10)
pdf.multi_cell(0, 5, 'La idea es sencilla: toda la lógica que pide el profesor vive en core/.\n\n- consola/ importa desde core/ (entidades, datos, funciones, cola_atencion, busqueda_lineal, archivo_datos)\n- app/ importa desde core/ (login usa busqueda_lineal, registro usa entidades.Usuario, citas/atención usan cola_atencion y archivo_datos)\n\nGracias a esto, ambos módulos trabajan con las MISMAS clases, MISMAS listas y MISMO archivo salunic_datos.json.')
pdf.ln(2)
pdf.set_font('Helvetica', 'B', 11)
pdf.cell(0, 8, '¿Qué demuestra esto?', ln=True)
pdf.set_font('Helvetica', '', 10)
pdf.multi_cell(0, 5, 'Que entendimos el objetivo: integrar la lógica al sistema, no tener dos programas aislados. La app gráfica ahora hace uso real de lo implementado en el módulo por consola.')

# 4
pdf.add_page()
pdf.set_font('Helvetica', 'B', 14)
pdf.cell(0, 10, '4. DataClass (entidades.py)', ln=True)
pdf.ln(1)
pdf.set_font('Helvetica', '', 10)
pdf.multi_cell(0, 5, 'Ubicación: core/entidades.py\n\nUsamos @dataclass para representar entidades del sistema con menos código y mayor claridad.\n\nClases:\n- Usuario: id, nombre, email, password, telefono\n- CitaMedica: id, paciente_id, medico_id, especialidad, fecha, hora, lugar\n- Medicamento: id, nombre, dosis, frecuencia, presentacion\n- AlmacenMedicamento: id, medicamento_id, cantidad, fecha_vencimiento\n\nUso en app: Al registrar, creamos entidades.Usuario(...) y lo agregamos a core.datos.usuarios para mantener la misma estructura.')
pdf.ln(2)

# 5
pdf.set_font('Helvetica', 'B', 14)
pdf.cell(0, 10, '5. Cola con Prioridad con heapq (cola_atencion.py)', ln=True)
pdf.ln(1)
pdf.set_font('Helvetica', '', 10)
pdf.multi_cell(0, 5, 'Ubicación: core/cola_atencion.py\n\nImportamos heapq. La clave es usar una tupla (prioridad, turno_global, item).\n\nReglas:\n- es_adulto_mayor = True -> prioridad = 0 (MAYOR PRIORIDAD)\n- es_adulto_mayor = False -> prioridad = 1 (NORMAL)\n- turno_global sirve como desempate\n- heapq.heappop() siempre extrae el elemento con menor valor de prioridad\n\nMétodos: encolar(), desencolar(), mostrar_cola(), tamanio(), esta_vacia()\n\nUso en app: Botón "AGREGAR A COLA DE ATENCION (PRIORIDAD)" en Citas y pantalla "Panel de Atención" para atender.')

# 6
pdf.add_page()
pdf.set_font('Helvetica', 'B', 14)
pdf.cell(0, 10, '6. Búsqueda Lineal (busqueda_lineal.py)', ln=True)
pdf.ln(1)
pdf.set_font('Helvetica', '', 10)
pdf.multi_cell(0, 5, 'Ubicación: core/busqueda_lineal.py\n\nConsiste en recorrer la lista elemento por elemento con un ciclo for, comparando hasta encontrar coincidencias.\n\nFunciones:\n- busqueda_lineal(lista, criterio, atributo): Genérica, usa getattr(), compara case-insensitive para strings\n- busqueda_lineal_por_email(usuarios, email): Búsqueda específica por email\n- busqueda_lineal_citas_por_medico(citas, medico_id): Filtra por médico\n- busqueda_lineal_medicamento_por_nombre(medicamentos, nombre): Filtra por nombre\n\nUso en app: Login usa busqueda_lineal_por_email() para validar credenciales. También se usa para obtener datos del usuario logueado.')

# 7
pdf.set_font('Helvetica', 'B', 14)
pdf.cell(0, 10, '7. Persistencia con Archivo JSON (archivo_datos.py)', ln=True)
pdf.ln(1)
pdf.set_font('Helvetica', '', 10)
pdf.multi_cell(0, 5, 'Ubicación: core/archivo_datos.py | Archivo: consola/salunic_datos.json (compartido)\n\nGuardar:\n- Usamos dataclasses.asdict() para convertir objetos DataClass a diccionarios\n- json.dump() con ensure_ascii=False, indent=4\n\nCargar:\n- json.load() lee el archivo\n- Limpiamos listas con clear()\n- Reconstruimos con Usuario(**u), CitaMedica(**c), etc.\n\nUso en app: Al registrar usuario y al agregar cita se guarda. Al iniciar app se intenta cargar datos.')

# 8
pdf.add_page()
pdf.set_font('Helvetica', 'B', 14)
pdf.cell(0, 10, '8. Integración en la App Tkinter', ln=True)
pdf.ln(1)
pdf.set_font('Helvetica', '', 10)
pdf.multi_cell(0, 5, 'Ubicación: app/\n\nPuntos clave de integración:\n\n- app/main.py: Al iniciar carga datos desde core.archivo_datos. Navegación entre pantallas (Splash, Login, Home, Citas, Atencion, etc.)\n- app/screens/login_screen.py: Usa core.busqueda_lineal + core.archivo_datos para login\n- app/screens/registro_screen.py: Crea core.entidades.Usuario, agrega a core.datos.usuarios, guarda con core.archivo_datos\n- app/screens/citas_screen.py: Muestra citas desde core.datos.citas, permite AGREGAR NUEVA CITA (guarda con DataClass), agrega a cola con prioridad\n- app/data/users_data.py: Adaptado para usar core como fuente principal, mantiene compatibilidad\n\nTodo con el mismo estilo visual (gradiente, colores, tarjetas redondeadas).')

# 9
pdf.set_font('Helvetica', 'B', 14)
pdf.cell(0, 10, '9. Panel de Atención (Integración visual de la Cola)', ln=True)
pdf.ln(1)
pdf.set_font('Helvetica', '', 10)
pdf.multi_cell(0, 5, 'Ubicación: app/screens/atencion_screen.py\n\nEsta pantalla hace visible lo que antes solo salía en consola.\n\nElementos:\n- EN ATENCIÓN: Muestra el paciente que se acaba de atender con su prioridad\n- COLA DE ESPERA: Lista ordenada por prioridad/turno (Adulto Mayor resaltado)\n- ATENDER SIGUIENTE: Llama a cola_atencion.desencolar()\n- ACTUALIZAR PANEL: Refresca la vista\n\nSe accede desde Home o directamente. Sigue el mismo formato visual del resto de la app.')

# 10
pdf.add_page()
pdf.set_font('Helvetica', 'B', 14)
pdf.cell(0, 10, '10. Flujo completo: Agregar a cola -> Ver -> Atender', ln=True)
pdf.ln(1)
pdf.set_font('Helvetica', '', 10)
pdf.multi_cell(0, 5, '1. Ir a Citas -> "AGREGAR A COLA DE ATENCION (PRIORIDAD)"\n2. Seleccionar si es Adulto Mayor (Sí/No). Esto define prioridad 0 o 1.\n3. Se llama a core.cola_atencion.encolar(item, es_adulto_mayor)\n4. Ir a Home -> "PANEL DE ATENCION CON PRIORIDAD" o pantalla Atencion\n5. Ver cola ordenada (Adulto Mayor primero)\n6. Presionar "ATENDER SIGUIENTE" -> desencolar() y pasa a "EN ATENCIÓN"\n7. En terminal también se ven los prints [COLA] confirmando el funcionamiento')

# 11
pdf.add_page()
pdf.set_font('Helvetica', 'B', 14)
pdf.cell(0, 10, '11. Tips para exponer y defender el código', ln=True)
pdf.ln(1)
pdf.set_font('Helvetica', '', 9)
tips = [
    "- Estructura: Di primero 'core/ es la lógica compartida, app y consola la reutilizan'",
    "- DataClass: Menciona que con @dataclass representamos entidades (Usuario, CitaMedica...)",
    "- Cola con prioridad: Explica tupla (prioridad, turno_global, item). Adulto Mayor = prioridad 0",
    "- Búsqueda lineal: Recorre elemento por elemento. Usado en login con busqueda_lineal_por_email",
    "- Archivo JSON: Guardar con asdict(), cargar reconstruyendo con Clase(**dict)",
    "- Integración: Muestra login/registro/citas usando core. No son módulos separados",
    "- Panel de Atención: Lo más visual. Agrega, ve la cola, atiende y demuestra prioridad",
    "- Unificación: Un solo salunic_datos.json para app y consola",
    "- Sé breve: Explica 'qué hace' y 'por qué' con el código abierto"
]
for t in tips:
    pdf.multi_cell(0, 5, t)
    pdf.ln(1)

# 12
pdf.ln(2)
pdf.set_font('Helvetica', 'B', 14)
pdf.cell(0, 10, '12. Checklist antes de exponer', ln=True)
pdf.ln(1)
pdf.set_font('Helvetica', '', 9)
check = [
    "[ ] Mostrar estructura de carpetas (core/, app/, consola/)",
    "[ ] Explicar core/ como lógica compartida",
    "[ ] Mostrar entidades.py con DataClass",
    "[ ] Explicar cola_atencion.py con heapq y prioridad al adulto mayor",
    "[ ] Mostrar busqueda_lineal.py usado en login",
    "[ ] Explicar archivo_datos.py (guardar/cargar JSON)",
    "[ ] Demo en app: Registrar/Login",
    "[ ] Demo en app: Agregar cita",
    "[ ] Demo en app: Agregar a cola (adulto mayor vs normal)",
    "[ ] Demo en app: Panel de Atención -> Atender siguiente",
    "[ ] Mostrar que imprime en terminal [COLA]",
    "[ ] Mencionar reutilización entre app y consola"
]
for c in check:
    pdf.cell(0, 5, c, ln=True)

# 13
pdf.add_page()
pdf.set_font('Helvetica', 'B', 14)
pdf.cell(0, 10, '13. Conclusión', ln=True)
pdf.ln(1)
pdf.set_font('Helvetica', '', 11)
pdf.multi_cell(0, 6, 'El proyecto SALUNIC ahora está integrado correctamente. La lógica solicitada (DataClass, Cola con Prioridad, Búsqueda Lineal, Archivo de Datos) se encuentra centralizada en core/ y es utilizada tanto por el módulo por consola como por la aplicación gráfica Tkinter.\n\nEl Panel de Atención permite visualizar y aplicar la cola con prioridad de forma práctica. Con esta estructura unificada, el código es más limpio, profesional, fácil de entender y está listo para exponer y defender con seguridad.')

output = Path('C:/salunic-app/docs/pdfs/GUIA_COMPLETA_INTEGRACION_APP_CONSOLA_CORE_TIPS_DEFENSA.pdf')
pdf.output(str(output))
print('ok')
print(output)
