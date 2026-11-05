import json
import os
from dataclasses import asdict

from .entidades import Usuario, CitaMedica, Medicamento, AlmacenMedicamento
from .datos import usuarios, citas, medicamentos, almacen


# Ruta absoluta al archivo de datos (en la raíz del proyecto) para consistencia
import os as _os
ARCHIVO_DATOS = _os.path.join(_os.path.dirname(_os.path.dirname(_os.path.abspath(__file__))), "salunic_datos.json")


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
        with open(ARCHIVO_DATOS, "r", encoding="utf-8") as f:
            data = json.load(f)

        # Limpiar listas actuales
        usuarios.clear()
        citas.clear()
        medicamentos.clear()
        almacen.clear()

        # Recrear objetos DataClass
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
