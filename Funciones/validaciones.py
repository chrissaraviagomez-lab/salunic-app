import re
from datetime import datetime


def validar_nombre(texto):
    if not texto.strip():
        raise ValueError("El nombre no puede estar vacio.")
    if not re.match(r"^[A-Za-záéíóúÁÉÍÓÚñÑ' ]+$", texto):
        raise ValueError("El nombre solo puede contener letras y espacios.")
    return texto.strip().title()


def validar_email(email):
    if not email.strip():
        raise ValueError("El email no puede estar vacio.")
    if not re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", email):
        raise ValueError("El email no tiene un formato valido (ej: usuario@correo.com).")
    return email.strip().lower()


def validar_password(password):
    if len(password) < 4:
        raise ValueError("La contrasena debe tener al menos 4 caracteres.")
    return password


def validar_fecha(fecha):
    try:
        datetime.strptime(fecha, "%d/%m/%Y")
    except ValueError:
        raise ValueError("La fecha debe tener formato DD/MM/AAAA con una fecha real.")
    return fecha


def validar_hora(hora):
    try:
        datetime.strptime(hora, "%H:%M")
    except ValueError:
        raise ValueError("La hora debe tener formato HH:MM (ej: 08:00, 20:00).")
    return hora


def validar_dosis(dosis):
    if not dosis.strip():
        raise ValueError("La dosis no puede estar vacia.")
    return dosis.strip()


def validar_celular(texto):
    if not texto.strip():
        raise ValueError("El telefono no puede estar vacio.")
    if not re.match(r"^\+?[\d\- ]{8,15}$", texto):
        raise ValueError("El telefono debe tener solo digitos (ej: +505 86459285).")
    return texto.strip()


def validar_cantidad(cantidad):
    if not cantidad.strip():
        raise ValueError("La cantidad no puede estar vacia.")
    if not cantidad.isdigit():
        raise ValueError("La cantidad debe ser un numero entero positivo.")
    return int(cantidad)


def validar_descripcion(texto):
    if not texto.strip():
        raise ValueError("El dato no puede estar vacio.")
    return texto.strip().capitalize()


def pedir_campo(etiqueta, validador):
    while True:
        try:
            valor = input(etiqueta)
            return validador(valor)
        except ValueError as e:
            print(f"  [Error] {e}")
