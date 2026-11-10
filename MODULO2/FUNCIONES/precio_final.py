

def precio_final(precio, descuento=10):
    return precio - (precio * descuento / 100)

precio = float(input("Ingrese el precio: "))

resultado = precio_final(precio)

print("El precio final es:", resultado)