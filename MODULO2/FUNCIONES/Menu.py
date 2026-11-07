

# Menú ordenado
# Un menú donde cada opción llama a su propia función.

def op1():
    print ("Hola")

def op2():
    print("Como estoy")

def op3():
    print("Adios")

print("Ingrese un numero del 1 al 3")
usuario = int(input ("numero: "))
if usuario == 1:
    op1()
elif usuario == 2:
    op2()
else: 
    op3()
