"""Compatibilidad: funciones delegadas a la estructura requerida (Funciones/ y Datos/)."""
from Datos.datos import cargar_datos_iniciales
from Funciones.validaciones import (
    validar_nombre, validar_email, validar_password, validar_fecha, validar_hora,
    validar_dosis, validar_celular, validar_cantidad, validar_descripcion, pedir_campo,
)
from Funciones.usuario import (
    registrar_usuario, buscar_usuario, listar_usuarios, actualizar_usuario, eliminar_usuario, contar_usuarios,
)
from Funciones.cita_medica import (
    registrar_cita, buscar_cita, listar_citas, actualizar_cita, eliminar_cita, contar_citas,
)
from Funciones.medicamento import (
    registrar_medicamento, buscar_medicamento, listar_medicamentos, actualizar_medicamento, eliminar_medicamento, contar_medicamentos,
)
from Funciones.almacen_medicamento import (
    registrar_stock, buscar_stock, listar_stock, actualizar_stock, eliminar_stock, contar_stock,
)

__all__ = [
    "cargar_datos_iniciales",
    "validar_nombre","validar_email","validar_password","validar_fecha","validar_hora",
    "validar_dosis","validar_celular","validar_cantidad","validar_descripcion","pedir_campo",
    "registrar_usuario","buscar_usuario","listar_usuarios","actualizar_usuario","eliminar_usuario","contar_usuarios",
    "registrar_cita","buscar_cita","listar_citas","actualizar_cita","eliminar_cita","contar_citas",
    "registrar_medicamento","buscar_medicamento","listar_medicamentos","actualizar_medicamento","eliminar_medicamento","contar_medicamentos",
    "registrar_stock","buscar_stock","listar_stock","actualizar_stock","eliminar_stock","contar_stock",
]
