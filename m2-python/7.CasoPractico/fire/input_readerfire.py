from fire import Fire
from fires_database import FireDatabase

def print_menu():
    print("------- Menú -------")
    print("1. Mostrar todos los incendios")
    print("2. Buscar incendio por ID")
    print("3. Buscar incendio por nivel")
    print("4. Agregar un nuevo incendio")
    print("5. Actualizar un incendio")
    print("6. Eliminar un incendio")
    print("0. Salir")
    print("---------------------")

def create_fire():
    prov = input("Ingrese la prov del incendio: ")
    Km = input("Ingrese el Km del incendio: ")
    nivel = input("Ingrese el nivel del incendio: ")
    causa = input("Ingrese la causa del incendio: ")
    return Fire(prov, Km, nivel, causa)

def show_all_fires(db):
    fires = db.find_all()
    if not fires:
        print("No hay incendios registrados.")
    else:
        for fire in fires:
            print(f"ID: {fire.id}, prov: {fire.prov}, Km: {fire.Km}, Nivel: {fire.nivel}, Causa: {fire.causa}")

def search_fire_by_id(db):
    id = int(input("Ingrese el ID del incendio: "))
    fire = db.find_by_id(id)
    if fire:
        print(f"ID: {fire.id}, prov: {fire.prov}, Km: {fire.Km}, Nivel: {fire.nivel}, Causa: {fire.causa}")