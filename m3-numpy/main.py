from fire import Fire
from fires_database import FireDatabase


def obtener_opcion():
    print("----- Menú de opciones -----")
    print("1. Crear un nuevo incendio")
    print("2. Actualizar un incendio existente")
    print("3. Eliminar un incendio")
    print("4. Mostrar todos los incendios")
    print("5. Salir")
    opcion = input("Ingrese una opción: ")
    return opcion


def ejecutar_opcion(opcion, fire_db):
    if opcion == "1":
        provincia = input("Ingrese la provincia: ")
        kilometro = float(input("Ingrese el kilómetro: "))
        nivel = input("Ingrese el nivel: ")
        causa = input("Ingrese la causa: ")
        fire = Fire(provincia, kilometro, nivel, causa)
        fire_db.add_fire(fire)
        print("Incendio creado exitosamente.")
    elif opcion == "2":
        fire_id = int(input("Ingrese el ID del incendio a actualizar: "))
        fires = fire_db.get_all_fires()
        if fire_id < len(fires):
            provincia = input("Ingrese la nueva provincia: ")
            kilometro = float(input("Ingrese el nuevo kilómetro: "))
            nivel = input("Ingrese el nuevo nivel: ")
            causa = input("Ingrese la nueva causa: ")
            updated_fire = Fire(provincia, kilometro, nivel, causa)
            fire_db.update_fire(fire_id, updated_fire)
            print("Incendio actualizado exitosamente.")
        else:
            print("ID de incendio inválido.")
    elif opcion == "3":
        fire_id = int(input("Ingrese el ID del incendio a eliminar: "))
        fires = fire_db.get_all_fires()
        if fire_id < len(fires):
            fire_db.remove_fire(fires[fire_id])
            print("Incendio eliminado exitosamente.")
        else:
            print("ID de incendio inválido.")
    elif opcion == "4":
        fires = fire_db.get_all_fires()
        print("Lista de incendios:")
        for i, fire in enumerate(fires):
            print(f"ID: {i}, {fire}")
    elif opcion == "5":
        print("Saliendo...")
        fire_db.save_to_file("fires.txt")
        exit()
    else:
        print("Opción inválida.")


def main():
    fire_db = FireDatabase()
    fire_db.load_from_file("fires.txt")

    while True:
        opcion = obtener_opcion()
        ejecutar_opcion(opcion, fire_db)
        print()


if __name__ == "__main__":
    main()
