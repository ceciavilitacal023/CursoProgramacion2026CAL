

radio = float(input("Ingrese el radio del círculo: "))

while radio <= 0:
    print("El radio debe ser mayor que cero")
    radio = float(input("Ingrese el radio del círculo: "))

area = 3.1416 * radio ** 2

print("El área del círculo es:", area)