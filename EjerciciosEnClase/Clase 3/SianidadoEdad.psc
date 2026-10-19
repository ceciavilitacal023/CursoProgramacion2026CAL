Algoritmo Sianidado
	//Leer la edad y decir si es niño menor de 12, adolecente (2 a 17) yo adulto
	Definir edad Como Entero
	Escribir "Ingrese la edad"
	Leer edad
	Si edad >= 12  Y edad <= 17 Entonces
		Escribir "Adolecente"
	SiNo
		Si edad < 12 Entonces
			Escribir "Niño"
		SiNo
			Escribir "Adulto"
		Fin Si
	FinSi
FinAlgoritmo