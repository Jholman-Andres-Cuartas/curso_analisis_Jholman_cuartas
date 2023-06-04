from fire import Fire

class FireDatabase:
    def __init__(self):
        self.fires = []

    def add_fire(self, fire):
        self.fires.append(fire)

    def remove_fire(self, fire):
        self.fires.remove(fire)

    def get_all_fires(self):
        return self.fires

    def update_fire(self, fire_id, updated_fire):
        if fire_id < len(self.fires):
            self.fires[fire_id] = updated_fire

    def load_from_file(self, filename):
        self.fires = []
        try:
            with open(filename, "r") as file:
                for line in file:
                    data = line.strip().split(",")
                    provincia, kilometro, nivel, causa = data
                    fire = Fire(provincia, float(kilometro), nivel, causa)
                    self.fires.append(fire)
        except FileNotFoundError:
            print("El archivo no existe. No se cargaron incendios.")

    def save_to_file(self, filename):
        with open(filename, "w") as file:
            for fire in self.fires:
                file.write(f"{fire.provincia},{fire.kilometro},{fire.nivel},{fire.causa}\n")
