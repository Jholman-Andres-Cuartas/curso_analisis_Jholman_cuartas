class Fire:
    def __init__(self, prov, Km, nivel, causa):
        self.id = None  # El ID se crea de inmediato al guardar el objeto
        self.prov = prov
        self.Km = Km
        self.nivel = nivel
        self.causa = causa


    # para imprimir un objeto
    def __str__(self):
        return f"{self.id} {self.prov} {self.Km} {self.nivel}{self.causa}"
    
    # REpresentacion Formal: para imprimir una la lista de objetos
    def __repr__(self):
        return f"{self.id} {self.prov} {self.Km} {self.nivel}{self.causa}"


    @classmethod
    def from_list(cls, fire_list):
        fires = []
        for fire_data in fire_list:
            fire = cls(fire_data["prov"], fire_data["Km"], fire_data["nivel"], fire_data["causa"])
            fires.append(fire)
        return fires
fire_data_list = [
    {"prov": "Alicante", "Km": 10, "nivel": "Alto", "causa": "Cigarrillo"},
    {"prov": "Valencia", "Km": 20, "nivel": "Moderado", "causa": "Fuego descuidado"},
    {"prov": "Madrid", "Km": 30, "nivel": "Bajo", "causa": "Quema de rastrojos"},
]

fires = Fire.from_list(fire_data_list)
print('fires')