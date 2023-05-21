import datetime


class Travel:

    def __init__(self):

        self.travels = []

    def find_all(self):
        return self.travels.copy()
    # Return list (self.travels)
    # SELECT * FROM travels WHERE id = id_travel
    # travel_database.find_by_id (8)

    def find_by_id(self, id_travel):
        # iterar sobre los viajes
        for travel in self.travels:
            if travel.id == id_travel:
                return travel
        return None

    def find_all_by_city(self, city_from, city_to):
        filtered_travels = []

        for travel in self.travels:
            if travel.city_from == city_from and travel.city_to == city_to:
                filtered_travels.append(travel)

        return filtered_travels

    def save(self, travel):
        id_max = 0
        for current in self.travels:
            if current.id > id_max:
                id_max = current.id
                travel.id = id_max + 1

        self.travels.append(travel)

    def update(self, travel):
        travel.id

        current.city_from = travel.city_from
        current.price = travel.price

    def delete_by_id(self, id):
        for travel in self.travels:
            if travel.id == id:
                self.travels.remove(travel)
                break


# SELEC * FROM travels
# WHERE city_from = "" AND city_to = ""
