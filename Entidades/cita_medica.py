from dataclasses import dataclass


@dataclass
class CitaMedica:
    id: int
    paciente_id: int
    medico_id: int
    especialidad: str
    fecha: str        # formato DD/MM/AAAA
    hora: str         # formato HH:MM
    lugar: str = "Hospital"
