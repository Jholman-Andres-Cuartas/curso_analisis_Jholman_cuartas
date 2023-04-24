
# FUNCIÓN CON UN PARÁMETRO DE ENTRADA, NO DEVUELVE NADA
def print_is_adult(age):
    print('Es mayor de edad') if age >= 18 else print('Es menor de edad')


print_is_adult(17)
print_is_adult(18)
print_is_adult(19)
print_is_adult(20)
print_is_adult(20)

# FUNCIÓN CON UN PARÁMETRO DE ENTRADA Y QUE DEVUELVE BOOL: True o False


def es_mayor_edad(age):
    return age >= 18


print(es_mayor_edad(20))  # True
print(es_mayor_edad(15))  # False

11
m2-python/3.Funciones/2.funciones_scope.py


@ @ -0, 0 + 1, 11 @ @
def saludar():
    nombre = 'Mike'
    print(nombre)


saludar()
# print(nombre) # NameError: name 'nombre' is not defined
# todas las variables creadas dentro de un bloque de código, solo son accesibles dentro de ese bloque

24
m2-python/3.Funciones/3.funciones_pass.py


@ @ -0, 0 + 1, 24 @ @
def consultar_saldo():
    validar_pin("")
    return 0


def retirar_saldo():
    pass


def depositar_saldo():
    pass


def validar_pin(pin):
    pass


def transferir(cuenta):
    pass


def validar_cuenta(cuenta):
    pass


consultar_saldo()
17
m2-python/3.Funciones/4.funciones_argumentos.py


@ @ -0, 0 + 1, 17 @ @
# En JavaScript: console.log(`Hola ${name}`)
name = 'Juan'
age = 30

print(f"Hola soy {name} con edad {age}")
print("Hola soy " + name + ", con edad " + str(age))
print("Hola soy", name, "con edad", age)


def saludar(name, age):
    return f"Hola soy {name} con edad {age}"


saludo = saludar("Mike", 35)
print(saludo)

mapçç
