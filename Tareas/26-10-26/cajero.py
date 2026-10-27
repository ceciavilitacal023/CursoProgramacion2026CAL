

monto = int(input("Ingrese el monto a retirar en Bs: "))

if monto <= 0:
    print("El monto debe ser mayor que cero")
elif monto % 10 != 0:
    print("El monto debe ser multiplo de 10")
else:
    billetes200 = monto // 200
    monto = monto % 200

    billetes100 = monto // 100
    monto = monto % 100

    billetes50 = monto // 50
    monto = monto % 50

    billetes20 = monto // 20
    monto = monto % 20

    billetes10 = monto // 10

    print("Billetes de 200 Bs:", billetes200)
    print("Billetes de 100 Bs:", billetes100)
    print("Billetes de 50 Bs:", billetes50)
    print("Billetes de 20 Bs:", billetes20)
    print("Billetes de 10 Bs:", billetes10)