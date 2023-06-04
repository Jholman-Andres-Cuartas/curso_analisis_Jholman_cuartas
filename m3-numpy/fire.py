class Fire:
    def __init__(self, provincia, kilometro, nivel, causa):
        self.provincia = provincia
        self.kilometro = kilometro
        self.nivel = nivel
        self.causa = causa

    def __str__(self):
        return f"{self.provincia} {self.kilometro} {self.nivel} {self.causa}"
