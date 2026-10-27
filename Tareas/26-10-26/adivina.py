

secreto = 7
intentos = 0

while intentos < 5:
    
    numero = int(input("Adivina el numero secreto del 1 al 10: "))
    intentos = intentos + 1

    if numero == secreto:
        print("¡Correcto! Adivinaste el numero")
        break
    elif numero < secreto:
        print("Mas alto")
    else:
        print("Mas bajo")

if numero != secreto:
    print("Se acabaron los intentos")
    print("El numero secreto era:", secreto)