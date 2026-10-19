Algoritmo Sianidado
	//Tenemos que determinar >= 90 es excelente
	//Si  61 aprobado
	// es < 61 reprobado
	Definir nota Como Entero
	Escribir "Ingrese su nota"
	Leer nota
	Si nota < 90 Y nota >= 61 Entonces
		Escribir "Aprobado"
	SiNo
		Si nota < 61 Entonces
			Escribir "Reprobado"
		SiNo
			Escribir "Excelente"
		Fin Si
	FinSi
FinAlgoritmo
