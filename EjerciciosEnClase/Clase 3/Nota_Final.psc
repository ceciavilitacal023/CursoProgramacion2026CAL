Algoritmo Nota_Final
	Definir nota1, nota2, nota3 Como Entero
	Definir promedio, asistencia Como Real
	Escribir "Ingresa tus 3 notas"  
	Leer nota1
	Leer nota2
	Leer nota3
	Escribir "Ingresa tu asistencia"
	Leer asistencia
	promedio <- (nota1 + nota2 + nota3) / 3
	Si promedio >= 61 Y asistencia > 80 Entonces
		Escribir "aprobaste"
	Sino
		Escribir "reprobaste" 
	FinSi
FinAlgoritmo
