Algoritmo AdivinaElNumero
	Definir numero Como Entero
	numero <- 0
	Mientras numero <> 7 Hacer
		Escribir "Adivina el numero secreto"
		Leer numero
		Si numero < 7 Entonces
			Escribir "Mas alto"
		SiNo
			Si numero > 7 Entonces
				Escribir "Mas bajo"
			SiNo
				Escribir "Correcto, adivinaste"
			FinSi
		FinSi
	FinMientras
FinAlgoritmo