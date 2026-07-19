Algoritmo Torniquete

	Definir estado Como Entero
	Definir evento Como Entero
	Definir salir Como Logico
	Definir contador_pasos Como Entero

	estado <- 0
	salir <- Falso
	contador_pasos <- 0

	// Estado 0 = Bloqueado
	// Estado 1 = Desbloqueado
	// Evento 1 = Moneda
	// Evento 2 = Empujar

	Escribir "MAQUINA DE ESTADOS: TORNIQUETE"

	Mientras salir = Falso Hacer

		Escribir ""
		Escribir "Estado actual:"
		
		Si estado = 0 Entonces
			Escribir "BLOQUEADO"
		Sino
			Escribir "DESBLOQUEADO"
		FinSi

		Escribir "Pasos registrados: " contador_pasos
		Escribir ""
		Escribir "Eventos disponibles:"
		Escribir "1 = Insertar moneda"
		Escribir "2 = Empujar torniquete"
		Escribir "0 = Salir"
		Escribir ""
		Escribir "Ingresa evento: "
		Leer evento

		// ESTADO 0: BLOQUEADO
		Si estado = 0 Entonces
			Si evento = 1 Entonces
				Escribir "Moneda insertada"
				Escribir "Torniquete DESBLOQUEADO - Puedes pasar"
				estado <- 1
			FinSi
			
			Si evento = 2 Entonces
				Escribir "ACCESO DENEGADO"
				Escribir "El torniquete esta bloqueado"
				Escribir "Inserta una moneda para desbloquear"
			FinSi
			
			Si evento = 0 Entonces
				salir <- Verdadero
				Escribir "Programa terminado"
			FinSi
		FinSi

		// ESTADO 1: DESBLOQUEADO
		Si estado = 1 Entonces
			Si evento = 2 Entonces
				Escribir "Paso registrado"
				contador_pasos <- contador_pasos + 1
				Escribir "Persona " contador_pasos " paso"
				Escribir "Torniquete BLOQUEADO nuevamente"
				estado <- 0
			FinSi
			
			Si evento = 1 Entonces
				Escribir "Ya esta desbloqueado"
			FinSi
			
			Si evento = 0 Entonces
				salir <- Verdadero
				Escribir "Programa terminado"
			FinSi
		FinSi

		Escribir ""

	FinMientras

	Escribir ""
	Escribir "RESUMEN FINAL"
	Escribir "Total personas que pasaron: " contador_pasos
	Si estado = 0 Entonces
		Escribir "Estado final: BLOQUEADO"
	Sino
		Escribir "Estado final: DESBLOQUEADO"
	FinSi

FinAlgoritmo
