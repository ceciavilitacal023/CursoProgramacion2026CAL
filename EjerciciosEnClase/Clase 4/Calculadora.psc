Algoritmo Calculadora
	Definir opc, num1, num2 Como Entero
	Definir resultado Como Real
	Escribir "======Calculadora======"
	Escribir "1. Sumar"
	Escribir "2. Restar"
	Escribir "3. Multiplicar"
	Escribir "4. Dividir"
	Leer opc
	Segun opc Hacer
		1: 
			Escribir "+++++SUMA+++++"
			Escribir "Ingrese el primer numero"
			Leer num1 
			Escribir "Ingrese el segundo numer	"
			Leer num2
			resultado <- num1 + num2
			Escribir "Su resultado de la suma es:", resultado
		2:
			Escribir "+++++RESTA+++++"
			Escribir "Ingrese el primer numero"
			Leer num1 
			Escribir "Ingrese el segundo numer	"
			Leer num2
			resultado <- num1 - num2
			Escribir "Su resultado de la resta es:", resultado
		3:
			Escribir "+++++MULTIPLICAR+++++"
			Escribir "Ingrese el primer numero"
			Leer num1 
			Escribir "Ingrese el segundo numer	"
			Leer num2
			resultado <- num1 * num2
			Escribir "Su resultado de la multiplicacion es:", resultado
		4:
			Escribir "+++++DIVISION+++++"
			Escribir "Ingrese el primer numero"
			Leer num1 
			Si num1 = 0 Entonces
				Escribir "No se puede dividir"
			SiNo
				Escribir "Ingrese el segundo numer	"
				Leer num2
				resultado <- num1 / num2
				Escribir "Su resultado de la division es:", resultado
			FinSi
			
			
		De Otro Modo:
			Escribir "Esa opcion no existe "
	FinSegun
FinAlgoritmo
