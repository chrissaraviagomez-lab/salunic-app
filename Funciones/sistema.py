# Funciones del sistema (usan Datos y Entidades según reglas)
from Datos import cargar_datos, guardar_datos, usuarios, citas, medicamentos, almacen
from Entidades import Usuario, CitaMedica, Medicamento, AlmacenMedicamento
from .busqueda_lineal import busqueda_lineal_por_email, busqueda_lineal
from .cola_atencion import cola_atencion


def iniciar_sistema():
    try:
        cargar_datos()
    except Exception:
        pass


def guardar_sistema():
    try:
        guardar_datos()
    except Exception:
        pass


def obtener_usuarios():
    iniciar_sistema()
    return usuarios


def obtener_citas():
    iniciar_sistema()
    return citas


def autenticar_usuario(email, password):
    iniciar_sistema()
    user_found = busqueda_lineal_por_email(usuarios, email)
    if user_found and getattr(user_found, 'password', None) == password:
        return user_found
    return None


def registrar_usuario_app(nombre, email, password, telefono="+505 00000000"):
    iniciar_sistema()
    # verificar duplicado
    existente = busqueda_lineal_por_email(usuarios, email)
    if existente:
        return None
    new_id = max([u.id for u in usuarios], default=0) + 1
    nuevo = Usuario(id=new_id, nombre=nombre, email=email, password=password, telefono=telefono)
    usuarios.append(nuevo)
    guardar_sistema()
    return nuevo


def actualizar_usuario_app(email_actual, nombre=None, email_nuevo=None, telefono=None):
    """Actualiza datos de usuario (para formularios de la app)."""
    iniciar_sistema()
    u = busqueda_lineal_por_email(usuarios, email_actual)
    if not u:
        return False
    if email_nuevo and email_nuevo.lower() != email_actual.lower():
        duplicado = busqueda_lineal_por_email(usuarios, email_nuevo)
        if duplicado:
            return False
        u.email = email_nuevo
    if nombre is not None:
        u.nombre = nombre
    if telefono is not None:
        u.telefono = telefono
    guardar_sistema()
    return True


def agregar_cita(paciente_id, medico_id, especialidad, fecha, hora, lugar="Hospital"):
    iniciar_sistema()
    new_id = max([c.id for c in citas], default=0) + 1
    c = CitaMedica(id=new_id, paciente_id=paciente_id, medico_id=medico_id,
                   especialidad=especialidad, fecha=fecha, hora=hora, lugar=lugar)
    citas.append(c)
    guardar_sistema()
    return c


def agregar_a_cola(paciente, cita_id, hora, es_adulto_mayor=False):
    item = {"paciente": paciente, "cita_id": cita_id, "hora": hora}
    cola_atencion.encolar(item, es_adulto_mayor=es_adulto_mayor)
    return item


def atender_siguiente():
    return cola_atencion.desencolar()


def obtener_cola():
    try:
        return sorted(cola_atencion.cola, key=lambda x: (x[0], x[1]))
    except Exception:
        return list(getattr(cola_atencion, 'cola', []))


def cola_vacia():
    return cola_atencion.esta_vacia()
