

class Travel


def __init__(self, city_from, city_to, date_from, date_to):
    self.city_from = city_from
    self.city_to = city_to
    self.date_from = date_from
    self.date_to = date_to


date_from = datetime.date.today()
date_to = datetime.date.today()
travel1 = travel1("Madrid", "Praga", date_from, date_to)

print(f"Dia de salida {Travel.date_from}" y dia de regreso {date_to})
