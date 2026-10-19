Algoritmo AnioBisiesto
	Definir anio Como Entero
	Definir estado Como Logico
	Escribir "Ingresa un anio"
	Leer anio
	estado <- (anio MOD 4 = 0 Y anio MOD 100 <> 0) O anio MOD 400 = 0
	Escribir estado
	Si estado Entonces
		Escribir "El anio es bisiesto"
	SiNo
		Escribir "El anio no es bisiesto"
	FinSi
FinAlgoritmo