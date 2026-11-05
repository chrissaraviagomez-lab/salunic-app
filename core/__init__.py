"""Capa de compatibilidad.
La estructura principal requerida por el profesor es: Entidades/, Datos/, Funciones/.
Este paquete se mantiene por compatibilidad y delega a esa estructura.
"""
from Entidades import Usuario, CitaMedica, Medicamento, AlmacenMedicamento

__all__ = ["Usuario", "CitaMedica", "Medicamento", "AlmacenMedicamento"]
