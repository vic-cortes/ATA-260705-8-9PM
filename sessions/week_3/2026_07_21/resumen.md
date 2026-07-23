---
title: "Sesión Week 3 - 2026_07_21"
date: 2026-07-21
week: 3
bloque: "1"
temas:
  - "Bienvenida a estudiantes nuevos"
  - "Máquina de estados del ACU (detalle de transiciones)"
  - "Diagrama de contexto y flujo de señales"
  - "Requisitos funcionales (redacción)"
  - "Rúbrica de la primera evaluación"
  - "Mecánica de entrega y cronograma"
duracion_minutos: 60
estudiantes_presentes: 15
---

# Sesión 2 - Martes 21/07/2026
## Máquina de Estados, Requisitos y Rúbrica de la Evaluación

### Contexto General

- **Bloque**: 1 (Especialidad Automotriz)
- **Objetivo de la sesión**: Cerrar la teoría de la evaluación (máquina de estados + requisitos) y presentar la rúbrica
- **Novedad**: Se integran estudiantes nuevos al grupo (Camila, Ramón, Alejandro)

---

## 1. Bienvenida a Estudiantes Nuevos

Se presentaron los estudiantes que se integran al curso:

- **Camila Olguín** — Estudiante de preparatoria (entrará a segundo año)
- **Ramón** — Profesional de la industria de almacenamiento; fuerte en C y Python, experiencia previa con C++ (versiones antiguas); interesado en robótica y automotriz
- **Alejandro** — Nuevo integrante (se registró en lista)

**Notas del profesor:**
- Los nuevos no cursaron el Rango 0 (pseudocódigo), pero pueden apoyarse en las grabaciones
- Contacto disponible por WhatsApp y correo para dudas
- El profesor pedirá que los agreguen al grupo de WhatsApp y Classroom
- Total de asistentes en lista: **15 estudiantes**

---

## 2. Máquina de Estados del ACU (Detalle)

### Estados propuestos (6)

El profesor propone 6 estados, **mínimo 5 requeridos**, sin máximo. Los nombres son editables (ej: SAFE_STATE puede llamarse ERROR).

| Estado | Descripción |
|--------|-------------|
| **INIT** | Estado inicial al arrancar la máquina (ej: `estado = 0`) |
| **SELF_TEST** | Autoprueba rápida de variables/sistema |
| **OPERATIONAL** | Estado recurrente deseado; recibe, valida y procesa mensajes |
| **DEGRADED** | Falla recuperable; aplica acciones correctivas |
| **SAFE_STATE** | Falla crítica; limita operaciones, única salida es apagar |
| **SHUTDOWN** | Detiene todo, guarda registros, finaliza ejecución |

### Transiciones clave

```
INIT → SELF_TEST
SELF_TEST → OPERATIONAL   (todo bien — camino más común)
SELF_TEST → DEGRADED      (falla recuperable)
SELF_TEST → SAFE_STATE    (falla crítica)
OPERATIONAL → DEGRADED    (falla menor detectada)
OPERATIONAL → SHUTDOWN    (solicitud de apagado)
DEGRADED → OPERATIONAL    (sistema se recupera)
DEGRADED → SAFE_STATE     (la falla empeora)
SAFE_STATE → SHUTDOWN     (única salida posible)
SHUTDOWN → (terminal)     (sin regreso; reiniciar = "llavazo al carro")
```

### Ejemplo con temperatura

- Límite máximo definido: 120°C
- Se detecta **121°C** → falla recuperable → **DEGRADED** → acción: prender ventilador
- Si baja la temperatura → regresa a **OPERATIONAL**
- Si sube a **150-160°C** → falla crítica → **SAFE_STATE**

### Recomendación del profesor

Empezar con el camino feliz: `INIT → SELF_TEST → OPERATIONAL → SHUTDOWN`, y después agregar variantes de fallas.

---

## 3. Diagrama de Contexto y Flujo de Señales

### Flujo completo

```
Sensores (variables generadas a mano)
   ↓
Mensaje (arreglo: valor actual + timestamp + estatus por señal)
   ↓
ACU Gateway (valida)
   ↓
ACU Control (decide)
   ↓
Cambio de estado / Acciones
```

### Validaciones del Gateway

1. **Rangos**: Todos los valores del mensaje dentro de los rangos definidos
2. **Ciclos perdidos** (timestamps): Con ciclo de 200 ms definido:
   - Mensaje actual 300 ms, anterior 100 ms → 300−100 = 200 → **válido**
   - Mensaje actual 500 ms, anterior 100 ms → 500−100 = 400 → **ciclo perdido, mensaje inválido**
3. Puede usarse una variable temporal global o una por señal (más estricto)
4. El Gateway pasa las señales (válidas o marcadas inválidas) al ACU de Control

### Validaciones del ACU de Control

A diferencia del Gateway (que valida que la señal "venga buena": formato, rango, tiempos), el Control valida **condiciones de operación**:

- Temperatura por debajo de cierto valor
- Velocidad que no supere cierto límite
- Voltaje ≥ 9V (menos de 9V = batería muerta)
- Si llega una señal inválida → decidir: ¿una falla basta para SAFE_STATE o va a DEGRADED?

**El ACU de Control es quien decide los cambios de estado de la máquina.**

### Notas de implementación en PSeInt

- **Validaciones en secuencia**, no en paralelo (PSeInt no tiene hilos; hilos se verán en C++)
- En la vida real la industria trabaja con **arquitectura zonal** y comunicación **síncrona** entre zonas
- El usuario ingresa manualmente los valores de las señales (no hay datos random en PSeInt)
- Inicializar: `estado = INIT`, señales en cero, mensaje como cadena/arreglo

---

## 4. Requisitos Funcionales

### Estructura (ecuación del requisito)

```
[El sistema X] + [deberá] + [acción] + [condición]
```

**Ejemplo:**
> "El sistema (Gateway) **deberá validar** que la velocidad se encuentre dentro del rango permitido (0-250 km/h) antes de enviarla al ACU de control."

### Requisito vago vs. verificable

| ❌ Vago | ✅ Atómico y verificable |
|---------|--------------------------|
| "El sistema deberá funcionar correctamente" | "El sistema deberá marcar como inválido un valor de acelerador menor a 0% o mayor a 100%" |
| No indica qué es "correcto" ni cómo verificarlo | Comparable directamente contra el rango |

**Atómico** = compara/verifica una sola cosa a la vez.

### Requerimiento de la evaluación

- **Mínimo 10 requisitos** redactados por el equipo
- Los requisitos son el punto de partida del pseudocódigo
- **Los requisitos deben cumplirse en el pseudocódigo** ("ustedes se ponen sus propias reglas")

### Contexto de industria

En proyectos reales, el cliente (marca de autos) entrega la lista de requisitos; el desarrollador los revisa, negocia cuáles acepta, y una vez aceptado un requisito **debe cumplirse sí o sí** (experiencia del profesor en Continental con radar).

---

## 5. Rúbrica de la Evaluación (100 puntos)

| Criterio | Puntos | Evaluación |
|----------|--------|-----------|
| **Pseudocódigo** | 35 | Cualitativa: flujo completo, claro, coherente, con validaciones y fallas |
| **Máquina de estados** | 25 | Cualitativa: incluye estados, transiciones coherentes, **coincide con el pseudocódigo** |
| **Requerimientos** | 20 | Claros, específicos, entendibles |
| **Presentación** | 20 | Video explicando la solución |

### Qué NO se evalúa

- Optimización del código ("ahorrar líneas")
- El proceso de diseño paso a paso (solo resultados finales)
- Cada mente piensa diferente; hay múltiples soluciones válidas

### Qué SÍ importa

- **Cómo pensaron y planearon** la solución
- Flujo claro, ordenado y coherente
- Que la máquina de estados **coincida** con el comportamiento del pseudocódigo
- Que se cumplan los requisitos propuestos por el propio equipo

---

## 6. Mecánica de Entrega

### Entregables (3)

1. **Pseudocódigo** del sistema (Gateway + Control)
2. **Máquina de estados** (diagrama: estados y relaciones entre ellos — distinto al pseudocódigo, que muestra operaciones y decisiones)
3. **10 requisitos funcionales**

### Presentación

- **Video** (subido a YouTube, Drive con permisos, etc.)
- Duración libre (5-10 min sugerido, sin mínimo ni máximo)
- Formato libre; puede grabarse por partes y juntarse
- No es exposición en clase (el profesor revisa en privado)
- En el video: contar **cómo pensaron la solución**

### Equipos

- **5 equipos de 3 personas** (15 estudiantes)
- El profesor asigna los equipos y los publica junto con la tarea
- Se aceptan cambios de equipo (avisar por mensaje)
- Trabajar **solo** es válido, pero se advierte que es mucha carga

### Cronograma

| Fecha | Actividad |
|-------|-----------|
| 21/07 (hoy) | Se sube la tarea + equipos al Classroom |
| 22-23/07 (mié-jue) | Clases dedicadas a **dudas** (no tema nuevo); setup de Linux para nuevos |
| 24-26/07 (vie-fin) | Desarrollo en equipos |
| **27/07 (lunes)** | **Último día de entrega** (28/07 martes máximo) |
| 27-28/07 | Inicia nuevo temario (Rango 1) |

### Regla del curso

No se puede avanzar de rango hasta que **todos** aprueben esta evaluación. El profesor debe justificar el pase de rango de cada estudiante.

---

## 7. Visión a Futuro del Proyecto

Este entregable es el **esqueleto** de un proyecto acumulativo que se reutilizará en todos los rangos:

1. **Rango 1**: Código directo (C++) + introducción a **Git** para versionar el proyecto
2. Después: Refactorización a objetos (OOP)
3. Después: Testing
4. **Meta final**: Producto estilo release de producción, embebido en una placa (el profesor busca opción de simulación si no se consiguen placas físicas)

**Advertencia**: No tomar la tarea a la ligera — cambiar el esqueleto/estructura después será costoso. Agregar señales nuevas sí es barato.

**Sobre IA**: Se permite apoyarse en IA, pero lo importante es **entender qué te está dando y cómo validarlo**.

---

## Preguntas Respondidas

**P (Jorge): ¿Si trabajo con las 5 señales básicas, tendré que rediseñar todo cuando se agreguen más señales (presión de llantas, temperatura de zona de confort, etc.)?**
R: No. Agregar señales/entradas es barato — solo es una señal extra a validar en el mismo flujo. Lo costoso es cambiar la **estructura** (el esqueleto de los dos ACUs). Todo se basa en 2 ACUs: Gateway (clasifica/valida) y Control (decide).

**P (Jorge): ¿Qué es la tarea de Linux que se mencionó?**
R: El curso se trabajará sobre **Debian** (distribución ligera, apta para embebidos). Instalar vía **WSL** (`wsl --install -d Debian` desde PowerShell como admin). Windows 10/11 lo traen por default. No requiere particionar el disco. Hay una clase grabada dedicada a la instalación.

**P (Jorge): ¿Se puede usar Raspbian/Raspberry OS?**
R: Raspbian es más pesado; vive en un procesador (la Raspberry ya es una computadora), no en un microcontrolador. Mejor Debian por WSL.

**P (Camila): ¿Es como instalar una máquina virtual? Ya tengo Debian en VM.**
R: WSL no es una VM, es un **subsistema** accesible solo por terminal — gasta menos espacio. Puede trabajar con su VM existente, pero se recomienda evaluar WSL.

---

## Notas Administrativas

- Se pasó lista: **15 estudiantes** registrados
- El profesor agregará con urgencia a Ramón al WhatsApp/Classroom
- Los nuevos deben revisar las grabaciones (especialmente la de setup de Linux)
- La tarea con toda la información (diapositivas, ejemplos, rúbrica, equipos) se sube hoy después de la clase de 9-10
- Mañana el profesor traerá cámara (hoy falló)

---

**Duración**: ~60 minutos
**Próxima sesión**: 22/07/2026 (sesión de dudas + setup Linux para nuevos)
**Entrega de evaluación**: Lunes 27/07/2026 (máximo martes 28/07)
