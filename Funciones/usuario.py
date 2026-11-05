from Entidades import Usuario
from Datos import usuarios
from .validaciones import validar_nombre, validar_email, validar_password, validar_celular, pedir_campo


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
