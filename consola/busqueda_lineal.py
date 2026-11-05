"""Compatibilidad: re-exporta busqueda lineal desde Funciones/."""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from Funciones.busqueda_lineal import (
    busqueda_lineal,
    busqueda_lineal_por_email,
    busqueda_lineal_citas_por_medico,
    busqueda_lineal_medicamento_por_nombre,
)

__all__ = [
    "busqueda_lineal",
    "busqueda_lineal_por_email",
    "busqueda_lineal_citas_por_medico",
    "busqueda_lineal_medicamento_por_nombre",
]
