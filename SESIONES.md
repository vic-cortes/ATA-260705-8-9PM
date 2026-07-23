# Índice de Sesiones

Navegación centralizada de todas las sesiones del curso por bloque, semana y fecha.

---

## 📚 Resúmenes Semanales

### Bloque 0: Pseudocódigo PSeInt

| Semana | Fechas | Tema Principal | Resumen |
|--------|--------|---|---|
| **1** | 06-09/07/2026 | Pensamiento algorítmico, condicionales, ciclos, arreglos | [📖 SEMANA_RESUMEN.md](sessions/week_1/SEMANA_RESUMEN.md) |

### Bloque 0→1: Transición a C++

| Semana | Fechas | Tema Principal | Resumen |
|--------|--------|---|---|
| **2** | 13-16/07/2026 | Linux terminal, máquinas de estado | [📖 SEMANA_RESUMEN.md](sessions/week_2/SEMANA_RESUMEN.md) |

### Bloque 1: Especialidad Automotriz - Sistemas ECU

| Semana | Fechas | Tema Principal | Resumen |
|--------|--------|---|---|
| **3** | 20-24/07/2026 | ECU, arquitectura automotriz, primera evaluación (ACU) | [📖 SEMANA_RESUMEN.md](sessions/week_3/SEMANA_RESUMEN.md) |

---

## 📅 Sesiones por Fecha

### Week 1: Bloque 0 Fundamentals

#### Sesión 1 - Lunes 06/07/2026
**Contexto, Profesor y Estudiantes**
- Presentación del profesor (Continental, Airbus, investigación en IA)
- Filosofía del curso (pensamiento del arquitecto)
- Perfil de estudiantes
- Evaluación diagnóstica

| Archivo | Descripción |
|---------|---|
| 📄 [resumen.md](sessions/week_1/2026_07_06/resumen.md) | Resumen estructurado |
| 📋 [raw_transcript.txt](sessions/week_1/2026_07_06/raw_transcript.txt) | Transcript completo |

---

#### Sesión 2 - Martes 07/07/2026
**Pensamiento Algorítmico y Memoria**
- Estructura entrada → proceso → salida
- Condicionales optimizados (descarte)
- Introducción a memoria y punteros
- Ejercicios de clasificación

| Archivo | Descripción |
|---------|---|
| 📄 [resumen.md](sessions/week_1/2026_07_07/resumen.md) | Resumen estructurado |
| 📋 [raw_transcript.txt](sessions/week_1/2026_07_07/raw_transcript.txt) | Transcript completo |

---

#### Sesión 3 - Miércoles 08/07/2026
**Estructuras Complejas en PSeInt**
- Tipos de datos (Entero, Real, Carácter, Cadena)
- Condicionales Si/FinSi
- **Menús con Según/FinSegún** (CLAVE)
- **Ciclos Mientras/FinMientras**
- C vs C++

| Archivo | Descripción |
|---------|---|
| 📄 [resumen.md](sessions/week_1/2026_07_08/resumen.md) | Resumen estructurado |
| 📋 [raw_transcript.txt](sessions/week_1/2026_07_08/raw_transcript.txt) | Transcript completo |

---

#### Sesión 4 - Jueves 09/07/2026
**Validación y Arreglos**
- Validación de entrada con ciclos
- **Arreglos (arrays)**: dimensión, llenado, lectura
- Operaciones sobre arrays (promedio, búsqueda, edición)
- Tarea: Menú con operaciones sobre arreglos

| Archivo | Descripción |
|---------|---|
| 📄 [resumen.md](sessions/week_1/2026_07_09/resumen.md) | Resumen estructurado |
| 📋 [raw_transcript.txt](sessions/week_1/2026_07_09/raw_transcript.txt) | Transcript completo |

---

### Week 3: Bloque 1 - Sistemas Automotrices

#### Sesión 1 - Domingo 20/07/2026
**ECU y Arquitectura Automotriz**
- Revisión de tarea: Solución del torniquete (Alejandro)
- **ECU - Electronic Control Unit**: concepto fundamental
- Componentes de un ECU (microcontrolador, memoria, I/O)
- **Arquitectura zonal** de vehículos modernos
- Gateway y ECU Control: roles diferentes
- **Señales**: definición, propiedades, validación
- **Mensajes**: agregación de señales
- Flujo de datos: sensor → gateway → control → actuador
- Clasificación de fallas (SAFE_STATE, DEGRADE, OPERATIONAL)
- **Primera evaluación**: Diseño de ACU (trabajo en equipos de 3)

| Archivo | Descripción |
|---------|---|
| 📄 [resumen.md](sessions/week_3/2026_07_20/resumen.md) | Resumen estructurado (completo y detallado) |
| 📋 [raw_transcript.txt](sessions/week_3/2026_07_20/raw_transcript.txt) | Transcript completo |
| 📖 [ECU_CONTEXT.md](sessions/week_3/ECU_CONTEXT.md) | Guía rápida de ECU |

**Ejercicio: Implementación ECU en Python** (`sessions/week_3/excercise/`)

| Archivo | Descripción |
|---------|---|
| 🐍 [ecu.py](sessions/week_3/excercise/ecu.py) | Máquina de estados, sensores y gateway |
| 🐍 [variables.py](sessions/week_3/excercise/variables.py) | Clases de sensores tipadas con validación |
| 🐍 [utils.py](sessions/week_3/excercise/utils.py) | Generador de datos de sensores simulados |
| 📄 [homework.md](sessions/week_3/excercise/homework.md) | Diseño de estados + diagrama Mermaid + requerimientos |

---

### Week 2: Bloque 0→1 Transition

#### Sesión 1 - Domingo 13/07/2026
**Cierre de Bloque 0 y Setup de Desarrollo**
- Revisión de tarea: MenuCalificaciones (validación, errores comunes)
- **Funciones en PSeInt** (SubProceso, Función con retorno)
- **Setup de Linux vía WSL**: instalación de Debian
- Instalación de herramientas: gcc, g++, gdb, make, nano

| Archivo | Descripción |
|---------|---|
| 📄 [resumen.md](sessions/week_2/2026_07_13/resumen.md) | Resumen estructurado |
| 📋 [raw_transcript.txt](sessions/week_2/2026_07_13/raw_transcript.txt) | Transcript completo |

---

#### Sesión 2 - Lunes 14/07/2026
**Comandos Linux Básicos**
- **Navegación**: `ls`, `pwd`, `cd`
- **Manipulación de archivos**: `mkdir`, `touch`, `cat`, `cp`, `mv`, `rm`
- **Edición**: `nano` (introducción)
- **Características**: autocompletado con Tab, permisos

| Archivo | Descripción |
|---------|---|
| 📄 [resumen.md](sessions/week_2/2026_07_14/resumen.md) | Resumen estructurado |
| 📋 [raw_transcript.txt](sessions/week_2/2026_07_14/raw_transcript.txt) | Transcript completo |

---

#### Sesión 3 - Martes 15/07/2026
**Comandos Linux Avanzados**
- **Visualización de archivos grandes**: `less`, `head`, `tail`
- **Búsqueda de contenido**: `grep` (búsqueda dentro de archivos)
- **Búsqueda de archivos**: `find` (nombres y extensiones)
- **Edición profunda**: `nano` (atajos, creación de archivos)
- **Automatización**: `echo` con redirección

| Archivo | Descripción |
|---------|---|
| 📄 [resumen.md](sessions/week_2/2026_07_15/resumen.md) | Resumen estructurado |
| 📋 [raw_transcript.txt](sessions/week_2/2026_07_15/raw_transcript.txt) | Transcript completo |

---

#### Sesión 4 - Miércoles 16/07/2026
**Máquinas de Estados (State Machines)**
- **Definición y componentes**: estado, evento, transición, acción
- **Ejemplos prácticos**: semáforo, puerta automática, relevador, elevador
- **Diagramas de transición**: lazos cerrados/abiertos, bifurcaciones
- **Tablas de transición**: alternativa a diagramas
- **Estados especiales**: ERROR, reintentos
- **Implementación en PSeInt**: `Según` (equivalente a `switch`)
- **Ciclos infinitos**: monitoreo permanente en embebidos
- Tarea: Diseño de máquina de estados

| Archivo | Descripción |
|---------|---|
| 📄 [resumen.md](sessions/week_2/2026_07_16/resumen.md) | Resumen estructurado |
| 📋 [raw_transcript.txt](sessions/week_2/2026_07_16/raw_transcript.txt) | Transcript completo |

---

## 🔗 Quick Links

### Por Concepto

**Estructuras de Control:**
- Condicionales: [Sesión 1.3](sessions/week_1/2026_07_08/resumen.md)
- Ciclos: [Sesión 1.3](sessions/week_1/2026_07_08/resumen.md)
- Menús: [Sesión 1.3](sessions/week_1/2026_07_08/resumen.md)

**Datos y Validación:**
- Tipos de datos: [Sesión 1.3](sessions/week_1/2026_07_08/resumen.md)
- Validación: [Sesión 1.4](sessions/week_1/2026_07_09/resumen.md)
- Arreglos: [Sesión 1.4](sessions/week_1/2026_07_09/resumen.md)

**Desarrollo Embebido:**
- Setup Linux: [Sesión 2.1](sessions/week_2/2026_07_13/resumen.md)
- Terminal Linux: [Sesión 2.2](sessions/week_2/2026_07_14/resumen.md), [Sesión 2.3](sessions/week_2/2026_07_15/resumen.md)
- **Máquinas de Estado**: [Sesión 2.4](sessions/week_2/2026_07_16/resumen.md) ⭐

### Recursos de Máquinas de Estado

**Material Complementario:**
- 📄 [TORNIQUETE_CONTEXT.md](sessions/week_2/TORNIQUETE_CONTEXT.md) — Índice y guía general
- 📄 [maquinas_de_estado_complementario.md](sessions/week_2/2026_07_16/maquinas_de_estado_complementario.md) — Material educativo profundo
- 📄 [torniquete_solucion.md](sessions/week_2/2026_07_16/torniquete_solucion.md) — Solución completa en pseudocódigo
- 📄 [torniquete_multiples_lenguajes.md](sessions/week_2/2026_07_16/torniquete_multiples_lenguajes.md) — Implementaciones en PSeInt, Python, C++

**Implementaciones (Ejecutables):**
- 🐍 [torniquete.py](sessions/week_2/torniquete.py) — Python con OOP y debugging (Recomendado para aprender)
- 📝 [torniquete.psc](sessions/week_2/torniquete.psc) — PSeInt ejecutable
- 📝 [torniquete_simple.psc](sessions/week_2/torniquete_simple.psc) — PSeInt versión simple

**Guías:**
- 📖 [README_TORNIQUETE.md](sessions/week_2/README_TORNIQUETE.md) — Cómo ejecutar y debuggear en VS Code

### Por Especialidad

**Especialidad Automotriz (Vehicular):**
- Concepto base: [Sesión 1.1](sessions/week_1/2026_07_06/resumen.md) (Filosofía, Continental, ADAS)
- Fundamental: [Sesión 2.4](sessions/week_2/2026_07_16/resumen.md) (Máquinas de estado para ECU)
- Próximo: Mini-ACU con máquinas de estado

**Especialidad IA:**
- Referencia: [Sesión 1.1](sessions/week_1/2026_07_06/resumen.md) (Investigación en redes neuronales)

---

## 📊 Estadísticas

| Métrica | Valor |
|---------|-------|
| **Bloques en progreso** | 3 (Bloque 0 ✓, Bloque 0→1 ✓, Bloque 1 en progreso) |
| **Semanas** | 3 |
| **Sesiones** | 9 |
| **Horas totales** | ~19.1 (390 min + 460 min + 287 min) |
| **Archivos de sesión** | 18 (9 resumen.md + 9 raw_transcript.txt) |

---

## 🚀 Próximos Pasos

1. **Próxima semana**: Bloque 1 - C++ Básico
2. **Temas pendientes**: Compilación, debugging, estructuras de datos
3. **Proyecto**: Mini-ACU para especialidad automotriz
4. **Evaluación**: Proyecto Bloque 0 (en equipos)

---

**Última actualización**: 22/07/2026  
**Resúmenes disponibles**: ✅ Semanas 1-2 completas · 🔄 Semana 3 en progreso (1/5 sesiones)  
**Próxima actualización**: Post-sesión week 3
