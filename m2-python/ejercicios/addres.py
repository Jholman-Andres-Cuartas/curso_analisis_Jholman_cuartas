
class Address:

    def __init__(self, id_addres, street, city, postal_code, country, proyecto):
        self.id_addres = id_addres
        self.street = street
        self.city = city
        self.postal_code = postal_code
        self.country = country
        if (len(proyecto) >= 21):
            self.proyecto = proyecto
        else:
            self.proyecto = 'Data Analytics Adecco'


Address1 = Address(1, 'de la alegría', 'Madrid', 28025, 'Hispania','')
Address2 = Address(2, 'pricincipe pio pio', 'Madrid', 28020, 'Hispania','')
Address3 = Address(3, 'Reina sofi', 'Madrid', 28030, 'Hispania','')
Address4 = Address(4, 'Avenida de America', 'Madrid', 28015, 'Hispania','')
Address5 = Address(5, 'Republica Argentina', 'Madrid', 28040, 'Hispania','')
Address6 = Address(6, 'Colombia', 'Madrid', 28045, 'Hispania','')
Address7 = Address(7, 'Cusco', 'Madrid', 28060, 'Hispania','')
Address8 = Address(8, 'Norte Quito sur', 'Bogotá', 193945, 'Colombia','')
Address9 = Address(9, 'Las palmeras', 'Lima', 48032, 'Peru','')
Address10 = Address(10, 'Plaza de mayo', 'Buenos Aires', 75023, 'Argentina','')
Address11 = Address(11, 'palmeiras', 'Belo Horizonte', 98065, 'Brasil','')
Address12 = Address(12, 'los libertadores', 'Caracas', 63025, 'Hispania','')

print(Address1.street, Address2.street, Address3.street, Address4.street)
print(Address12.street)
print(Address12.proyecto)


user3 = User(3, '54345643T', )