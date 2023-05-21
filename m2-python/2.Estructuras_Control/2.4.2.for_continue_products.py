'''
Ejemplo de bucle for con palabra reservada continue que salta a la siguiente iteración
'''
lechuga = [3.99, 'verduras']
tomate = [4.99, 'verdura']
barcelo = [29.99, 'alcohol']
escalopines = [12.99, 'carnes']
jack_daniels = [39.99, 'alcohol']
yogures = [4.50, 'lacteos']
queso = [14.99, 'lacteos']

productos = [lechuga, tomate, barcelo, escalopines, jack_daniels, yogures, queso]

# Aplicar descuento del 10% a los productos menos a
# los que contemgan alcohol
# Utilizar for y continue

for producto in productos:
    # print(producto[0], producto[1])
    if producto[1]=='alcohol':
        continue

    producto[0] *= 0.90
    # producto[0] = producto[0] * 0.90
    # producto[0] = producto[0] - producto[0] * 0.10
    
for producto in productos:
    print(producto)    

