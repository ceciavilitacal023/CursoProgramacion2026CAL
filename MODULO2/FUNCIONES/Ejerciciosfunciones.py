
# cuadrado

def cuadrado(n):
    return n * n

for i in range(1, 6):
    print("El cuadrado de", i, "es:", cuadrado(i))

# es mayor de edad, devolver true o Flase y usarlo en un if

def es_mayor(edad):
    return edad >= 18

edad = int(input("Ingrese su edad: "))

if es_mayor(edad):
    print("Es mayor de edad")
else:
    print("Es menor de edad")

# precio final (precio, descuento=10%) * devolver el precio con descuento

def precio_final(precio, descuento=10):
    return precio - (precio * descuento / 100)

precio = float(input("Ingrese el precio: "))
descuento = float(input("Ingrese el descuento: "))

# Si coloco el descuento despues del precio tomará el que coloquemos, sino el que está por defecto arriba

resultado = precio_final(precio, descuento)

print("El precio final es:", resultado)

# promedio a b c

def promedio(a, b, c):
    return (a + b + c) / 3

nota1 = float(input("Ingrese la primera nota: "))
nota2 = float(input("Ingrese la segunda nota: "))
nota3 = float(input("Ingrese la tercera nota: "))

resultado = promedio(nota1, nota2, nota3)

print("El promedio es:", resultado)

if resultado >= 61:
    print("Aprobó")
else:
    print("Reprobó")

# Otra forma de promedio


def pedir_nota():
    return float(input("Nota: "))


def promedio(a, b, c):
    return (a + b + c) / 3


def mostrar(p):
    print("Promedio:", round(p, 2))

    if p >= 61:
        print("Aprobado")
    else:
        print("Reprobado")

# funcion import para importar un código de otro archivo

