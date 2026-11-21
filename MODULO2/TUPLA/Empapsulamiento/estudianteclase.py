

#1
#Clase Estudiante con nombre y nota
#privados, y ver_nombre() y ver_nota().
#2
#cambiar_nota(nueva): solo acepta de 0 a 100;
#3
#aprobo() usando el atributo privado.
#4
#Prueben cambiar_nota(150) y print(e.__nota):


class Estudiante:
    def __init__(self, nombre, nota):
        self._nombre = nombre
        self._nota = nota
    def ver_nombre(self):
        return self._nombre
    def ver_nota(self):
        return self._nota

    def cambiar_nota(self, notaNueva):
        if notaNueva <0 or notaNueva >100:
            print("Nota invalida")
        else: 
            self._nota = notaNueva
    def aprobo (self):
        if self._nota >= 61:
            print("Aprobó")
        else: 
            print("Reprobó")
m = Estudiante("ana", 67)

print(m.ver_nombre(), m.ver_nota())

m.cambiar_nota(90)
print(m.ver_nombre(), m.ver_nota())

m.aprobo()