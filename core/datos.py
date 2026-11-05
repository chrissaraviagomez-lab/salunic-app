"""Compatibilidad: listas y datos desde la estructura requerida (Datos/).
Comparte las MISMAS listas en memoria para evitar estados divididos.
"""
from Datos.datos import (
    usuarios, citas, medicamentos, almacen,
    usuarios_iniciales, citas_iniciales, inventario_inicial, medicamentos_iniciales,
    cargar_datos_iniciales, cargar_datos, guardar_datos, ARCHIVO_DATOS,
)

__all__ = [
    "usuarios", "citas", "medicamentos", "almacen",
    "usuarios_iniciales", "citas_iniciales", "inventario_inicial", "medicamentos_iniciales",
    "cargar_datos_iniciales", "cargar_datos", "guardar_datos", "ARCHIVO_DATOS",
]
