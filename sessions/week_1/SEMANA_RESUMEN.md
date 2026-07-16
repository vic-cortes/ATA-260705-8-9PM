---
semana: 1
fechas: 2026-07-06 a 2026-07-09
bloque: 0
duracion_total: ~390 minutos (6.5 horas)
sesiones: 4
participantes_base:
  - Profesor Óscar Godíz
  - Víctor Cortés
  - Ismael
  - Arturo
  - Carlos Caravantes
  - Alejandro Coronado
  - Juan Anuel
  - Fernando Gutiérrez
  - Edweni
  - Ofelia (ingresa sesión 4)
---

# Resumen Semanal: Semana 1 del Curso

## Contexto General

La Semana 1 marca el inicio del curso de programación con **Bloque 0** (pensamiento algorítmico y pseudocódigo en PSeInt). Se divide en cuatro sesiones progresivas:

1. **Lunes (06/07)**: Presentaciones, filosofía del curso y evaluación diagnóstica
2. **Martes (07/07)**: Diagnóstico, pensamiento algorítmico y conceptos de memoria
3. **Miércoles (08/07)**: Estructuras complejas en PSeInt (menús, ciclos, refactorización)
4. **Jueves (09/07)**: Validación de entrada y arreglos (arrays)

La semana cierra con una evaluación del Bloque 0 en equipos y tarea sobre menús con operaciones en arrays.

---

## Temas Principales por Sesión

### Sesión 1 (06/07): Contexto, Profesor y Estudiantes

**Presentación del Profesor:**
- Background: Ingeniero mecatrónico, Maestría, Doctorado en Ingeniería
- Experiencia industrial: 4 años en Continental Automotive (radares, conducción autónoma, ADAS), 8 meses en Airbus Canadá (asistencia de vuelo, análisis de datos)
- Investigación actual: Modelación matemática, IA, redes neuronales para control en sistemas embebidos
- **Filosofía**: Enseñanza enfocada en industria, aplicación práctica, no solo teoría

**Filosofía del Curso:**
- Desarrollar el **"pensamiento del arquitecto"**: análisis (90%) antes que codificación (10%)
- Estructura: Bloque 0 (pseudocódigo) → Bloque 1+ (C++) → Especialización (Vehículos o IA)
- Progresión: Desde conceptos fundamentales hasta complejidad elevada (módulo 3)
- Proyecto final (Vehículos): ECU con comunicación CAN

**Perfiles de Estudiantes (9 iniciales + Ofelia en sesión 4):**
- Backend developers (JavaScript, Python)
- Ingenieros con experiencia en automotriz, control, robótica
- Experiencia en microcontroladores, data engineering, desarrollo web
- Edades: 22-40 años; experiencia: 0-6 años en industria

**Evaluación Diagnóstica:**
- Sin calificación, solo diagnóstica
- Plazo: 9:30 PM (zona central)
- Objetivo: Conocer nivel de entrada, ajustar velocidad

---

### Sesión 2 (07/07): Pensamiento Algorítmico y Memoria

**Diagnóstico:**
- Profesor retoma el curso tras evaluación diagnóstica
- Ajusta velocidad según resultados de estudiantes

**Pensamiento Algorítmico Repasado:**
- Estructura de problemas: Entradas → Proceso → Salidas
- Ejemplo: Cálculo de promedio y determinación de aprobación/reprobación
- Importancia: Separar problema en partes antes de codificar

**Condicionales y Optimización:**
- Uso de "Si/No" (if/else encadenado) vs. "descarte" para reducir evaluaciones
- Relevancia en sistemas embebidos: optimización es crítica
- Ejemplo: Sistema anticolisión (radar + cámara) detectando personas/animales
- Aporte de Arturo: Orden de IFs importa en producción

**Memoria y Punteros:**
- Introducción conceptual a bits y jerarquía de memoria
- Punteros: Control de ubicación de datos (relevante en código de producción/embebido)
- Explicación gráfica postponida

**Ejercicio Práctico:**
- Clasificación de número: positivo/negativo/cero
- Debate: Descarte (if/else) vs. condiciones explícitas
- Conclusión: Elegir según legibilidad y contexto

**Importancia de la Planeación:**
- Ahorra tiempo a largo plazo: requerimientos, análisis de riesgos, pruebas
- Contexto LLM: Más tiempo en planeación/prototipado que en codificación

---

### Sesión 3 (08/07): Estructuras Complejas en PSeInt

**Tipos de Datos Repasados:**
- Entero, Real/Double, Carácter, Cadena
- Buena práctica: Agrupar variables del mismo tipo

**Comandos Básicos:**
- `Escribir` (print), `Leer` (input), `<-` o `=` (asignación)
- Concatenación con comas en Escribir

**Condicionales Si/FinSi:**
- Ejemplo: Determinar aprobación (≥70) vs. reprobación
- Indentación crítica

**Menús con Según/FinSegún (CLAVE):**
- Construcción de menú interactivo con 4+ opciones
- Uso de `De otro modo` para opciones inválidas
- Estructura clara y eficiente

**Ciclos Mientras/FinMientras (Contribución de Ismael):**
- Refactorización: Mover menú adentro de ciclo
- Usar variable booleana (Verdadero/Falso) para control
- Permita múltiples iteraciones hasta salida explícita

**Diferencias C vs C++ (Contribución de Arturo):**
- **C**: Estructurado, .c/.h, compilación a objeto
- **C++**: Orientado a objetos, .cpp, compilación directa
- **Decisión**: Curso usa **C++ directamente**
- Make para compilación mencionado

**Evaluación del Bloque 0:**
- Formato: Pseudocódigo complejo en PSeInt
- Equipos: 2 personas
- Requisitos: Código limpio, diagrama de flujo, video explicativo
- Evaluación: Limpieza, optimización, orden

---

### Sesión 4 (09/07): Validación y Arreglos

**Bienvenida a Ofelia:**
- Experiencia: 3 años software embebido automotriz en Sidec (Querétaro)
- Conexión: Mismo ecosistema que Continental/profesor

**Validación de Entrada (CRÍTICO):**
- Problema: Valores inválidos causan crash o comportamiento incorrecto
- Solución: Ciclos while/repetir para re-preguntar

Ejemplo:
```pseudocodigo
Escribir "Ingresa edad"
Leer edad
Mientras edad < 0
    Escribir "Edad inválida"
    Leer edad
FinMientras
```

**Arreglos (Arrays) - Tema Central:**

**Definición y Dimensionamiento:**
```pseudocodigo
Definir calificaciones Como Real
Dimensión calificaciones[5]
```

**Características:**
- PSeInt indexa desde 1 (no desde 0)
- Acceso: `calificaciones[1]`, `calificaciones[2]`
- Llenado en cualquier orden

**Llenado:**

Manual (ineficiente):
```pseudocodigo
calificaciones[1] <- 10
calificaciones[2] <- 9
...
```

Automático con for (eficiente):
```pseudocodigo
Para i <- 1 Hasta 5
    Leer calificaciones[i]
FinPara
```

**Lectura:**
```pseudocodigo
Para i <- 1 Hasta 5
    Escribir calificaciones[i]
FinPara
```

**Validación dentro de ciclos:**
Combinar for + mientras para validar cada entrada (ej. 0-10)

**Operaciones sobre Arrays:**
- Promedio (suma/cantidad)
- Búsqueda (retornar valor en posición)
- Edición (modificar valor)

**Tarea Propuesta:**
Menú con operaciones sobre arreglos:
- Agregar datos
- Ver datos
- Borrar datos
- Editar datos

Requisitos: Combinar menú + arreglos + validación

---

## Progresión Temática de la Semana

```
Sesión 1: CONTEXTO
  └─ Presentaciones, filosofía, entrada diagnóstica

Sesión 2: FUNDAMENTOS ALGORÍTMICOS
  └─ Estructura entrada/proceso/salida
  └─ Condicionales optimizados
  └─ Memoria conceptual

Sesión 3: ESTRUCTURAS DE CONTROL
  └─ Menús (Según)
  └─ Ciclos (Mientras)
  └─ Refactorización
  └─ C++ vs C

Sesión 4: COLECCIONES Y VALIDACIÓN
  └─ Validación con ciclos
  └─ Arreglos (define, dimensiona, llena)
  └─ Iteración sobre arrays
  └─ Operaciones complejas
```

---

## Hitos y Evaluaciones

| Fecha | Evento | Estado |
|-------|--------|--------|
| 06/07 | Evaluación diagnóstica | Completada |
| 09/07 | Tarea: Menú con arrays | Propuesta |
| ~10-11/07 | Evaluación Bloque 0 (en equipos) | Próxima |
| Post-11/07 | Linux + C++ (Bloque 1) | Pendiente |

---

## Conceptos Clave Establecidos

1. **Pensamiento del arquitecto**: Análisis antes de código
2. **Pseudocódigo**: Herramienta esencial para planeación
3. **Indentación**: Crítica en PSeInt
4. **Validación**: Ciclos para restricciones de entrada
5. **Eficiencia**: Arreglos vs. múltiples variables
6. **Optimización**: Orden de condicionales, descarte en producción
7. **Menús**: Estructura de decisiones múltiples
8. **Ciclos**: Control de repetición y estado
9. **C++**: Lenguaje de destino (no C plano)

---

## Próximos Pasos

1. **Alumnos:**
   - Completar tarea de menú con arrays
   - Preparar evaluación Bloque 0 (pseudocódigo + diagrama + video)
   - Estudiar conceptos de ciclos y validación

2. **Profesor:**
   - Revisar tarea de arrays
   - Evaluar Bloque 0 en equipos
   - Preparar transición a Linux + instalación de herramientas
   - Iniciar Bloque 1: C++ básico

3. **Especialización:**
   - Vehículos: Proyecto final será ECU con CAN
   - IA: Enfoque diferente (probablemente redes neuronales)

---

## Notas Transversales

- **Mercado laboral:** Mexicanos preferidos en Canadá/Alemania; experiencia diversa suma
- **Generaciones:** Normal cambiar de empresa (no "casarse" con un trabajo)
- **Herramientas:** PSeInt, VS Code, Make, Docker (mencionados)
- **Filosofía pedagógica:** Poco a poco (gatear → caminar → correr); errores son normales
- **Conexiones industriales:** Continental, Sidec, empresas japonesas (TQ1), Airbus
