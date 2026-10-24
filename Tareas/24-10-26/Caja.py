


precio = float(input("Ingrese el precio del producto (0 para terminar): "))
total = 0
cantidad = 0

while precio != 0:
    total = total + precio
    cantidad = cantidad + 1

    precio = float(input("Ingrese el precio del producto (0 para terminar): "))

print("Cantidad de productos:", cantidad)
print("Total de la compra:", round(total, 2), "Bs")
print("Fin")