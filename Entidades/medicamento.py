from dataclasses import dataclass


@dataclass
class Medicamento:
    id: int
    nombre: str
    dosis: str
    frecuencia: str
    presentacion: str = "Tabletas"
