class FireDatabase:
    def __init__(self):
        self.fires = []

    def find_all(self):
        return self.fires.copy()

    def find_by_id(self, id):
        for fire in self.fires:
            if fire.id == id:
                return fire
        return None

    def find_by_level(self, level):
        found_fires = []
        for fire in self.fires:
            if fire.nivel == level:
                found_fires.append(fire)
        return found_fires

    # Implementar más métodos find_by para filtrar por otros atributos

    def save(self, fire):
        if fire.id is None:
            fire.id = self._generate_id()
            self.fires.append(fire)

    def update(self, fire):
        existing_fire = self.find_by_id(fire.id)
        if existing_fire:
            existing_fire.prov = fire.prov
            existing_fire.Km = fire.Km
            existing_fire.nivel = fire.nivel
            existing_fire.causa = fire.causa

    def delete_by_id(self, id):
        for fire in self.fires:
            if fire.id == id:
                self.fires.remove(fire)
                break

    def _generate_id(self):
        if not self.fires:
            return 1
        else:
            max_id = max(fire.id for fire in self.fires)
            return max_id + 1