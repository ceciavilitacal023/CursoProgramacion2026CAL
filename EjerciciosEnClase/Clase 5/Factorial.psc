Algoritmo Factorial
	Definir n, i, factorial_ Como Entero
	Escribir "Ingrese un numero"
	Leer n
	factorial_ <- 1
	Para i <- 1 Hasta n Hacer
		factorial_ <- factorial_ * i
		Escribir "Multiplicacion por ", i, ": ", factorial_
	FinPara
	
	Escribir "El factorial es: ", factorial_
FinAlgoritmo