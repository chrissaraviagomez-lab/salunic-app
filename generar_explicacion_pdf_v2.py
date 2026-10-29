from fpdf import FPDF
from datetime import datetime

class PDF(FPDF):
    def header(self):
        self.set_font('Helvetica', 'B', 12)
        self.cell(0, 10, 'SALUNIC - Explicacion para Estudio', border=0, ln=True, align='C')
        self.ln(2)

    def footer(self):
        self.set_y(-15)
        self.set_font('Helvetica', 'I', 8)
        self.cell(0, 10, f'Pagina {self.page_no()}', align='C')

def add_title(pdf, text):
    pdf.set_font('Helvetica', 'B', 14)
    pdf.set_fill_color(21, 101, 192)
    pdf.set_text_color(255, 255, 255)
    pdf.cell(0, 9, text, border=0, ln=True, fill=True)
    pdf.set_text_color(0, 0, 0)
    pdf.ln(3)

def add_subtitle(pdf, text):
    pdf.set_font('Helvetica', 'B', 11)
    pdf.cell(0, 7, text, border=0, ln=True)
    pdf.ln(1)

def add_text(pdf, text):
    pdf.set_font('Helvetica', '', 9)
    pdf.multi_cell(0, 5, text)
    pdf.ln(2)

def add_code(pdf, text):
    pdf.set_font('Courier', '', 8)
    pdf.set_fill_color(245, 245, 245)
    pdf.multi_cell(0, 4, text.replace('├','-').replace('└','-').replace('│','|'), border=0, fill=True)
    pdf.ln(3)

pdf = PDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()

pdf.set_font('Helvetica', 'B', 18)
pdf.ln(40)
pdf.cell(0, 10, 'SALUNIC - Sistema de Salud y Bienestar', ln=True, align='C')
pdf.set_font('Helvetica', '', 12)
pdf.ln(5)
pdf.cell(0, 10, 'Modulo por Consola - DataClass, Cola con Prioridad, Busqueda Lineal y Archivo de Datos', ln=True, align='C')
pdf.ln(10)
pdf.set_font('Helvetica', '', 10)
pdf.cell(0, 10, f'Fecha: {datetime.now().strftime("%d/%m/%Y")} - Actualizado', ln=True, align='C')
pdf.add_page()

add_title(pdf, '1. Estructura del Modulo')
add_text(pdf, 'Carpeta: SALUNIC-Sistema-de-Salud-y-Bienestar/')
add_code(pdf, '''- entidades.py        # Lista de DataClass
- datos.py            # Listas donde se guardan los objetos
- funciones.py        # Validaciones, CRUD y logica
- busqueda_lineal.py  # Implementacion de busqueda lineal
- cola_atencion.py    # Implementacion de Cola CON PRIORIDAD (heapq)
- archivo_datos.py    # Guardar/Cargar datos en archivo JSON
- main.py             # Menus y punto de entrada
- salunic_datos.json  # Archivo generado al guardar''')

add_title(pdf, '2. Lista de DataClass (entidades.py)')
add_text(pdf, 'Usamos @dataclass para definir las entidades: Usuario, CitaMedica, Medicamento, AlmacenMedicamento.')
add_code(pdf, '''from dataclasses import dataclass

@dataclass
class Usuario:
    id: int
    nombre: str
    email: str
    password: str
    telefono: str = "+505 00000000"''')

add_title(pdf, '3. Busqueda Lineal (busqueda_lineal.py)')
add_text(pdf, 'Recorre la lista elemento por elemento con un bucle for comparando hasta encontrar coincidencia.')
add_code(pdf, '''def busqueda_lineal_por_email(usuarios, email):
    for u in usuarios:
        if u.email.lower() == email.lower():
            return u
    return None''')
add_text(pdf, 'Se usa en Menu 1 > 2 (Buscar usuario por email).')

add_title(pdf, '4. Cola con Prioridad para Adulto Mayor (cola_atencion.py)')
add_text(pdf, 'Ahora NO es FIFO puro. Usamos heapq. Adulto Mayor tiene prioridad=0 (se atiende primero), Normal prioridad=1.')
add_subtitle(pdf, 'Logica clave')
add_code(pdf, '''import heapq

# prioridad 0 = ADULTO MAYOR (PRIORITARIO), 1 = NORMAL
if es_adulto_mayor:
    prioridad = 0
    tipo = "ADULTO MAYOR (PRIORITARIO)"
else:
    prioridad = 1
    tipo = "NORMAL"

heapq.heappush(self.cola, (prioridad, self.turno_global, item))
prioridad, turno, atendido = heapq.heappop(self.cola)''')
add_text(pdf, 'Aunque llegue despues, si es adulto mayor (prioridad 0) siempre sale primero con heappop().')

add_title(pdf, '5. Archivo de Datos (archivo_datos.py)')
add_text(pdf, 'Guardamos con json.dump usando asdict() y cargamos recreando objetos DataClass con Usuario(**u).')
add_code(pdf, '''data = {
    "usuarios": [asdict(u) for u in usuarios],
    "citas": [asdict(c) for c in citas],
    "medicamentos": [asdict(m) for m in medicamentos],
    "almacen": [asdict(a) for a in almacen]
}
json.dump(data, f, ensure_ascii=False, indent=4)''')

add_title(pdf, '6. Como Probar')
add_code(pdf, '''cd "C:\\salunic-app\\SALUNIC-Sistema-de-Salud-y-Bienestar"
py main.py''')
add_text(pdf, '1. DataClass -> entidades.py\n2. Busqueda Lineal -> Menu 1 > 2 (buscar por email)\n3. Cola con Prioridad -> Menu 5: Agregar pacientes (marcar adulto mayor/no). Al mostrar/ver atender, el adulto mayor va primero aunque llegue despues.\n4. Archivo de Datos -> Menu 6 (guardar/cargar) crea salunic_datos.json')

add_title(pdf, '7. Frase para Explicar al Profesor')
add_text(pdf, '"El sistema usa DataClass para definir entidades, listas para almacenarlas, busqueda lineal para recorrer elemento por elemento, una cola con prioridad usando heapq para dar atencion preferencial al adulto mayor (prioridad 0) sin importar el orden de llegada, y persistencia JSON para guardar/cargar los datos."')

pdf.output(r'C:\salunic-app\EXPLICACION_SALUNIC_DataClass_ColaCONPrioridad_BusquedaLineal_ArchivoDatos.pdf')
print('PDF_V2_CREADO')
