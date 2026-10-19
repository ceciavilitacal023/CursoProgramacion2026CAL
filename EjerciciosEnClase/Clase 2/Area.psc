Algoritmo Area
	Escribir "Hola"
	Escribir "Ingrese la base del rectangulo"
	Leer base
	Escribir "Ingrese la altura del rectangulo"
	Leer altura
	area_total <- base * altura
	Escribir "El area es: ", area_total
	Si base = altura Entonces
		Escribir "Es un cuadrado"
	SiNo
		Escribir "Es un rectangulo"
	FinSi
FinAlgoritmo