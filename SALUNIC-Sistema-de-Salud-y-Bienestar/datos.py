from entidades import Medicamento, AlmacenMedicamento

# Listas propias de cada entidad (se guardan en memoria mientras corre el programa)
usuarios = []
citas = []
medicamentos = []
almacen = []

# =========================================================
# INVENTARIO PRE-CARGADO - Medicamentos reales del MINSA
# Hospitales: Fernando Velez Paiz, Hospital Bautista
# Fuente: Lista Basica de Medicamentos Esenciales MINSA
# =========================================================
inventario_inicial = [
    AlmacenMedicamento(id=1, medicamento_id=1, cantidad=500, fecha_vencimiento="15/12/2026"),
    AlmacenMedicamento(id=2, medicamento_id=2, cantidad=350, fecha_vencimiento="20/11/2026"),
    AlmacenMedicamento(id=3, medicamento_id=3, cantidad=200, fecha_vencimiento="01/06/2027"),
    AlmacenMedicamento(id=4, medicamento_id=4, cantidad=150, fecha_vencimiento="10/09/2026"),
    AlmacenMedicamento(id=5, medicamento_id=5, cantidad=400, fecha_vencimiento="05/03/2027"),
    AlmacenMedicamento(id=6, medicamento_id=6, cantidad=300, fecha_vencimiento="22/08/2026"),
    AlmacenMedicamento(id=7, medicamento_id=7, cantidad=250, fecha_vencimiento="30/07/2027"),
    AlmacenMedicamento(id=8, medicamento_id=8, cantidad=180, fecha_vencimiento="14/04/2026"),
    AlmacenMedicamento(id=9, medicamento_id=9, cantidad=420, fecha_vencimiento="19/10/2026"),
    AlmacenMedicamento(id=10, medicamento_id=10, cantidad=100, fecha_vencimiento="28/02/2027"),
    AlmacenMedicamento(id=11, medicamento_id=11, cantidad=90, fecha_vencimiento="03/01/2027"),
    AlmacenMedicamento(id=12, medicamento_id=12, cantidad=120, fecha_vencimiento="17/05/2026"),
]

medicamentos_iniciales = [
    Medicamento(id=1, nombre="Paracetamol", dosis="500mg", frecuencia="Cada 8 horas", presentacion="Tabletas"),
    Medicamento(id=2, nombre="Ibuprofeno", dosis="400mg", frecuencia="Cada 8 horas", presentacion="Tabletas"),
    Medicamento(id=3, nombre="Amoxicilina", dosis="500mg", frecuencia="Cada 8 horas", presentacion="Capsulas"),
    Medicamento(id=4, nombre="Omeprazol", dosis="20mg", frecuencia="1 vez al dia", presentacion="Capsulas"),
    Medicamento(id=5, nombre="Metformina", dosis="850mg", frecuencia="2 veces al dia", presentacion="Tabletas"),
    Medicamento(id=6, nombre="Losartan", dosis="50mg", frecuencia="1 vez al dia", presentacion="Tabletas"),
    Medicamento(id=7, nombre="Ciprofloxacina", dosis="500mg", frecuencia="Cada 12 horas", presentacion="Tabletas"),
    Medicamento(id=8, nombre="Ampicilina", dosis="500mg", frecuencia="Cada 6 horas", presentacion="Capsulas"),
    Medicamento(id=9, nombre="Trimetoprim + Sulfametoxazol", dosis="160/800mg", frecuencia="Cada 12 horas", presentacion="Tabletas"),
    Medicamento(id=10, nombre="Aciclovir", dosis="400mg", frecuencia="Cada 8 horas", presentacion="Tabletas"),
    Medicamento(id=11, nombre="Fluconazol", dosis="150mg", frecuencia="1 vez a la semana", presentacion="Tabletas"),
    Medicamento(id=12, nombre="Nitrofurantoina", dosis="100mg", frecuencia="Cada 6 horas", presentacion="Tabletas"),
]