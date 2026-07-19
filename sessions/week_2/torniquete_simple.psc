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
		Escribir "Estado: "
		
		Segun estado Hacer
			0:
				Escribir "BLOQUEADO"
			1:
				Escribir "DESBLOQUEADO"
		FinSegun
		
		Escribir "Contador: " contador
		Escribir "1=Moneda, 2=Empujar, 0=Salir"
		Leer evento

		Segun evento Hacer
			1:
				Segun estado Hacer
					0:
						Escribir "Desbloqueado"
						estado <- 1
					1:
						Escribir "Ya esta desbloqueado"
				FinSegun
			2:
				Segun estado Hacer
					0:
						Escribir "Acceso denegado"
					1:
						contador <- contador + 1
						Escribir "Paso " contador " registrado"
						estado <- 0
				FinSegun
			0:
				salir <- Verdadero
			De Otro Modo:
				Escribir "Evento invalido"
		FinSegun

	FinMientras

	Escribir ""
	Escribir "Total personas: " contador

FinAlgoritmo
