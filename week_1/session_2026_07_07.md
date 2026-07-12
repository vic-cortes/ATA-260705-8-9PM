# Resumen de la sesión de clase

**Contexto general:** El profesor retoma el curso (aparentemente sustituyendo a otra profesora) y dedica la clase a hacer un diagnóstico de hasta dónde llegaron los alumnos en el **Bloque 0** del curso, antes de avanzar al Bloque 1 (introducción a C).

## Puntos principales

**1. Diagnóstico y evaluación pendiente**
El profesor explica que antes de pasar al Bloque 1 deben evaluar el Bloque 0 con un **proyecto final** (un pseudocódigo más elaborado que se entrega en Classroom). Menciona que probablemente trabajen en equipos de 2-3 personas y que este proyecto se irá complementando en bloques posteriores hasta volverse un sistema robusto y escalable.

**2. Repaso de pensamiento algorítmico**
Se revisó la lógica de separar un problema en partes antes de codificar:
- **Entradas** (qué datos necesito)
- **Proceso** (qué operación debo realizar)
- **Salida** (qué debo entregar como resultado)

Se usó como ejemplo un programa de tres calificaciones que calcula un promedio y determina si el alumno aprobó (≥70) o reprobó, mostrando cómo declarar variables (tipo real/float), leer valores y aplicar condicionales con **descarte** (usar "si no" en vez de evaluar todas las condiciones).

**3. Memoria y punteros**
Se abordó brevemente qué es un bit y la jerarquía de unidades de memoria. Ismael preguntó sobre punteros en C, lo que llevó a una explicación conceptual (se pospone una explicación gráfica más completa para después), destacando su utilidad para controlar dónde se almacenan los datos, algo relevante en código de producción/embebido.

**4. Optimización de condicionales (aporte de Arturo)**
Arturo, con experiencia en la industria automotriz (C++), preguntó si el orden de los IFs importa en producción. El profesor confirmó que sí, y usó un ejemplo de sistema anticolisión (radar + cámara detectando personas/animales) para mostrar cómo agrupar condiciones reduce la complejidad del código, especialmente en sistemas embebidos donde el costo de ejecución importa.

**5. Ejercicio: positivo/negativo/cero**
Se resolvió un pseudocódigo para clasificar un número entero. Surgió un debate interesante entre usar descarte (if/else encadenado) vs. condiciones explícitas para cada caso (propuesta de Ismael), concluyendo que la elección depende de qué tan legible necesite ser el código para otras personas que lo revisen (buenas prácticas, documentación).

**6. Importancia de planear antes de programar**
Cierre reflexivo sobre por qué planear ahorra tiempo a largo plazo: recolección de requerimientos, análisis de riesgos y definición de pruebas. Arturo añadió que, con el auge de los LLMs, ahora se invierte más tiempo en planeación/prototipado que en la codificación misma, lo cual el profesor confirmó.

## Siguiente paso
El profesor cerrará el Bloque 0 pronto y aplicará el proyecto de evaluación (con posible trabajo en equipo), para después avanzar rápidamente al Bloque 1 (C).