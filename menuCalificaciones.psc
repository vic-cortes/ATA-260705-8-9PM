Algoritmo MenuCalificaciones

	Dimension nombres[100]
	Dimension calificaciones[100]
	Definir cantidad, opcion, i Como Entero
	Definir suma, promedio, notaTemp Como Real
	Definir nombreTemp Como Cadena

	cantidad <- 0

	Repetir
		Escribir ""
		Escribir "===== MENU DE CALIFICACIONES ====="
		Escribir "1. Registrar alumnos"
		Escribir "2. Registrar calificaciones"
		Escribir "3. Mostrar todas las calificaciones"
		Escribir "4. Calcular el promedio"
		Escribir "5. Salir"
		Escribir "Seleccione una opcion: "
		Leer opcion

		Segun opcion Hacer
			1:
				Escribir "Cuantos alumnos desea registrar? "
				Leer cantidad
				Para i <- 1 Hasta cantidad Hacer
					Escribir "Ingrese el nombre del alumno ", i, ": "
					Leer nombreTemp
					nombres[i] <- nombreTemp
				FinPara
				Escribir "Alumnos registrados correctamente."
			2:
				Si cantidad = 0 Entonces
					Escribir "Primero debe registrar a los alumnos (opcion 1)."
				SiNo
					Para i <- 1 Hasta cantidad Hacer
						Escribir "Ingrese la calificacion de ", nombres[i], ": "
						Leer notaTemp
						calificaciones[i] <- notaTemp
					FinPara
					Escribir "Calificaciones registradas correctamente."
				FinSi
			3:
				Si cantidad = 0 Entonces
					Escribir "No hay alumnos registrados."
				SiNo
					Escribir "----- CALIFICACIONES -----"
					Para i <- 1 Hasta cantidad Hacer
						Escribir "Alumno ", i, " (", nombres[i], "): ", calificaciones[i]
					FinPara
				FinSi
			4:
				Si cantidad = 0 Entonces
					Escribir "No hay calificaciones registradas."
				SiNo
					suma <- 0
					Para i <- 1 Hasta cantidad Hacer
						suma <- suma + calificaciones[i]
					FinPara
					promedio <- suma / cantidad
					Escribir "El promedio es: ", promedio
				FinSi
			5:
				Escribir "Saliendo del programa..."
			De Otro Modo:
				Escribir "Opcion no valida. Intente de nuevo."
		FinSegun

	Hasta Que opcion = 5

FinAlgoritmo
