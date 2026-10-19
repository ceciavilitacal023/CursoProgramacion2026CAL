Algoritmo ElReloj
	Definir total, horas, minutos, segundos Como Entero
	Escribir "Ingresa la cantidad de segundos"
	Leer total
	horas <- (total - (total MOD 3600)) / 3600
	minutos <- (total - (horas * 3600) - (total MOD 60)) / 60
	segundos <- total - (horas * 3600) - (minutos * 60)
	Escribir horas, " horas"
	Escribir minutos, " minutos"
	Escribir segundos, " segundos"
FinAlgoritmo