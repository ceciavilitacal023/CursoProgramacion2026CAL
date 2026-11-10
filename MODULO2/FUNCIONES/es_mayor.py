

def es_mayor(edad):
    return edad >= 18

edad = int(input("Ingrese su edad: "))

if es_mayor(edad):
    print("Es mayor de edad")
else:
    print("Es menor de edad")