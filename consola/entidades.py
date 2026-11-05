"""Compatibilidad: re-exporta las DataClass desde la estructura requerida (Entidades/)."""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from Entidades import Usuario, CitaMedica, Medicamento, AlmacenMedicamento

__all__ = ["Usuario", "CitaMedica", "Medicamento", "AlmacenMedicamento"]
