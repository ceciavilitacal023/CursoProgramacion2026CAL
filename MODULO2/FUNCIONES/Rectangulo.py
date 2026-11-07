

# 02
# Rectangulo
# rectangulo(ancho, alto) dibuja un rectangulo de asteriscos.

def rectangulo (ancho, alto):
     
    for fila in range (1, alto+1):
        if fila == 1 or fila == alto:
            print ("*" * ancho)
        else:
            print ("*" + " " * (ancho-2) + "*")
rectangulo (10,7)


#ancho + 5 y alto + 4

# *****
# *   *
# *   *
# *****