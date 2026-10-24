
#pedir 5 notas y contar cuantos son aprobados
aprobados = 0
reprobados = 0

for i in range (1, 6):
    nota = int(input("Ingrese una nota: "))
    if nota >= 61:
        aprobados = aprobados + 1
    else : 
        reprobados = reprobados + 1
print("Los aprobados son: ", aprobados)        
print("Los reprobados son: ", reprobados) 