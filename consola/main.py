import sys
import os

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

# Estructura requerida por el profesor: consola usa Entidades, Datos y Funciones
from Datos import usuarios, citas, medicamentos, almacen
from Datos.datos import cargar_datos, guardar_datos, cargar_datos_iniciales
from Funciones import usuario as f_usuario
from Funciones import cita_medica as f_cita
from Funciones import medicamento as f_medicamento
from Funciones import almacen_medicamento as f_almacen
from Funciones.cola_atencion import cola_atencion

TITULO = "SALUNIC - Sistema de Salud y Bienestar"
LINEA = "=" * 55
SUB = "-" * 55


def cabecera_modulo(nombre):
    print("\n" + SUB)
    print(f"  MENU {nombre}")
    print(SUB)


def pedir_opcion():
    while True:
        try:
            opc = input("Seleccione una opcion: ").strip()
            if not opc.isdigit():
                raise ValueError("Debe ingresar un numero.")
            return int(opc)
        except ValueError as e:
            print(f"  [Error] {e}")


def mostrar_menu_principal():
    print("\n" + LINEA)
    print(TITULO)
    print(LINEA)
    print("SELECCIONE UN MODULO:")
    print("1. Gestion de Usuarios")
    print("2. Gestion de Citas Medicas")
    print("3. Gestion de Medicamentos")
    print("4. Gestion de Almacen / Inventario")
    print("5. Cola de Atencion con Prioridad")
    print("6. Archivo de Datos (Guardar/Cargar)")
    print(SUB)
    print("0. Salir")


# =========================================================
# SUBMENU DE USUARIOS (usa Funciones.usuario + Datos/Entidades)
# =========================================================
def submenu_usuarios():
    while True:
        cabecera_modulo("GESTION DE USUARIOS")
        print("1. Registrar un usuario")
        print("2. Buscar un usuario")
        print("3. Actualizar un usuario")
        print("4. Eliminar un usuario")
        print("5. Contar usuarios")
        print("6. Listar todos los usuarios")
        print(SUB)
        print("0. Volver al menu principal")

        opc = pedir_opcion()

        if opc == 0:
            return
        elif opc == 1:
            f_usuario.registrar_usuario()
        elif opc == 2:
            email = input("Email a buscar: ").strip().lower()
            u = f_usuario.buscar_usuario(email)
            print(f"  ID:{u.id} | {u.nombre} | {u.email} | {u.telefono}" if u else "  No se encontro el usuario.")
        elif opc == 3:
            email = input("Email del usuario a actualizar: ").strip().lower()
            f_usuario.actualizar_usuario(email)
        elif opc == 4:
            email = input("Email del usuario a eliminar: ").strip().lower()
            f_usuario.eliminar_usuario(email)
        elif opc == 5:
            print(f"  Total de usuarios: {f_usuario.contar_usuarios()}")
        elif opc == 6:
            f_usuario.listar_usuarios()
        else:
            print("  [Error] Opcion invalida.")


# =========================================================
# SUBMENU DE CITAS MEDICAS
# =========================================================
def submenu_citas():
    while True:
        cabecera_modulo("GESTION DE CITAS MEDICAS")
        print("1. Registrar una cita medica")
        print("2. Buscar una cita medica")
        print("3. Actualizar una cita")
        print("4. Eliminar una cita")
        print("5. Contar citas")
        print("6. Listar todas las citas")
        print(SUB)
        print("0. Volver al menu principal")

        opc = pedir_opcion()

        if opc == 0:
            return
        elif opc == 1:
            f_cita.registrar_cita()
        elif opc == 2:
            medico_id = input("ID del medico a buscar: ").strip()
            if medico_id.isdigit():
                f_cita.listar_citas(f_cita.buscar_cita(int(medico_id)))
            else:
                print("  [Error] Debe ingresar un numero valido.")
        elif opc == 3:
            medico_id = input("ID del medico de la cita a actualizar: ").strip()
            if medico_id.isdigit():
                f_cita.actualizar_cita(int(medico_id))
            else:
                print("  [Error] Debe ingresar un numero valido.")
        elif opc == 4:
            medico_id = input("ID del medico de la cita a eliminar: ").strip()
            if medico_id.isdigit():
                f_cita.eliminar_cita(int(medico_id))
            else:
                print("  [Error] Debe ingresar un numero valido.")
        elif opc == 5:
            print(f"  Total de citas: {f_cita.contar_citas()}")
        elif opc == 6:
            f_cita.listar_citas()
        else:
            print("  [Error] Opcion invalida.")


# =========================================================
# SUBMENU DE MEDICAMENTOS
# =========================================================
def submenu_medicamentos():
    while True:
        cabecera_modulo("GESTION DE MEDICAMENTOS")
        print("1. Registrar un medicamento")
        print("2. Buscar un medicamento")
        print("3. Actualizar un medicamento")
        print("4. Eliminar un medicamento")
        print("5. Contar medicamentos")
        print("6. Listar todos los medicamentos")
        print(SUB)
        print("0. Volver al menu principal")

        opc = pedir_opcion()

        if opc == 0:
            return
        elif opc == 1:
            f_medicamento.registrar_medicamento()
        elif opc == 2:
            nombre = input("Medicamento a buscar: ").strip()
            f_medicamento.listar_medicamentos(f_medicamento.buscar_medicamento(nombre))
        elif opc == 3:
            nombre = input("Medicamento a actualizar: ").strip()
            f_medicamento.actualizar_medicamento(nombre)
        elif opc == 4:
            nombre = input("Medicamento a eliminar: ").strip()
            f_medicamento.eliminar_medicamento(nombre)
        elif opc == 5:
            print(f"  Total de medicamentos: {f_medicamento.contar_medicamentos()}")
        elif opc == 6:
            f_medicamento.listar_medicamentos()
        else:
            print("  [Error] Opcion invalida.")


# =========================================================
# SUBMENU DE ALMACEN / INVENTARIO
# =========================================================
def submenu_almacen():
    while True:
        cabecera_modulo("GESTION DE ALMACEN / INVENTARIO")
        print("1. Registrar stock en almacen")
        print("2. Buscar stock por ID de medicamento")
        print("3. Actualizar stock")
        print("4. Eliminar stock")
        print("5. Contar registros de stock")
        print("6. Listar todo el inventario")
        print(SUB)
        print("0. Volver al menu principal")

        opc = pedir_opcion()

        if opc == 0:
            return
        elif opc == 1:
            f_almacen.registrar_stock()
        elif opc == 2:
            med_id = input("ID del medicamento a buscar: ").strip()
            if med_id.isdigit():
                f_almacen.listar_stock(f_almacen.buscar_stock(int(med_id)))
            else:
                print("  [Error] Debe ingresar un numero valido.")
        elif opc == 3:
            med_id = input("ID del medicamento del stock a actualizar: ").strip()
            if med_id.isdigit():
                f_almacen.actualizar_stock(int(med_id))
            else:
                print("  [Error] Debe ingresar un numero valido.")
        elif opc == 4:
            med_id = input("ID del medicamento del stock a eliminar: ").strip()
            if med_id.isdigit():
                f_almacen.eliminar_stock(int(med_id))
            else:
                print("  [Error] Debe ingresar un numero valido.")
        elif opc == 5:
            print(f"  Total de registros de stock: {f_almacen.contar_stock()}")
        elif opc == 6:
            f_almacen.listar_stock()
        else:
            print("  [Error] Opcion invalida.")


# =========================================================
# SUBMENU DE COLA DE ATENCION (CON PRIORIDAD + heapq)
# =========================================================
def submenu_cola_atencion():
    while True:
        cabecera_modulo("COLA DE ATENCION - CON PRIORIDAD")
        print("1. Agregar paciente a la cola")
        print("2. Atender siguiente paciente (Por prioridad)")
        print("3. Mostrar cola de espera")
        print("4. Ver cantidad en cola")
        print(SUB)
        print("0. Volver al menu principal")

        opc = pedir_opcion()

        if opc == 0:
            return
        elif opc == 1:
            print("\n--- Agregar a Cola de Atencion ---")
            if not citas:
                print("  [INFO] No hay citas registradas. Registre una cita primero.")
                continue
            f_cita.listar_citas()
            cita_id = input("Ingrese ID de la cita a encolar: ").strip()
            if not cita_id.isdigit():
                print("  [Error] Debe ingresar un numero valido.")
                continue
            cita_id = int(cita_id)
            cita_sel = None
            for c in citas:
                if c.id == cita_id:
                    cita_sel = c
                    break
            if not cita_sel:
                print("  [Error] No se encontro la cita con ese ID.")
                continue
            paciente = None
            for u in usuarios:
                if u.id == cita_sel.paciente_id:
                    paciente = u
                    break
            print("\n  ¿Es adulto mayor?")
            print("  1. Si - TIENE PRIORIDAD")
            print("  2. No")
            prio = input("Seleccione: ").strip()
            es_mayor = (prio == "1")
            cola_atencion.encolar({
                "cita_id": cita_sel.id,
                "paciente_id": cita_sel.paciente_id,
                "paciente": paciente.nombre if paciente else "Desconocido",
                "hora": cita_sel.hora,
                "especialidad": cita_sel.especialidad
            }, es_adulto_mayor=es_mayor)
        elif opc == 2:
            cola_atencion.desencolar()
        elif opc == 3:
            cola_atencion.mostrar_cola()
        elif opc == 4:
            print(f"  Pacientes en espera: {cola_atencion.tamanio()}")
        else:
            print("  [Error] Opcion invalida.")


# =========================================================
# SUBMENU ARCHIVO DE DATOS (JSON)
# =========================================================
def submenu_archivo_datos():
    while True:
        cabecera_modulo("ARCHIVO DE DATOS - PERSISTENCIA")
        print("1. Guardar datos en archivo JSON")
        print("2. Cargar datos desde archivo JSON")
        print(SUB)
        print("0. Volver al menu principal")

        opc = pedir_opcion()

        if opc == 0:
            return
        elif opc == 1:
            guardar_datos()
        elif opc == 2:
            cargar_datos()
        else:
            print("  [Error] Opcion invalida.")


def main():
    print("\n" + LINEA)
    print("  BIENVENIDO A SALUNIC - SISTEMA DE SALUD Y BIENESTAR")
    print(LINEA)
    print("  [INFO] Cargando datos iniciales...")
    cargar_datos_iniciales()

    while True:
        mostrar_menu_principal()
        opc = pedir_opcion()

        if opc == 0:
            print("\nGracias por usar SALUNIC. Hasta pronto!")
            break
        elif opc == 1:
            submenu_usuarios()
        elif opc == 2:
            submenu_citas()
        elif opc == 3:
            submenu_medicamentos()
        elif opc == 4:
            submenu_almacen()
        elif opc == 5:
            submenu_cola_atencion()
        elif opc == 6:
            submenu_archivo_datos()
        else:
            print("  [Error] Opcion invalida.")


if __name__ == "__main__":
    main()
