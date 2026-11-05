"""Compatibilidad: re-exporta la cola con prioridad desde Funciones/."""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from Funciones.cola_atencion import ColaAtencion, cola_atencion

__all__ = ["ColaAtencion", "cola_atencion"]
