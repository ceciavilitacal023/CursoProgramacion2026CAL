Algoritmo PiedraPapelTijera
	Definir jugador1, jugador2 Como Entero
	Escribir "------JUGUEMOS PIEDRA, PAPEL O TIJERA-----"
	Escribir "1. Piedra"
	Escribir "2. Tijera"
	Escribir "3. Papel"
	Escribir "Ingrese la jugada del jugador 1"
	Leer jugador1
	Escribir "Ingrese la jugada del jugador 2"
	Leer jugador2
	Si jugador1 = jugador2 Entonces
		Escribir "Hay empate"
	SiNo
		Si jugador1 = 1 Y jugador2 = 2 Entonces
			Escribir "Gana el jugador 1"
		SiNo
			Si jugador1 = 2 Y jugador2 = 3 Entonces
				Escribir "Gana el jugador 1"
			SiNo
				Si jugador1 = 3 Y jugador2 = 1 Entonces
					Escribir "Gana el jugador 1"
				SiNo
					Escribir "Gana el jugador 2"
				FinSi
			FinSi
		FinSi
	FinSi
FinAlgoritmo