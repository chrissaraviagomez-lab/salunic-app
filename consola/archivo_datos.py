"""Compatibilidad: persistencia JSON desde la estructura requerida (Datos/)."""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from Datos.datos import guardar_datos, cargar_datos, ARCHIVO_DATOS

__all__ = ["guardar_datos", "cargar_datos", "ARCHIVO_DATOS"]
