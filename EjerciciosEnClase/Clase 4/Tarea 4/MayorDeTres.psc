Algoritmo MayorDeTres
	Definir num1, num2, num3 Como Entero
	Escribir "Ingrese el numero 1"
	Leer num1
	Escribir "Ingrese el numero 2"
	Leer num2
	Escribir "Ingrese el numero 3"
	Leer num3
	Si num1 >= num2 Y num1 >= num3 Entonces
		Escribir "El mayor es:", num1
	SiNo
		Si num2 >= num1 Y num2 >= num3 Entonces
			Escribir "El mayor es:", num2
		SiNo
			Escribir "El mayor es:", num3
		FinSi
	FinSi
FinAlgoritmo