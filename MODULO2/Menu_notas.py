
# REGISTRO DE NOTAS
# 1. Agregar(lista)
# 2. Mostrar(lista)
# 3. Estadisticas(lista)
# 4. Buscar(lista, nombre)
# 0. Salir

# Funcion para agregar estudiantes
def agregar(lista):
    nombre = input("Ingrese el nombre: ")
    nota = float(input("Ingrese la nota: "))

    lista.append({"Nombre": nombre, "Nota": nota})
    print("Estudiante agregado correctamente")


# Funcion para mostrar estudiantes
def mostrar(lista):
    if len(lista) == 0:
        print("Lista vacia")
    else:
        for est in lista:
            print(est["Nombre"], "=", est["Nota"])


# Funcion para calcular el promedio
def promedio(lista):
    total = 0
    for est in lista:
        total = total + est["Nota"]
    return total / len(lista)


# Funcion para contar los aprobados
def aprobados(lista):
    total = 0
    for est in lista:
        if est["Nota"] >= 61:
            total = total + 1
    return total

# Funcion para contar los reprobados
def reprobados(lista):
    total = 0
    for est in lista:
        if est["Nota"] < 61:
            total = total + 1
    return total

# Funcion para encontrar al mejor estudiante
def mejor(lista):
    el_mejor = lista[0]
    for est in lista:
        if est["Nota"] > el_mejor["Nota"]:
            el_mejor = est
    return el_mejor


# Funcion para buscar un estudiante
def buscar(lista, nombre):
    for est in lista:
        if est["Nombre"].lower() == nombre.lower():
            return est

    return None


# Variables iniciales
estudiantes = [
    {"Nombre": "David", "Nota": 46},
    {"Nombre": "Adrian", "Nota": 99},
    {"Nombre": "Maria", "Nota": 67}
]
opcion = ""

# Menu principal
while opcion != "0":

    print("\n=== REGISTRO DE NOTAS ===")
    print("1. Agregar  2. Mostrar")
    print("3. Estadisticas  4. Buscar")
    print("0. Salir")

    opcion = input("Opcion: ")

    if opcion == "0":
        print("Hasta luego")

    elif opcion == "1":
        agregar(estudiantes)

    elif opcion == "2":
        mostrar(estudiantes)

    elif opcion == "3":
        if len(estudiantes) == 0:
            print("No hay estudiantes para sacar estadisticas")
        else:
            print("El promedio es:", promedio(estudiantes))
            print("Aprobados son:", aprobados(estudiantes))
            print("Reprobados son:", reprobados(estudiantes))

            m = mejor(estudiantes)

            print("El mejor es:", m["Nombre"],
              "con la nota:", m["Nota"])

    elif opcion == "4":
        nombre = input("Ingrese el estudiante que quiere buscar: ")

        e = buscar(estudiantes, nombre)

        if e == None:
            print("Ese estudiante no existe")
        else:
            print("El estudiante es:", e["Nombre"],
                  "con la nota de:", e["Nota"])

    else:
        print("Opcion no valida")


print("Fin")


