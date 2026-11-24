
class Personas:
    # Constructor
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def presentarse(self):
        print("Soy", self.nombre, "y tengo", self.edad, "años")


# Clase Estudiante que hereda de Personas
class Estudiante(Personas):
    def __init__(self, nombre, edad, carrera, nota):
        super().__init__(nombre, edad)

        self.carrera = carrera
        self.nota = nota

    def presentarse(self):
        super().presentarse()
        print("Estudio la carrera de", self.carrera)
        print("Mi nota es", self.nota)


# Clase Docente que hereda de Personas
class Docente(Personas):
    def __init__(self, nombre, edad, materia):
        super().__init__(nombre, edad)

        self.materia = materia

    def presentarse(self):
        super().presentarse()
        print("Enseño", self.materia)


# Crear objetos
e = Estudiante("Pedro", 18, "Sistemas", 85)
e.presentarse()

print("--------------------")

d = Docente("Maria", 35, "Programación")
d.presentarse()

print("--------------------")

p = Personas("Juan", 21)
p.presentarse()