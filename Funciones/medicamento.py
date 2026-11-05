from Entidades import Medicamento
from Datos import medicamentos
from .validaciones import validar_nombre, validar_dosis, validar_descripcion, pedir_campo


def registrar_medicamento():
    print("\n--- Registrar Medicamento ---")
    nombre = pedir_campo("Nombre: ", validar_nombre)
    dosis = pedir_campo("Dosis (ej: 500mg): ", validar_dosis)
    frecuencia = pedir_campo("Frecuencia (ej: 1 vez al dia): ", validar_descripcion)
    presentacion = pedir_campo("Presentacion (ej: Tabletas): ", validar_nombre)
    nuevo_id = max([m.id for m in medicamentos], default=0) + 1
    m = Medicamento(id=nuevo_id, nombre=nombre, dosis=dosis,
                    frecuencia=frecuencia, presentacion=presentacion)
    medicamentos.append(m)
    print(f"  Medicamento registrado con exito. ID: {nuevo_id}")


def buscar_medicamento(nombre):
    encontrados = [m for m in medicamentos if m.nombre.lower() == nombre.lower()]
    return encontrados


def listar_medicamentos(lista=None):
    lista = lista if lista is not None else medicamentos
    if not lista:
        print("  No hay medicamentos registrados.")
        return
    for m in lista:
        print(f"  ID:{m.id} | {m.nombre} {m.dosis} | {m.frecuencia} | {m.presentacion}")


def actualizar_medicamento(nombre):
    lista = buscar_medicamento(nombre)
    if not lista:
        print("  [Error] No se encontro un medicamento con ese nombre.")
        return
    m = lista[0]
    print(f"  Editando: {m.nombre} (ID: {m.id})")
    print("  Deje el campo vacio para no cambiar el dato.")
    dosis = input("Nueva dosis: ")
    if dosis.strip():
        m.dosis = validar_dosis(dosis)
    frecuencia = input("Nueva frecuencia: ")
    if frecuencia.strip():
        m.frecuencia = validar_descripcion(frecuencia)
    print("  Medicamento actualizado con exito.")


def eliminar_medicamento(nombre):
    lista = buscar_medicamento(nombre)
    if not lista:
        print("  [Error] No se encontro un medicamento con ese nombre.")
        return
    medicamentos.remove(lista[0])
    print("  Medicamento eliminado con exito.")


def contar_medicamentos():
    return len(medicamentos)
