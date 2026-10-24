

i = 1000

while i != 0:
    print(i)
    numero = int(input("Ingrese su gasto: "))

    if numero > i:
        print("No tienes esa cantidad de dinero")
    else:
        i = i - numero

print("Se le acabó su dinero")