from dataclasses import dataclass


@dataclass
class Usuario:
    id: int
    nombre: str
    email: str
    password: str
    telefono: str = "+505 00000000"


@dataclass
class CitaMedica:
    id: int
    paciente_id: int
    medico_id: int
    especialidad: str
    fecha: str        # formato DD/MM/AAAA
    hora: str         # formato HH:MM
    lugar: str = "Hospital"


@dataclass
class Medicamento:
    id: int
    nombre: str
    dosis: str
    frecuencia: str
    presentacion: str = "Tabletas"


@dataclass
class AlmacenMedicamento:
    id: int
    medicamento_id: int
    cantidad: int
    fecha_vencimiento: str  # formato DD/MM/AAAA