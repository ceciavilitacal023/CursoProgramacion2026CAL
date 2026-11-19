
# Función para crear un objeto
class Estudiante:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def aprobo(self):
        return self.nota >= 61

    def mostrar(self):
        print(self.nombre, "-", self.nota)

    def subir(self, notaNueva):
        self.nota = self.nota + notaNueva
        if self.nota > 100:
            self.nota = 100


# Instancias de la clase
ana = Estudiante("Ana", 85)
luis = Estudiante("Luis", 58)
david = Estudiante("David", 50)

ana.subir(150)
ana.mostrar()

luis.subir(50)
luis.mostrar()


# 1
# Clase Producto con nombre, precio y stock; creen dos productos.

# 2
# Método mostrar(): «Arroz - Bs 8.5 - stock 20».

# 3
# Método vender(cantidad): resta del stock, o avisa
# «No hay suficiente».

# 4
# Método valor_total(): devuelve precio * stock.


class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    # Método para mostrar los datos
    def mostrar(self):
        print(self.nombre, "-", self.precio, "-", self.stock)

    # Método para vender productos
    def vender(self, cantidad):
        if cantidad <= self.stock:
            self.stock = self.stock - cantidad
            print("Venta realizada")
        else:
            print("No hay suficiente")

    # Método para calcular el valor total
    def valor_total(self):
        return self.precio * self.stock


# Crear dos productos
producto1 = Producto("Arroz", 10, 70)
producto2 = Producto("Papa", 100, 7)


# Mostrar productos
producto1.mostrar()
producto2.mostrar()

# Realizar ventas
producto1.vender(5)
producto2.vender(20)

# Mostrar stock actualizado
producto1.mostrar()
producto2.mostrar()

# Calcular valor total del stock
print("Valor total del arroz: Bs", producto1.valor_total())
print("Valor total del azucar: Bs", producto2.valor_total())