

nota = int(input("Ingrese su nota: "))

if nota < 0 or nota > 100:
    print("Nota inválida")
elif nota >= 90:
    print("Estudiante excelente")
elif nota >= 61:
    print("Esa nota es de aprobado")
else:
    print("Esa nota es de reprobado")

print("Fin")