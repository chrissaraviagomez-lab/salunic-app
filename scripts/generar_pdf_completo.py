from fpdf import FPDF
from pathlib import Path

class PDF(FPDF):
    def header(self):
        self.set_font('Helvetica', 'B', 10)
        self.cell(0, 8, 'SALUNIC - Módulo por Consola: DataClass, Cola con Prioridad, Búsqueda Lineal y Archivo de Datos', align='C', ln=True)
        self.ln(2)

    def footer(self):
        self.set_y(-15)
        self.set_font('Helvetica', 'I', 8)
        self.cell(0, 10, f'Página {self.page_no()}', align='C')

pdf = PDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()

# Portada
pdf.set_font('Helvetica', 'B', 18)
pdf.ln(20)
pdf.cell(0, 10, 'SALUNIC - Sistema de Salud y Bienestar', align='C', ln=True)
pdf.set_font('Helvetica', 'B', 14)
pdf.cell(0, 10, 'Módulo por Consola', align='C', ln=True)
pdf.ln(5)
pdf.set_font('Helvetica', '', 12)
pdf.cell(0, 10, 'DataClass | Cola con Prioridad | Búsqueda Lineal | Archivo de Datos', align='C', ln=True)
pdf.ln(30)
pdf.cell(0, 10, 'Guía para Estudio', align='C', ln=True)

# Índice
pdf.add_page()
pdf.set_font('Helvetica', 'B', 16)
pdf.cell(0, 10, 'ÍNDICE', ln=True)
pdf.ln(2)
pdf.set_font('Helvetica', '', 11)
items = [
    "1. Objetivo",
    "2. Estructura del Módulo por Consola",
    "3. DataClass (entidades.py)",
    "4. Cola con Prioridad (cola_atencion.py)",
    "5. Búsqueda Lineal (busqueda_lineal.py)",
    "6. Archivo de Datos JSON (archivo_datos.py)",
    "7. Integración con main.py",
    "8. Pruebas y Ejemplos",
    "9. Conclusión",
]
for i, it in enumerate(items):
    pdf.cell(0, 8, it, ln=True)
pdf.ln(5)

# 1. Objetivo
pdf.add_page()
pdf.set_font('Helvetica', 'B', 14)
pdf.cell(0, 10, '1. Objetivo', ln=True)
pdf.ln(1)
pdf.set_font('Helvetica', '', 11)
pdf.multi_cell(0, 6, 'El objetivo de este módulo es aplicar los conceptos de Programación Estructurada: clases con DataClass, estructuras de datos (cola con prioridad), algoritmos de búsqueda (búsqueda lineal) y persistencia de datos (archivos JSON).')

# 2. Estructura
pdf.ln(4)
pdf.set_font('Helvetica', 'B', 14)
pdf.cell(0, 10, '2. Estructura del Módulo por Consola', ln=True)
pdf.ln(1)
pdf.set_font('Helvetica', '', 11)
pdf.multi_cell(0, 6, 'Ubicación: consola/\n\nArchivos principales:\n- entidades.py: Definición de las clases con @dataclass\n- datos.py: Datos iniciales en memoria\n- funciones.py: Funciones CRUD y lógica del sistema\n- cola_atencion.py: Cola con prioridad usando heapq\n- busqueda_lineal.py: Implementación de búsqueda lineal\n- archivo_datos.py: Guardar/cargar datos en JSON\n- main.py: Menú principal e integración')
pdf.ln(2)

# 3. DataClass
pdf.add_page()
pdf.set_font('Helvetica', 'B', 14)
pdf.cell(0, 10, '3. DataClass (entidades.py)', ln=True)
pdf.ln(1)
pdf.set_font('Helvetica', '', 11)
pdf.multi_cell(0, 6, 'Los dataclasses permiten crear clases para representar entidades con menos código. Se importan con: from dataclasses import dataclass\n\nEntidades definidas:')
pdf.ln(2)
pdf.set_font('Helvetica', 'B', 11)
pdf.cell(0, 8, 'Usuario', ln=True)
pdf.set_font('Helvetica', '', 10)
pdf.multi_cell(0, 5, '- id: int\n- nombre: str\n- email: str\n- password: str\n- telefono: str = "+505 00000000"')
pdf.ln(1)
pdf.set_font('Helvetica', 'B', 11)
pdf.cell(0, 8, 'CitaMedica', ln=True)
pdf.set_font('Helvetica', '', 10)
pdf.multi_cell(0, 5, '- id: int\n- paciente_id: int\n- medico_id: int\n- especialidad: str\n- fecha: str (DD/MM/AAAA)\n- hora: str (HH:MM)\n- lugar: str = "Hospital"')
pdf.ln(1)
pdf.set_font('Helvetica', 'B', 11)
pdf.cell(0, 8, 'Medicamento', ln=True)
pdf.set_font('Helvetica', '', 10)
pdf.multi_cell(0, 5, '- id: int\n- nombre: str\n- dosis: str\n- frecuencia: str\n- presentacion: str = "Tabletas"')
pdf.ln(1)
pdf.set_font('Helvetica', 'B', 11)
pdf.cell(0, 8, 'AlmacenMedicamento', ln=True)
pdf.set_font('Helvetica', '', 10)
pdf.multi_cell(0, 5, '- id: int\n- medicamento_id: int\n- cantidad: int\n- fecha_vencimiento: str (DD/MM/AAAA)')

# 4. Cola con prioridad
pdf.add_page()
pdf.set_font('Helvetica', 'B', 14)
pdf.cell(0, 10, '4. Cola con Prioridad (cola_atencion.py)', ln=True)
pdf.ln(1)
pdf.set_font('Helvetica', '', 11)
pdf.multi_cell(0, 6, 'Se utiliza heapq para implementar una cola con prioridad. El objetivo es atender primero a Adultos Mayores, sin importar el orden de llegada.\n\nEstrategia:')
pdf.ln(2)
pdf.set_font('Helvetica', '', 10)
pdf.multi_cell(0, 5, '- Se usa una tupla (prioridad, turno_global, item) para ordenar\n- Prioridad 0 = Adulto Mayor (máxima prioridad)\n- Prioridad 1 = Paciente Normal\n- turno_global actúa como desempate para mantener un orden estable\n- heapq.heappush() agrega y heapq.heappop() extrae el elemento con menor prioridad numérica (prioritario)')
pdf.ln(3)
pdf.set_font('Helvetica', 'B', 11)
pdf.cell(0, 8, 'Métodos principales:', ln=True)
pdf.set_font('Helvetica', '', 10)
pdf.multi_cell(0, 5, '- encolar(item, es_adulto_mayor=False): Agrega paciente con su prioridad\n- desencolar(): Atiende y remueve el paciente con mayor prioridad\n- mostrar_cola(): Muestra la cola ordenada por prioridad y turno\n- tamanio(): Retorna cantidad de pacientes en espera\n- esta_vacia(): Verifica si hay pacientes en espera')

# 5. Búsqueda lineal
pdf.add_page()
pdf.set_font('Helvetica', 'B', 14)
pdf.cell(0, 10, '5. Búsqueda Lineal (busqueda_lineal.py)', ln=True)
pdf.ln(1)
pdf.set_font('Helvetica', '', 11)
pdf.multi_cell(0, 6, 'La búsqueda lineal recorre la lista elemento por elemento, comparando uno a uno hasta encontrar coincidencias.\n\nFunción general:')
pdf.ln(2)
pdf.set_font('Helvetica', '', 10)
pdf.multi_cell(0, 5, 'busqueda_lineal(lista, criterio, atributo) - Recorre con un ciclo for, usa getattr() para obtener el atributo, compara por igualdad (case-insensitive para strings), retorna lista de resultados.')
pdf.ln(3)
pdf.set_font('Helvetica', 'B', 11)
pdf.cell(0, 8, 'Funciones específicas:', ln=True)
pdf.set_font('Helvetica', '', 10)
pdf.multi_cell(0, 5, '- busqueda_lineal_por_email(usuarios, email): Busca un usuario exacto por email\n- busqueda_lineal_citas_por_medico(citas, medico_id): Filtra citas por ID de médico\n- busqueda_lineal_medicamento_por_nombre(medicamentos, nombre): Filtra medicamentos por nombre')

# 6. Archivo de datos
pdf.add_page()
pdf.set_font('Helvetica', 'B', 14)
pdf.cell(0, 10, '6. Archivo de Datos JSON (archivo_datos.py)', ln=True)
pdf.ln(1)
pdf.set_font('Helvetica', '', 11)
pdf.multi_cell(0, 6, 'Se utiliza JSON para guardar y cargar la información. Los objetos DataClass se convierten a diccionarios con dataclasses.asdict() y se reconstruyen con Clase(**dict).\n\nArchivo: consola/salunic_datos.json')
pdf.ln(2)
pdf.set_font('Helvetica', 'B', 11)
pdf.cell(0, 8, 'guardar_datos():', ln=True)
pdf.set_font('Helvetica', '', 10)
pdf.multi_cell(0, 5, '1. Construye un diccionario con las 4 listas (usuarios, citas, medicamentos, almacen)\n2. Convierte cada objeto a dict con asdict()\n3. Guarda con json.dump() con ensure_ascii=False e indent=4')
pdf.ln(2)
pdf.set_font('Helvetica', 'B', 11)
pdf.cell(0, 8, 'cargar_datos():', ln=True)
pdf.set_font('Helvetica', '', 10)
pdf.multi_cell(0, 5, '1. Verifica si existe el archivo\n2. Lee con json.load()\n3. Limpia las listas actuales con clear()\n4. Reconstruye objetos DataClass con Usuario(**u), etc.')

# 7. Integración
pdf.add_page()
pdf.set_font('Helvetica', 'B', 14)
pdf.cell(0, 10, '7. Integración con main.py', ln=True)
pdf.ln(1)
pdf.set_font('Helvetica', '', 11)
pdf.multi_cell(0, 6, 'El menú del módulo por consola integra todos los componentes:\n\n- Al iniciar, llama a cargar_datos() para recuperar información guardada\n- Permite gestionar usuarios, citas, medicamentos\n- Tiene opción "Cola de Atención con Prioridad" para encolar/desencolar pacientes\n- Tiene opción "Búsqueda Lineal" para buscar por diferentes criterios\n- Permite guardar con guardar_datos() antes de salir')
pdf.ln(4)

# 8. Ejemplos
pdf.set_font('Helvetica', 'B', 14)
pdf.cell(0, 10, '8. Pruebas y Ejemplos', ln=True)
pdf.ln(1)
pdf.set_font('Helvetica', 'B', 11)
pdf.cell(0, 8, 'Ejemplo: Cola con Prioridad', ln=True)
pdf.set_font('Helvetica', '', 10)
pdf.multi_cell(0, 5, 'Si se encolan: Paciente Normal (llega primero) y luego Adulto Mayor, el Adulto Mayor será atendido PRIMERO porque tiene prioridad 0.')
pdf.ln(2)
pdf.set_font('Helvetica', 'B', 11)
pdf.cell(0, 8, 'Ejemplo: Búsqueda Lineal', ln=True)
pdf.set_font('Helvetica', '', 10)
pdf.multi_cell(0, 5, 'Al buscar por email "ana@salunic.com", se recorre la lista elemento por elemento comparando u.email hasta encontrar la coincidencia.')
pdf.ln(2)
pdf.set_font('Helvetica', 'B', 11)
pdf.cell(0, 8, 'Ejemplo: Persistencia JSON', ln=True)
pdf.set_font('Helvetica', '', 10)
pdf.multi_cell(0, 5, 'Al guardar, se convierte todo a JSON. Al cargar, se reconstruyen los objetos DataClass manteniendo sus atributos.')

# 9. Conclusión
pdf.add_page()
pdf.set_font('Helvetica', 'B', 14)
pdf.cell(0, 10, '9. Conclusión', ln=True)
pdf.ln(1)
pdf.set_font('Helvetica', '', 11)
pdf.multi_cell(0, 6, 'El módulo por consola cumple con todos los requisitos solicitados:\n\n- DataClass: Implementado en entidades.py con 4 clases\n- Cola con Prioridad: Implementado con heapq, dando prioridad al Adulto Mayor\n- Búsqueda Lineal: Implementado recorriendo elemento por elemento\n- Archivo de Datos: Implementado con JSON (guardar/cargar)\n\nTodo esto se integra correctamente en main.py y funciona tanto de forma aislada como junto al resto del sistema SALUNIC.')

output = Path('C:/salunic-app/docs/pdfs/EXPLICACION_SALUNIC_COMPLETA_DataClass_ColaPrioridad_BusquedaLineal_ArchivoJSON.pdf')
pdf.output(str(output))
print('ok')
print(output)
