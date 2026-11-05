import json
import os
from dataclasses import asdict

from Entidades import Usuario, CitaMedica, Medicamento, AlmacenMedicamento

# Listas propias de cada entidad (se guardan en memoria mientras corre el programa)
usuarios = []
citas = []
medicamentos = []
almacen = []


# Datos iniciales para pruebas
usuarios_iniciales = [
    Usuario(id=1, nombre="Ana Lopez", email="ana.lopez@salunic.com", password="123456", telefono="+505 88888888"),
    Usuario(id=2, nombre="Carlos Ruiz", email="carlos.ruiz@salunic.com", password="123456", telefono="+505 77777777"),
    Usuario(id=3, nombre="Maria Gonzalez", email="maria.gonzalez@salunic.com", password="123456", telefono="+505 66666666"),
]

citas_iniciales = [
    CitaMedica(id=101, paciente_id=1, medico_id=201, especialidad="Medicina General", fecha="30/10/2025", hora="09:00", lugar="Consultorio 1"),
    CitaMedica(id=102, paciente_id=2, medico_id=202, especialidad="Pediatria", fecha="30/10/2025", hora="10:30", lugar="Consultorio 2"),
    CitaMedica(id=103, paciente_id=3, medico_id=201, especialidad="Medicina General", fecha="31/10/2025", hora="14:00", lugar="Consultorio 1"),
]

medicamentos_iniciales = [
    Medicamento(id=301, nombre="Paracetamol", dosis="500mg", frecuencia="Cada 8 horas", presentacion="Tabletas"),
    Medicamento(id=302, nombre="Amoxicilina", dosis="500mg", frecuencia="Cada 12 horas", presentacion="Capsulas"),
    Medicamento(id=303, nombre="Ibuprofeno", dosis="400mg", frecuencia="Cada 8 horas", presentacion="Tabletas"),
]

inventario_inicial = [
    AlmacenMedicamento(id=401, medicamento_id=301, cantidad=150, fecha_vencimiento="12/2026"),
    AlmacenMedicamento(id=402, medicamento_id=302, cantidad=80, fecha_vencimiento="08/2026"),
    AlmacenMedicamento(id=403, medicamento_id=303, cantidad=200, fecha_vencimiento="10/2026"),
]

# Ruta absoluta al archivo de datos (en la raíz del proyecto) para consistencia
ARCHIVO_DATOS = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "salunic_datos.json")


def cargar_datos_iniciales():
    """Carga datos de ejemplo si las listas estan vacias."""
    if not usuarios:
        usuarios.extend(usuarios_iniciales)
    if not citas:
        citas.extend(citas_iniciales)
    if not medicamentos:
        medicamentos.extend(medicamentos_iniciales)
    if not almacen:
        almacen.extend(inventario_inicial)


def guardar_datos():
    """Guarda todas las listas (DataClass) en un archivo JSON"""
    try:
        data = {
            "usuarios": [asdict(u) for u in usuarios],
            "citas": [asdict(c) for c in citas],
            "medicamentos": [asdict(m) for m in medicamentos],
            "almacen": [asdict(a) for a in almacen]
        }
        with open(ARCHIVO_DATOS, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        print(f"\n[OK] Datos guardados correctamente en: {ARCHIVO_DATOS}")
    except Exception as e:
        print(f"\n[ERROR] No se pudieron guardar los datos: {e}")


def cargar_datos():
    """Carga datos desde archivo JSON hacia las listas de DataClass"""
    if not os.path.exists(ARCHIVO_DATOS):
        print("\n[INFO] No existe archivo de datos. Se trabajara con datos en memoria.")
        return
    try:
        with open(ARCHIVO_DATOS, "r", encoding="utf-8-sig") as f:
            data = json.load(f)
        usuarios.clear()
        citas.clear()
        medicamentos.clear()
        almacen.clear()
        for u in data.get("usuarios", []):
            usuarios.append(Usuario(**u))
        for c in data.get("citas", []):
            citas.append(CitaMedica(**c))
        for m in data.get("medicamentos", []):
            medicamentos.append(Medicamento(**m))
        for a in data.get("almacen", []):
            almacen.append(AlmacenMedicamento(**a))
        print(f"\n[OK] Datos cargados desde: {ARCHIVO_DATOS}")
        print(f"     Usuarios: {len(usuarios)} | Citas: {len(citas)} | Medicamentos: {len(medicamentos)} | Almacen: {len(almacen)}")
    except Exception as e:
        print(f"\n[ERROR] No se pudieron cargar los datos: {e}")
