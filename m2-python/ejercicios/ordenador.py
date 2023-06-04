# crear una clase
class Ordenador:

    def __init__(self, fabricante, modelo, anio, precio, estado):
        self.fabricante = fabricante
        self.modelo = modelo
        self.anio = anio
        self.precio = precio
        self.estado = False
# comportamiento : metodos, cambian el estado

    def encender(self)
    self.estado = True

    def aplicar_descuento(self, descuento):
        if (descuento > 0 and descuento < 0.9):

            # creación de objetos / instancias


Ordenador1 = Ordenador("ASUS", "A55A", 2008, 495)
Ordenador1.precio *= 0.9

Ordenador2 = Ordenador("MSI", "Modern 15", 2021, 935)  # apagado
Ordenador2.encender()
Ordenador2.aplicar_descuento(0.10)
# Recomendable usar metodos en lugar de los atributos directamente
Ordenador2.encender()
Ordenador2.aplicar_descuento(0.10)  # si se aplica
Ordenador2.aplicar_descuento(-0.4)  # si no se aplica
