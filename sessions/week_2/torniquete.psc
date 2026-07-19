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
		
		Segun estado Hacer
			0:
				Escribir "BLOQUEADO"
			1:
				Escribir "DESBLOQUEADO"
		FinSegun

		Escribir "Pasos registrados: " contador_pasos
		Escribir ""
		Escribir "Eventos disponibles:"
		Escribir "1 = Insertar moneda"
		Escribir "2 = Empujar torniquete"
		Escribir "0 = Salir"
		Escribir ""
		Escribir "Ingresa evento: "
		Leer evento

		Segun evento Hacer
			1:
				Segun estado Hacer
					0:
						Escribir "Moneda insertada"
						Escribir "Torniquete DESBLOQUEADO - Puedes pasar"
						estado <- 1
					1:
						Escribir "Ya esta desbloqueado"
				FinSegun

			2:
				Segun estado Hacer
					0:
						Escribir "ACCESO DENEGADO"
						Escribir "El torniquete esta bloqueado"
						Escribir "Inserta una moneda para desbloquear"
					1:
						Escribir "Paso registrado"
						contador_pasos <- contador_pasos + 1
						Escribir "Persona " contador_pasos " paso"
						Escribir "Torniquete BLOQUEADO nuevamente"
						estado <- 0
				FinSegun

			0:
				salir <- Verdadero
				Escribir "Programa terminado"

			De Otro Modo:
				Escribir "Evento invalido"
		FinSegun

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
