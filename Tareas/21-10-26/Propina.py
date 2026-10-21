

TotalCuenta = float(input("Ingrese el monto de la cuenta: "))
porcentaje = float(input("Ingrese el porcentaje de propina en %: "))

propina = TotalCuenta * porcentaje / 100
total = TotalCuenta + propina

print("La propina es: ", propina)
print("El total a pagar es: ", total)
print("Muchas gracias")