
fecha = (15, 10, 2026)

print(fecha)

print(fecha[0])
print(fecha[2])

fecha = (13, 11, 2023)
dia, mes, anio = fecha

print(mes)  # 11
print(fecha[1])

def extremos(lista):
    return min(lista), max(lista)

a, b = extremos([15, 8, 30, 4, 20])

print("Minimo:", a)
print("Maximo:", b)
