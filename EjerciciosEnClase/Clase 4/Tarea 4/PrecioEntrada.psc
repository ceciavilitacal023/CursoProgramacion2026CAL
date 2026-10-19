Algoritmo PrecioEntrada
	Definir edad, dia Como Entero
	Definir precio Como Real
	Escribir "Ingrese su edad"
	Leer edad
	Escribir "Ingrese el dia de la semana del 1 al 7"
	Leer dia
	Si dia >= 1 Y dia <= 7 Entonces
		Escribir "Dia valido"
	SiNo
		Escribir "Error: Ingrese nuevamente el dia de la semana del 1 al 7"
	FinSi
	Leer dia
	Si edad < 12 Y dia = 2 Entonces
		precio <- 5
	SiNo
		Si edad < 12 Entonces
			precio <- 10
		SiNo
			Si dia = 2 Entonces
				precio <- 10
			SiNo
				precio <- 20
			FinSi
		FinSi
	FinSi
	Escribir "El precio de la entrada es: ", precio, " Bs"
FinAlgoritmo