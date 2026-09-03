import funciones as f

TITULO = "SALUNIC - Sistema de Salud y Bienestar - Grupo 8"


def mostrar_menu():
    print("\n" + "=" * 55)
    print(TITULO)
    print("=" * 55)
    print("1. Registrar un usuario")
    print("2. Buscar un usuario")
    print("3. Actualizar un usuario")
    print("4. Eliminar un usuario")
    print("5. Contar usuarios")
    print("6. Listar todos los usuarios")
    print("-" * 55)
    print("7. Registrar una cita medica")
    print("8. Buscar una cita medica")
    print("9. Actualizar una cita")
    print("10. Eliminar una cita")
    print("11. Contar citas")
    print("12. Listar todas las citas")
    print("-" * 55)
    print("13. Registrar un medicamento")
    print("14. Buscar un medicamento")
    print("15. Actualizar un medicamento")
    print("16. Eliminar un medicamento")
    print("17. Contar medicamentos")
    print("18. Listar todos los medicamentos")
    print("-" * 55)
    print("19. Registrar stock en almacen")
    print("20. Buscar stock por medicamento")
    print("21. Actualizar stock")
    print("22. Eliminar stock")
    print("23. Contar items en almacen")
    print("24. Listar todo el almacen")
    print("-" * 55)
    print("0. Salir")


def pedir_opcion():
    while True:
        try:
            opc = input("Seleccione una opcion: ").strip()
            if not opc.isdigit():
                raise ValueError("Debe ingresar un numero.")
            return int(opc)
        except ValueError as e:
            print(f"  [Error] {e}")


def main():
    f.cargar_datos_iniciales()

    while True:
        mostrar_menu()
        opc = pedir_opcion()

        if opc == 0:
            print("\nGracias por usar SALUNIC. Hasta pronto!")
            break

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

        elif opc == 7:
            f.registrar_cita()
        elif opc == 8:
            medico_id = input("ID del medico a buscar: ").strip()
            if medico_id.isdigit():
                lista = f.buscar_cita(int(medico_id))
                f.listar_citas(lista)
            else:
                print("  [Error] Debe ingresar un numero valido.")
        elif opc == 9:
            medico_id = input("ID del medico de la cita a actualizar: ").strip()
            if medico_id.isdigit():
                f.actualizar_cita(int(medico_id))
            else:
                print("  [Error] Debe ingresar un numero valido.")
        elif opc == 10:
            medico_id = input("ID del medico de la cita a eliminar: ").strip()
            if medico_id.isdigit():
                f.eliminar_cita(int(medico_id))
            else:
                print("  [Error] Debe ingresar un numero valido.")
        elif opc == 11:
            print(f"  Total de citas: {f.contar_citas()}")
        elif opc == 12:
            f.listar_citas()

        elif opc == 13:
            f.registrar_medicamento()
        elif opc == 14:
            nombre = input("Medicamento a buscar: ").strip()
            lista = f.buscar_medicamento(nombre)
            f.listar_medicamentos(lista)
        elif opc == 15:
            nombre = input("Medicamento a actualizar: ").strip()
            f.actualizar_medicamento(nombre)
        elif opc == 16:
            nombre = input("Medicamento a eliminar: ").strip()
            f.eliminar_medicamento(nombre)
        elif opc == 17:
            print(f"  Total de medicamentos: {f.contar_medicamentos()}")
        elif opc == 18:
            f.listar_medicamentos()

        elif opc == 19:
            f.registrar_stock()
        elif opc == 20:
            medico_id = input("ID del medicamento a buscar: ").strip()
            if medico_id.isdigit():
                lista = f.buscar_stock(int(medico_id))
                f.listar_stock(lista)
            else:
                print("  [Error] Debe ingresar un numero valido.")
        elif opc == 21:
            medico_id = input("ID del medicamento del stock a actualizar: ").strip()
            if medico_id.isdigit():
                f.actualizar_stock(int(medico_id))
            else:
                print("  [Error] Debe ingresar un numero valido.")
        elif opc == 22:
            medico_id = input("ID del medicamento del stock a eliminar: ").strip()
            if medico_id.isdigit():
                f.eliminar_stock(int(medico_id))
            else:
                print("  [Error] Debe ingresar un numero valido.")
        elif opc == 23:
            print(f"  Total de items en almacen: {f.contar_stock()}")
        elif opc == 24:
            f.listar_stock()

        else:
            print("  [Error] Opcion invalida.")


if __name__ == "__main__":
    main()