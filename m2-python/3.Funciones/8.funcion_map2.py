prices = [10, 20, 30, 40, 50]

prices_iva = []

# Opción 1: bucle for tradicioal
for price in prices:
    prices_iva.append(price * 1.21)

# print(prices_iva)

# opción 2: función def


def sumarIva(price):
    return price * 1.21


print(f"El resultado es: {list(map(sumarIva, prices))}")

# opción 3: función map con función lambda


def sumarIVA2(price): return price * 1.21


print(f"El resultado con lambda es: {list(map(sumarIVA2, price))}")

print(f"Hay un total de {len(prices)} products")
