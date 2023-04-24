

prices = [10, 20, 30, 40, 50]

price_iva = []

# opción 1: bucle for tradicional

for price in prices:
    price_in_iva.append(price * 1.21)

    # print(prices_iva)

# opción 2: función map con función lambda

# opción 2: función def


def sumarIva(price):
    return price * 1.21


print(f"El resultado es: {list(map(sumarIva, prices))}")

# opcion 3: función map con función lambda
sumarIVA2
