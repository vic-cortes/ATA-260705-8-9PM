Algoritmo Torniquete_Simple

	Definir estado Como Entero
	Definir evento Como Entero
	Definir salir Como Logico
	Definir contador Como Entero

	estado <- 0
	salir <- Falso
	contador <- 0

	Mientras salir = Falso Hacer

		Escribir ""
		Si estado = 0 Entonces
			Escribir "ESTADO: BLOQUEADO"
		Sino
			Escribir "ESTADO: DESBLOQUEADO"
		FinSi
		Escribir "Contador: " contador

		Escribir "1=Moneda, 2=Empujar, 0=Salir"
		Leer evento

		// ESTADO BLOQUEADO
		Si estado = 0 Entonces
			Si evento = 1 Entonces
				Escribir "Desbloqueado"
				estado <- 1
			FinSi
			Si evento = 2 Entonces
				Escribir "Acceso denegado"
			FinSi
			Si evento = 0 Entonces
				salir <- Verdadero
			FinSi
		FinSi

		// ESTADO DESBLOQUEADO
		Si estado = 1 Entonces
			Si evento = 2 Entonces
				contador <- contador + 1
				Escribir "Paso " contador " registrado"
				estado <- 0
			FinSi
			Si evento = 1 Entonces
				Escribir "Ya esta desbloqueado"
			FinSi
			Si evento = 0 Entonces
				salir <- Verdadero
			FinSi
		FinSi

	FinMientras

	Escribir ""
	Escribir "Total personas: " contador

FinAlgoritmo
