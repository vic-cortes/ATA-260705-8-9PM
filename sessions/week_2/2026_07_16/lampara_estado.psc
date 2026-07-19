Algoritmo MaquinaEstadosLampara
	Definir estado Como Entero
	Definir boton Como Entero
	Definir salir Como Logico
	
	estado <- 0
	salir <- Falso
	
	// Estado 0 = Apagada
	// Estado 1 = Encendida
	
	Mientras salir = Falso Hacer
		Escribir ""
		Escribir "Estado actual:"
		
		Segun estado Hacer
			0:
				Escribir "L�mpara APAGADA"
			1:
				Escribir "L�mpara ENCENDIDA"
		FinSegun
		
		Escribir "Presiona 1 para simular bot�n"
		Escribir "Presiona 2 para salir"
		Leer boton
		
		Segun boton Hacer
			1:
				Si estado = 0 Entonces
					estado <- 1
				SiNo
					estado <- 0
				FinSi
				
			2:
				salir <- Verdadero
				
			De Otro Modo:
				Escribir "Opci�n inv�lida"
		FinSegun
	FinMientras
	
	Escribir "Programa terminado"
FinAlgoritmo