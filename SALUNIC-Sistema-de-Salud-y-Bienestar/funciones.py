import re
from datetime import datetime

from entidades import Usuario, CitaMedica, Medicamento, AlmacenMedicamento
from datos import usuarios, citas, medicamentos, almacen, inventario_inicial, medicamentos_iniciales


# =========================================================
# CARGAR DATOS INICIALES
# =========================================================
def cargar_datos_iniciales():
    """Carga medicamentos e inventario del MINSA si las listas estan vacias."""
    if not medicamentos:
        medicamentos.extend(medicamentos_iniciales)
    if not almacen:
        almacen.extend(inventario_inicial)


# =========================================================
# VALIDACIONES
# =========================================================
def validar_nombre(texto):
    if not texto.strip():
        raise ValueError("El nombre no puede estar vacio.")
    if not re.match(r"^[A-Za-záéíóúÁÉÍÓÚÑñ ]+$", texto):
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


# =========================================================
# USUARIOS - CRUD
# =========================================================
def registrar_usuario():
    print("\n--- Registrar Usuario ---")
    nombre = pedir_campo("Nombre completo: ", validar_nombre)
    email = pedir_campo("Email: ", validar_email)
    if buscar_usuario(email):
        print("  [Error] Ya existe un usuario con ese email.")
        return
    password = pedir_campo("Contrasena: ", validar_password)
    telefono = pedir_campo("Telefono: ", validar_celular)
    nuevo_id = max([u.id for u in usuarios], default=0) + 1
    usuarios.append(Usuario(id=nuevo_id, nombre=nombre, email=email,
                            password=password, telefono=telefono))
    print(f"  Usuario registrado con exito. ID: {nuevo_id}")


def buscar_usuario(email):
    for u in usuarios:
        if u.email == email:
            return u
    return None


def listar_usuarios():
    if not usuarios:
        print("  No hay usuarios registrados.")
        return
    for u in usuarios:
        print(f"  ID:{u.id} | {u.nombre} | {u.email} | {u.telefono}")


def actualizar_usuario(email):
    u = buscar_usuario(email)
    if not u:
        print("  [Error] No se encontro un usuario con ese email.")
        return
    print(f"  Editando: {u.nombre} (ID: {u.id})")
    print("  Deje el campo vacio para no cambiar el dato.")
    nombre = input("Nuevo nombre: ")
    if nombre.strip():
        u.nombre = validar_nombre(nombre)
    telefono = input("Nuevo telefono: ")
    if telefono.strip():
        u.telefono = validar_celular(telefono)
    print("  Usuario actualizado con exito.")


def eliminar_usuario(email):
    u = buscar_usuario(email)
    if not u:
        print("  [Error] No se encontro un usuario con ese email.")
        return
    usuarios.remove(u)
    print("  Usuario eliminado con exito.")


def contar_usuarios():
    return len(usuarios)


# =========================================================
# CITAS MEDICAS - CRUD
# =========================================================
def registrar_cita():
    print("\n--- Registrar Cita Medica ---")
    paciente_id = pedir_campo("ID del paciente: ", lambda x: int(x) if x.strip().isdigit() else (_ for _ in ()).throw(ValueError("Debe ser un numero entero.")))
    medico_id = pedir_campo("ID del medico: ", lambda x: int(x) if x.strip().isdigit() else (_ for _ in ()).throw(ValueError("Debe ser un numero entero.")))
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


# =========================================================
# MEDICAMENTOS - CRUD
# =========================================================
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


# =========================================================
# ALMACEN/INVENTARIO - CRUD
# =========================================================
def registrar_stock():
    print("\n--- Registrar Stock en Almacen ---")
    medico_id = pedir_campo("ID del medicamento: ", lambda x: int(x) if x.strip().isdigit() else (_ for _ in ()).throw(ValueError("Debe ser un numero entero.")))
    cantidad = pedir_campo("Cantidad: ", validar_cantidad)
    fecha_ven = pedir_campo("Fecha vencimiento (DD/MM/AAAA): ", validar_fecha)
    nuevo_id = max([a.id for a in almacen], default=0) + 1
    a = AlmacenMedicamento(id=nuevo_id, medicamento_id=medico_id,
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