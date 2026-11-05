from dataclasses import dataclass


@dataclass
class AlmacenMedicamento:
    id: int
    medicamento_id: int
    cantidad: int
    fecha_vencimiento: str  # formato DD/MM/AAAA
