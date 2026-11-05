from Entidades import AlmacenMedicamento
from Datos import almacen, medicamentos
from .validaciones import validar_fecha, validar_cantidad, pedir_campo


def _validar_int(x):
    if x.strip().isdigit():
        return int(x)
    raise ValueError("Debe ser un numero entero.")


def registrar_stock():
    print("\n--- Registrar Stock en Almacen ---")
    medicamento_id = pedir_campo("ID del medicamento: ", _validar_int)
    cantidad = pedir_campo("Cantidad: ", validar_cantidad)
    fecha_ven = pedir_campo("Fecha vencimiento (DD/MM/AAAA): ", validar_fecha)
    nuevo_id = max([a.id for a in almacen], default=0) + 1
    a = AlmacenMedicamento(id=nuevo_id, medicamento_id=medicamento_id,
                           cantidad=cantidad, fecha_vencimiento=fecha_ven)
    almacen.append(a)
    print(f"  Stock registrado con exito. ID: {nuevo_id}")


def buscar_stock(medicamento_id):
    encontrados = [a for a in almacen if a.medicamento_id == medicamento_id]
    return encontrados


def listar_stock(lista=None):
    lista = lista if lista is not None else almacen
    if not lista:
        print("  No hay stock en el almacen.")
        return
    for a in lista:
        nombre_med = "Desconocido"
        for m in medicamentos:
            if m.id == a.medicamento_id:
                nombre_med = m.nombre
                break
        print(f"  ID:{a.id} | {nombre_med} | Cantidad:{a.cantidad} | Vence:{a.fecha_vencimiento}")


def actualizar_stock(medicamento_id):
    lista = buscar_stock(medicamento_id)
    if not lista:
        print("  [Error] No se encontro stock para ese medicamento.")
        return
    a = lista[0]
    print(f"  Editando stock ID: {a.id}")
    print("  Deje el campo vacio para no cambiar el dato.")
    cantidad = input("Nueva cantidad: ")
    if cantidad.strip():
        a.cantidad = validar_cantidad(cantidad)
    fecha_ven = input("Nueva fecha vencimiento (DD/MM/AAAA): ")
    if fecha_ven.strip():
        a.fecha_vencimiento = validar_fecha(fecha_ven)
    print("  Stock actualizado con exito.")


def eliminar_stock(medicamento_id):
    lista = buscar_stock(medicamento_id)
    if not lista:
        print("  [Error] No se encontro stock para ese medicamento.")
        return
    almacen.remove(lista[0])
    print("  Stock eliminado con exito.")


def contar_stock():
    return len(almacen)
