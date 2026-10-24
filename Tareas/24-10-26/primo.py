

num = int(input("Ingrese un número: "))
divisores = 0
i = 1

while i <= num:
    if num % i == 0:
        print(i)
        divisores = divisores + 1

    i = i + 1

print("Cantidad de divisores:", divisores)

if divisores == 2:
    print("El número es primo")
else:
    print("El número no es primo")

print("Fin")