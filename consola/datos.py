"""Compatibilidad: usa las listas y utilidades desde la estructura requerida (Datos/)."""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from Datos.datos import (
    usuarios, citas, medicamentos, almacen,
    usuarios_iniciales, citas_iniciales, inventario_inicial, medicamentos_iniciales,
    cargar_datos_iniciales, cargar_datos, guardar_datos,
)
from Entidades import Usuario, CitaMedica, Medicamento, AlmacenMedicamento

__all__ = [
    "usuarios", "citas", "medicamentos", "almacen",
    "usuarios_iniciales", "citas_iniciales", "inventario_inicial", "medicamentos_iniciales",
    "cargar_datos_iniciales", "cargar_datos", "guardar_datos",
    "Usuario", "CitaMedica", "Medicamento", "AlmacenMedicamento",
]
