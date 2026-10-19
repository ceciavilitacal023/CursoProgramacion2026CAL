Algoritmo El_Vuelto
	Escribir "Ingrese el precio del producto"
	Leer precio
	Escribir "Ingrese con cuanto va a pagar"
	Leer pago
	Si precio = pago Entonces
		Escribir "No hay vuelto"
	SiNo
		Si precio < pago Entonces
			vuelto <- pago - precio
			Escribir "El vuelto es: ", vuelto
		SiNo
			Escribir "El pago es insuficiente"
		FinSi
	FinSi
FinAlgoritmo