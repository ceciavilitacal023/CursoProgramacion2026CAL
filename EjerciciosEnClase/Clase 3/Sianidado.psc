Algoritmo Sianidado
	//Tenemos que determinar >= 90 es excelente
	//Si  61 aprobado
	// es < 61 reprobado
	Definir nota Como Entero
	Escribir "Ingrese su nota"
	Leer nota
	Si nota >= 90 Entonces
		Escribir "Excelente"
	SiNo
		Si nota >= 61 Entonces
			Escribir "Aprobado"
		SiNo
			Escribir "Reprobado"
		Fin Si
	Fin Si
FinAlgoritmo
