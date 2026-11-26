


# Clase padre
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        return "..."

# Clases hijas
class Perro(Animal):
    def hablar(self):
        return "Guau Guau"


class Gato(Animal):
    def hablar(self):
        return "Miau Miau"


class Vaca(Animal):
    def hablar(self):
        return "Muuuuuuu"


class Pato(Animal):
    def hablar(self):
        return "Cuac Cuac"


# Lista con un animal de cada tipo
animales = [
    Perro("Firulais"),
    Gato("Michi"),
    Vaca("Lola")
]

# Agregamos un pato sin modificar el FOR
animales.append(Pato("Donald"))

# Mostrar los animales
for animal in animales:
    print(f"{animal.nombre} dice {animal.hablar()}")