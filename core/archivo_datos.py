"""Compatibilidad: persistencia JSON delegada a Datos/ (archivo compartido)."""
from Datos.datos import guardar_datos, cargar_datos, ARCHIVO_DATOS

__all__ = ["guardar_datos", "cargar_datos", "ARCHIVO_DATOS"]
