import funciones as f

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
    print(SUB)
    print("0. Salir")


# =========================================================
# SUBMENU DE USUARIOS
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
            f.registrar_usuario()
        elif opc == 2:
            email = input("Email a buscar: ").strip().lower()
            u = f.buscar_usuario(email)
            print(f"  ID:{u.id} | {u.nombre} | {u.email} | {u.telefono}" if u else "  No se encontro el usuario.")
        elif opc == 3:
            email = input("Email del usuario a actualizar: ").strip().lower()
            f.actualizar_usuario(email)
        elif opc == 4:
            email = input("Email del usuario a eliminar: ").strip().lower()
            f.eliminar_usuario(email)
        elif opc == 5:
            print(f"  Total de usuarios: {f.contar_usuarios()}")
        elif opc == 6:
            f.listar_usuarios()
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
            f.registrar_cita()
        elif opc == 2:
            medico_id = input("ID del medico a buscar: ").strip()
            if medico_id.isdigit():
                f.listar_citas(f.buscar_cita(int(medico_id)))
            else:
                print("  [Error] Debe ingresar un numero valido.")
        elif opc == 3:
            medico_id = input("ID del medico de la cita a actualizar: ").strip()
            if medico_id.isdigit():
                f.actualizar_cita(int(medico_id))
            else:
                print("  [Error] Debe ingresar un numero valido.")
        elif opc == 4:
            medico_id = input("ID del medico de la cita a eliminar: ").strip()
            if medico_id.isdigit():
                f.eliminar_cita(int(medico_id))
            else:
                print("  [Error] Debe ingresar un numero valido.")
        elif opc == 5:
            print(f"  Total de citas: {f.contar_citas()}")
        elif opc == 6:
            f.listar_citas()
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
            f.registrar_medicamento()
        elif opc == 2:
            nombre = input("Medicamento a buscar: ").strip()
            f.listar_medicamentos(f.buscar_medicamento(nombre))
        elif opc == 3:
            nombre = input("Medicamento a actualizar: ").strip()
            f.actualizar_medicamento(nombre)
        elif opc == 4:
            nombre = input("Medicamento a eliminar: ").strip()
            f.eliminar_medicamento(nombre)
        elif opc == 5:
            print(f"  Total de medicamentos: {f.contar_medicamentos()}")
        elif opc == 6:
            f.listar_medicamentos()
        else:
            print("  [Error] Opcion invalida.")


# =========================================================
# SUBMENU DE ALMACEN / INVENTARIO
# =========================================================
def submenu_almacen():
    while True:
        cabecera_modulo("GESTION DE ALMACEN / INVENTARIO")
        print("1. Registrar stock en almacen")
        print("2. Buscar stock por medicamento")
        print("3. Actualizar stock")
        print("4. Eliminar stock")
        print("5. Contar items en almacen")
        print("6. Listar todo el almacen")
        print(SUB)
        print("0. Volver al menu principal")

        opc = pedir_opcion()

        if opc == 0:
            return
        elif opc == 1:
            f.registrar_stock()
        elif opc == 2:
            med_id = input("ID del medicamento a buscar: ").strip()
            if med_id.isdigit():
                f.listar_stock(f.buscar_stock(int(med_id)))
            else:
                print("  [Error] Debe ingresar un numero valido.")
        elif opc == 3:
            med_id = input("ID del medicamento del stock a actualizar: ").strip()
            if med_id.isdigit():
                f.actualizar_stock(int(med_id))
            else:
                print("  [Error] Debe ingresar un numero valido.")
        elif opc == 4:
            med_id = input("ID del medicamento del stock a eliminar: ").strip()
            if med_id.isdigit():
                f.eliminar_stock(int(med_id))
            else:
                print("  [Error] Debe ingresar un numero valido.")
        elif opc == 5:
            print(f"  Total de items en almacen: {f.contar_stock()}")
        elif opc == 6:
            f.listar_stock()
        else:
            print("  [Error] Opcion invalida.")


def main():
    f.cargar_datos_iniciales()

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
        else:
            print("  [Error] Opcion invalida.")


if __name__ == "__main__":
    main()
