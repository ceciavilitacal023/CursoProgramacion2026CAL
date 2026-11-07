

# El mayor
# mayor (a,b) muestra cual de los dos numeros es mayor, o si son iguales

def mayor_retorno(a, b):
    if a > b:
        return a
    elif a==b:
        return 0
    else:
        return b

print(mayor_retorno(8,9))
print(mayor_retorno(1,1))
print(mayor_retorno(10,7))

