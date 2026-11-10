

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