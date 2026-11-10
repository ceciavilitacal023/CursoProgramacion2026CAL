

def esPar(n):
    return n % 2 == 0

def doble(n):
    return n * 2

print(esPar(2))
print(esPar(21))

# -- Que se puede hacer con lo que retorna
# Guardar
guardar = esPar(90)

# Podemos imprimir

print (esPar(21))

if esPar(8):
    print ("Es par")
else:
    print ("Es impar")