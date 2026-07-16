---
fecha: 2026-07-08
bloque: 0 (transición)
duracion: ~120 minutos
participantes:
  - Profesor
  - Ismael
  - Arturo
  - Alejandro
  - Carlos
  - Fernando
  - Juan Cocosin
  - Juan Solís
  - Otros alumnos
recursos:
  - raw_transcript.txt (disponible en la misma carpeta)
  - PSeInt IDE (online)
  - Visual Studio Code con extensión de pseudocódigo (mencionada)
---

# Resumen de la sesión de clase

**Contexto general:** El profesor repasa estructuras de pseudocódigo en PSeInt, enfocándose en temas más complejos (condicionales, ciclos, menús) antes de la evaluación del Bloque 0. Adicionalmente, aclara diferencias entre C y C++, aclarando que el curso usará C++ directamente, no C plano.

## Puntos principales

**1. Repaso de pensamiento algorítmico y estructura de código**
Se revisaron los pasos fundamentales: definición de variables, entrada de datos, procesamiento y salida. El profesor enfatizó la importancia de la indentación correcta en PSeInt para evitar errores.

**2. Tipos de datos en PSeInt**
- Entero (int)
- Real/Double (para números decimales)
- Carácter (char)
- Cadena (string)

Se mostró que el orden importa: agrupar variables del mismo tipo en líneas consecutivas es buena práctica.

**3. Comandos básicos**
- `Escribir` — imprime texto/variables en consola
- `Leer` — espera entrada del usuario y asigna a variable
- `<-` o `=` — asignación de valores
- Uso de comas para concatenar strings con variables en `Escribir`

**4. Ejemplo 1: Suma de números**
Se codificó un programa que suma dos números. Se mostró que tanto `<-` como `=` funcionan para asignaciones. Se demostró ejecución con valores flotantes (reales).

**5. Ejemplo 2: Concatenación de strings**
Se creó un algoritmo que recibe nombre y edad, luego imprime un saludo formateado. Se destacó la importancia de los espacios en strings y el uso de comas para mezclar texto con variables.

**6. Condicionales: Si/FinSi**
Se mostró un algoritmo de calificaciones que verifica si un alumno aprobó (≥70) o reprobó usando estructura Si/FinSi. Se enfatizó la indentación dentro de las condicionales.

**7. Menús con Según/FinSegún (aporte clave)**
Se construyó un menú interactivo con 4 opciones:
- Opción 1: Saludo
- Opción 2: Suma de dos números
- Opción 3: Resta de dos números
- Opción 4: Salir
Se mostró el uso de `Según` para evaluar múltiples casos y `De otro modo` para manejar opciones inválidas.

**8. Ciclos: Mientras/FinMientras (aporte de Ismael)**
Ismael sugirió agregar un ciclo `Mientras` para que el menú se repita hasta que el usuario elija salir. Se refactorizó el código para:
- Usar una variable booleana (Verdadero/Falso)
- Mover el menú adentro del ciclo
- Establecer condiciones de salida

Se mostró la ejecución exitosa con múltiples iteraciones.

**9. Diferencias entre C y C++ (aporte de Arturo)**
Arturo preguntó sobre el lenguaje a usar. El profesor aclaró:
- **C**: Estructurado, requiere archivos .c y .h (headers), compilación a objeto antes de ejecución
- **C++**: Orientado a objetos, archivos .cpp, compilación directa a ejecutable, más modular
- Se enseñará **C++ directamente**, no C plano
- La diferencia es "grande aunque sea solo una o dos palabras"
- Se mencionó Make para compilación en algún momento

**10. Evaluación del Bloque 0**
- Será pseudocódigo complejo en PSeInt
- Probablemente en equipos de 2 personas
- Requiere grabar un video explicando el código
- Se evaluará: limpieza del código, optimización, orden
- Necesitarán crear un diagrama de flujo (como "arquitectura" básica)
- Recomendación: usar PSeInt IDE para escribir

**11. Plan futuro**
- Cierre próximo del Bloque 0 con evaluación
- Instalación de Linux y comandos básicos
- Transición a Bloque 1: **C++ básico**
- El profesor ya enseña C++ a otros grupos

**12. Herramientas mencionadas**
- PSeInt IDE (instalado y funcional)
- Visual Studio Code con extensión de pseudocódigo (sugerida, pendiente revisar)

## Siguiente paso

La evaluación del Bloque 0 es inminente. Estudiantes deben:
1. Practicar menús y ciclos en PSeInt
2. Asegurarse de que el código esté limpio y bien indentado
3. Prepararse para grabar un video explicando su pseudocódigo
4. Crear un diagrama de flujo de su algoritmo
5. Tras evaluación: prepararse para Linux y luego C++

## Notas adicionales

- El profesor está "oxidado" con PSeInt (hace años no lo usa)
- Se cometieron errores durante la codificación en vivo (falta de lectura de variable), pero fueron corregidos
- Se enfatizó que los errores son normales en entrevistas/presentaciones
- La sesión fue práctica: mostró problemas comunes y cómo resolverlos
