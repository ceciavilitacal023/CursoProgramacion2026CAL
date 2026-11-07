

def area_rectangulo (base, altura):
    print (base * altura)
    print ("La base es: ", base)
    print ("La altura es: ", altura)

def area_rectangulo_retorno (base, altura):
    return base*altura

area_rectangulo(45, 100)
resultado = area_rectangulo_retorno (45, 100)
print (resultado)

def saludar (nombre, apellido):
    print ("saludos ", nombre, apellido)
salida=saludar("Cecilia", "Avila")
print(salida)