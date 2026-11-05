from Entidades import CitaMedica
from Datos import citas
from .validaciones import validar_nombre, validar_fecha, validar_hora, pedir_campo


def _validar_int(x):
    if x.strip().isdigit():
        return int(x)
    raise ValueError("Debe ser un numero entero.")


def registrar_cita():
    print("\n--- Registrar Cita Medica ---")
    paciente_id = pedir_campo("ID del paciente: ", _validar_int)
    medico_id = pedir_campo("ID del medico: ", _validar_int)
    especialidad = pedir_campo("Especialidad: ", validar_nombre)
    fecha = pedir_campo("Fecha (DD/MM/AAAA): ", validar_fecha)
    hora = pedir_campo("Hora (HH:MM): ", validar_hora)
    lugar = pedir_campo("Lugar/Hospital: ", validar_nombre)
    nuevo_id = max([c.id for c in citas], default=0) + 1
    c = CitaMedica(id=nuevo_id, paciente_id=paciente_id, medico_id=medico_id,
                   especialidad=especialidad, fecha=fecha, hora=hora, lugar=lugar)
    citas.append(c)
    print(f"  Cita registrada con exito. ID: {nuevo_id}")


def buscar_cita(medico_id):
    encontradas = [c for c in citas if c.medico_id == medico_id]
    return encontradas


def listar_citas(lista=None):
    lista = lista if lista is not None else citas
    if not lista:
        print("  No hay citas registradas.")
        return
    for c in lista:
        print(f"  ID:{c.id} | Paciente:{c.paciente_id} | Medico:{c.medico_id} | {c.especialidad} | {c.fecha} {c.hora} | {c.lugar}")


def actualizar_cita(medico_id):
    lista = buscar_cita(medico_id)
    if not lista:
        print("  [Error] No se encontro una cita con ese medico.")
        return
    c = lista[0]
    print(f"  Editando cita ID: {c.id}")
    print("  Deje el campo vacio para no cambiar el dato.")
    fecha = input("Nueva fecha (DD/MM/AAAA): ")
    if fecha.strip():
        c.fecha = validar_fecha(fecha)
    hora = input("Nueva hora (HH:MM): ")
    if hora.strip():
        c.hora = validar_hora(hora)
    lugar = input("Nuevo lugar: ")
    if lugar.strip():
        c.lugar = validar_nombre(lugar)
    print("  Cita actualizada con exito.")


def eliminar_cita(medico_id):
    lista = buscar_cita(medico_id)
    if not lista:
        print("  [Error] No se encontro una cita con ese medico.")
        return
    citas.remove(lista[0])
    print("  Cita eliminada con exito.")


def contar_citas():
    return len(citas)
