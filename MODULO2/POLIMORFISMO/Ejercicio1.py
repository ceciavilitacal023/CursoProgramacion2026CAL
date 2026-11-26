

# Esta clase esta definiendo que todas las clases hija deben tener la funcion area
class Figura:
    def area(self):
        return 0

class Rectangulo(Figura):
    def __init__(self, b, h):
        self.b = b
        self.h = h

    def area(self):
        return self.b * self.h

class Circulo(Figura):
    def __init__(self, r):
        self.r = r

    def area(self):
        return 3.14 * self.r * self.r

class Triangulo(Figura):
    def __init__(self, b, h):
        self.b = b
        self.h = h
    def area(self):
        return self.b * self.h / 2

figuras = [
    Rectangulo(3, 4),
    Circulo(2),
    Triangulo(5, 10)
]

for f in figuras:
    print(f.area())