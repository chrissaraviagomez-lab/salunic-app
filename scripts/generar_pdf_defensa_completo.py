"""Generador legado: delega al PDF de estudio final (estructura requerida).
Mantener este archivo evita confusión con versiones antiguas basadas en core/.
"""
from pathlib import Path
import runpy

runpy.run_path(str(Path(__file__).with_name("generar_pdf_estudio_final.py")), run_name="__main__")
