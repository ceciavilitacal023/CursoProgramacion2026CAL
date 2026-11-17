

# Ejercicio 2: Funciones y tuplas

def suma_y_promedio(lista):
    suma = sum(lista)
    promedio = suma / len(lista)

    return suma, promedio


numeros = [5, 10, 15, 20]

resultado = suma_y_promedio(numeros)

print("Suma:", resultado[0])
print("Promedio:", resultado[1])