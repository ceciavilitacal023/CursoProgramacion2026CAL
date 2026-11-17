

precios = {"pan": 0.5, "leche": 6, "queso": 25}

for producto in precios:
    print(producto)


for producto, precio in precios.items():
    print(producto, "Bs", precio)


votos = ["Ana", "Luis", "Ana", "Eva", "Ana", "Luis"]

conteo = {}

for v in votos:
    if v in conteo:
        conteo[v] = conteo[v] + 1
    else:
        conteo[v] = 1

print(conteo)