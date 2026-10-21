
numero = int(input("Ingrese un numero de 3 cifras: "))

centena = numero // 100
decena = (numero % 100) // 10
unidad = numero % 10

invertido = unidad * 100 + decena * 10 + centena

print("El numero invertido es: ", invertido)