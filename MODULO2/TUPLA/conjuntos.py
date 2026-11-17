

# Esto es un conjunto porque trabaja con {}

colores = {"rojo", "azul", "rojo"}
print(colores)  # {'rojo', 'azul'}

colores.add("verde")
colores.add("verde")
colores.add("verde")

print(colores[0])

print(len(colores))  # 3

print("azul" in colores)  # True