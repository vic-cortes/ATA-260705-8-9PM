Algoritmo MenuCalificaciones

	Dimension nombres[100]
	Dimension calificaciones[100]
	Definir cantidad, opcion, i, conteo Como Entero
	Definir suma, promedio, notaTemp Como Real
	Definir nombreTemp Como Cadena
	Definir valido Como Logico

	cantidad <- 0
	conteo <- 0

	Escribir "============================================"
	Escribir "   BIENVENIDO AL SISTEMA DE CALIFICACIONES"
	Escribir "============================================"
	Escribir ""

	Repetir
		Escribir ""
		Escribir "===== MENU DE CALIFICACIONES ====="
		Escribir "1. Registrar calificaciones"
		Escribir "2. Mostrar todas las calificaciones"
		Escribir "3. Calcular el promedio"
		Escribir "4. Salir"
		Escribir "Seleccione una opcion: "
		Leer opcion

		Segun opcion Hacer
			1:
				Si cantidad = 0 Entonces
					Escribir ""
					Escribir "Cuantas calificaciones desea registrar? "
					Leer cantidad

					Si cantidad <= 0 Entonces
						Escribir "ERROR: La cantidad debe ser mayor a 0. Intente de nuevo."
						cantidad <- 0
					SiNo
						Para i <- 1 Hasta cantidad Hacer
							Escribir "Ingrese el nombre del alumno ", i, ": "
							Leer nombreTemp
							nombres[i] <- nombreTemp
						FinPara
						Escribir ""
						Para i <- 1 Hasta cantidad Hacer
							valido <- Falso
							Mientras No valido Hacer
								Escribir "Ingrese la calificacion de ", nombres[i], " (0-10): "
								Leer notaTemp
								Si notaTemp >= 0 Y notaTemp <= 10 Entonces
									calificaciones[i] <- notaTemp
									valido <- Verdadero
								SiNo
									Escribir "ERROR: La calificacion debe estar entre 0 y 10. Intente de nuevo."
								FinSi
							FinMientras
						FinPara
						conteo <- cantidad
						Escribir ""
						Escribir "Calificaciones registradas correctamente."
					FinSi
				SiNo
					Escribir ""
					Escribir "AVISO: Las calificaciones ya fueron registradas."
					Escribir "No se puede registrar nuevamente."
				FinSi

			2:
				Si conteo = 0 Entonces
					Escribir ""
					Escribir "ERROR: No hay calificaciones registradas aun."
				SiNo
					Escribir ""
					Escribir "----- CALIFICACIONES REGISTRADAS -----"
					Para i <- 1 Hasta cantidad Hacer
						Escribir "Alumno ", i, " (", nombres[i], "): ", calificaciones[i]
					FinPara
				FinSi

			3:
				Si conteo = 0 Entonces
					Escribir ""
					Escribir "ERROR: No hay calificaciones registradas aun."
				SiNo
					suma <- 0
					Para i <- 1 Hasta cantidad Hacer
						suma <- suma + calificaciones[i]
					FinPara
					promedio <- suma / cantidad
					Escribir ""
					Escribir "----- ESTADISTICAS -----"
					Escribir "Total de alumnos: ", cantidad
					Escribir "Suma de calificaciones: ", suma
					Escribir "El promedio es: ", promedio
					Escribir ""
				FinSi

			4:
				Escribir ""
				Escribir "Gracias por usar el sistema. Hasta luego!"
				Escribir ""

			De Otro Modo:
				Escribir ""
				Escribir "ERROR: Opcion no valida. Debe seleccionar entre 1 y 4. Intente de nuevo."
				Escribir ""
		FinSegun

	Hasta Que opcion = 4

FinAlgoritmo
