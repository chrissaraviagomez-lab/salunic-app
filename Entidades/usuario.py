from dataclasses import dataclass


@dataclass
class Usuario:
    id: int
    nombre: str
    email: str
    password: str
    telefono: str = "+505 00000000"
