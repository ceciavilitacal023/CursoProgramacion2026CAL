


compra = float(input("Ingrese el monto de la compra en Bs: "))

if compra > 200 and compra > 0:
    descuento = compra * 0.10
    total = compra - descuento
    print("Tiene un descuento del 10%")
    print("El descuento es:", round(descuento, 2), "Bs")
    print("El total a pagar es:", round(total, 2), "Bs")
else:
    print("No tiene descuento")
    print("El total a pagar es:", compra, "Bs")