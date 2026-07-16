---
fecha: 2026-07-09
bloque: 0
duracion: ~90 minutos
participantes:
  - Profesor
  - Ofelia (nueva)
  - Otros alumnos
recursos:
  - raw_transcript.txt (disponible en la misma carpeta)
---

# Resumen de la sesión de clase

**Contexto general:** Se introduce a Ofelia (nueva estudiante con 3 años de experiencia en software embebido automotriz en Sidec/Querétaro). Se revisan dos temas importantes del Bloque 0: **validación de entrada** usando ciclos (while/repetir) y **arreglos** (arrays) con sus operaciones de definición, dimensionamiento, llenado e iteración. Se enfatiza que los arreglos serán esenciales para la evaluación.

## Puntos principales

**1. Bienvenida a Ofelia (alumna nueva)**

Ofelia se presenta:
- Experiencia: 3 años en software embebido automotriz (código legacy, producción)
- Actualmente en **Sidec** (centro de investigación en Querétaro)
- Área anterior: diseño mecánico
- Motivación: profundizar en software para mayor oportunidad laboral
- Conexión: trabaja en la misma rama que el profesor (quien trabajó en Continental, que comparte raíz con Sidec)

El profesor recuerda que el curso inicia fácil pero la complejidad aumenta. Para la especialización **Vehículos**, el proyecto final será un **ECU con comunicación CAN** (muy complejo).

**2. Validación de entrada de datos (restricciones de tipo y rango)**

Se enseñó a validar que los datos recibidos cumplan restricciones antes de asignarlos a variables:

**Problema**: Una variable de tipo entero puede recibir valores inválidos (ej. edad negativa, división por cero) y causaría crash del programa o comportamiento incorrecto.

**Solución en pseudocódigo**: Usar ciclos **while** o **repetir** para re-preguntar si el valor está fuera de rango:

```pseudocodigo
Escribir "Ingresa tu edad"
Leer edad
Mientras edad < 0
    Escribir "Edad inválida, ingresa un número positivo"
    Leer edad
FinMientras
Escribir "Edad registrada: " edad
```

**Conceptos clave**:
- La validación se realiza con ciclos (en código real se usa try-catch/manejo de errores)
- El ciclo **while** revisa condición primero, luego ejecuta (equivale a `while` en C++)
- El ciclo **repetir** ejecuta primero, luego revisa condición (equivale a `do-while` en C++)
- Opción de validar rango simple (ej. edad ≥ 0) o más complejo (ej. 0 ≤ edad < 18 para bar)

**3. Introducción a arreglos (arrays)**

**Problema**: Si necesitas guardar 35 calificaciones, ¿declararías 35 variables diferentes? Ineficiente.

**Solución**: Usar un **arreglo** (array), que es una colección de valores del mismo tipo almacenados en posiciones indexadas.

**Definición y dimensionamiento en PSeInt**:
```pseudocodigo
Definir calificaciones Como Real
Dimensión calificaciones[5]
```

Esto crea un arreglo de 5 posiciones, cada una puede guardar un real (flotante o entero).

**Características de indexación**:
- PSeInt parece contar desde **1** (no desde 0 como en C++)
- Se accede con corchetes: `calificaciones[1]`, `calificaciones[2]`, etc.
- Se pueden llenar posiciones en cualquier orden (no secuencialmente)

**4. Llenado manual vs. automático con ciclos**

**Llenado manual** (ineficiente):
```pseudocodigo
calificaciones[1] <- 10
calificaciones[2] <- 9
calificaciones[3] <- 8
...
```

**Llenado automático con for** (eficiente):
```pseudocodigo
Para i <- 1 Hasta 5
    Escribir "Ingresa calificación ", i, ": "
    Leer calificaciones[i]
FinPara
```

**Lectura/impresión de arreglos**:
```pseudocodigo
Para i <- 1 Hasta 5
    Escribir "Calificación ", i, ": ", calificaciones[i]
FinPara
```

Nota: No se puede imprimir el arreglo completo de una vez (`Escribir calificaciones[i]` requiere índice específico).

**5. Validación dentro de ciclos de llenado**

Se pueden combinar ciclos con condicionales para validar cada entrada:
```pseudocodigo
Para i <- 1 Hasta 5
    Escribir "Ingresa calificación ", i, " (0-10): "
    Leer calificaciones[i]
    Mientras calificaciones[i] < 0 O calificaciones[i] > 10
        Escribir "Fuera de rango. Ingresa de nuevo: "
        Leer calificaciones[i]
    FinMientras
FinPara
```

**6. Operaciones comunes sobre arreglos**

Ejemplos mencionados:
- **Promedio**: Recorrer arreglo sumando valores, dividir entre cantidad
- **Búsqueda**: Pedir al usuario posición a consultar, retornar valor en esa posición
- **Edición**: Permitir modificar valor en posición específica

**7. Tarea del alumno**

Se propone crear un menú con operaciones sobre arreglos:
- **Agregar datos**: llenar posiciones del arreglo
- **Ver datos**: mostrar valores almacenados
- **Borrar datos**: limpiar posiciones
- **Editar datos**: modificar valores existentes

Debe combinar:
- Menú (ciclos, condicionales - visto en clase anterior)
- Arreglos (nuevo)
- Validación (reciente)

## Siguiente paso

Los alumnos entregarán la tarea con menú de operaciones sobre arreglos. El lunes (próxima sesión) se revisarán resultados. Después se introducirán **funciones/subprocesos en PSeInt** (temas más avanzados del Bloque 0) antes de pasar a **Linux y C++** en Bloque 1.
