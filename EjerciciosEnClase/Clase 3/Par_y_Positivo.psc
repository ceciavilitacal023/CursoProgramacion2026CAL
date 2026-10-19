Algoritmo Par_y_Positivo
	Definir numero Como Entero
	Definir estado Como Logico
	Escribir "Ingresa un numero"
	Leer numero
	estado <- numero MOD 2 = 0 Y numero > 0
	Escribir estado
	Si estado Entonces
		Escribir "El numero es par y positivo"
	SiNo
		Escribir "El numero no es par y positivo a la vez"
	FinSi
FinAlgoritmo
