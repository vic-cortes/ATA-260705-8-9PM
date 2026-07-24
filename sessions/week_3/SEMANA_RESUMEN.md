---
week: 3
bloque: 1
periodo: "20-24/07/2026"
tema_principal: "ECU y Sistemas Automotrices"
objetivo: "Introducción a arquitectura de control electrónico automotriz"
evaluacion: "Primera evaluación: Diseño lógico de ACU"
sesiones_completadas: 3
sesiones_planeadas: 4
---

# Resumen de Semana 3: ECU y Sistemas Automotrices

## Contexto Semanal

**Bloque**: 1 - Especialidad Automotriz  
**Período**: 20-24 de Julio 2026  
**Objetivo principal**: Entender arquitectura de sistemas de control electrónico en vehículos  
**Evaluación**: Trabajo en equipo (diseño de ACU - Electronic Control Unit)  
**Duración**: Semana completa (hasta 28/07)

---

## Sesión 1 - 20/07/2026: ECU y Arquitectura Automotriz

### Tema Central

**Electronic Control Unit (ECU)** - La "computadora del vehículo"

### Conceptos Fundamentales Introducidos

#### 1. ¿Qué es una ECU?

Una ECU es un sistema que:
- **Recibe** señales de sensores
- **Procesa** información
- **Toma decisiones** basadas en lógica
- **Controla** actuadores (ventiladores, bombas, inyectores)
- **Comunica** con otras ECUs
- **Detecta y reporta** fallas

**Fórmula básica:**
```
Entrada (Sensor) → Procesamiento → Decisión → Salida (Actuador)
```

#### 2. Concepto Clave: "Transforma Medición Física en Decisión Lógica"

**Ejemplo:**
- Sensor: "Temperatura = 115°C"
- Límite crítico: 105°C
- Decisión: "115 > 105, encender ventilador"
- Acción: Ventilador activado

#### 3. Arquitectura Zonal

En vehículos modernos, el sistema de control se divide en **zonas**:

| ECU | Zona | Responsabilidad |
|-----|------|---|
| Engine ECU | Motor | Inyección, ignición, combustible |
| Transmission ECU | Transmisión | Cambios automáticos, torque |
| Brake ECU | Frenos | ABS, frenado automático |
| Airbag ECU | Seguridad | Despliegue de bolsas de aire |
| Steering ECU | Dirección | Dirección asistida, ADAS |
| Body ECU | Carrocería | Puertas, ventanas, luces |
| Gateway ECU | Centro | Distribuye mensajes entre ECUs |
| Diagnostic ECU | Diagnóstico | Lectura de códigos de error (OBD) |

### Componentes de una ECU

**Hardware:**
1. Microcontrolador (circuito integrado)
2. Memoria (generalmente volátil)
3. Fuente de alimentación (12-14V)
4. Entradas/Salidas (I/O) - conectadas a sensores/actuadores
5. Interfaces de comunicación (CAN, Ethernet)

**Software:**
- Código embebido (lo que programaremos)
- Funciones de diagnóstico
- Mecanismos de seguridad

### Gateway vs Control ECU

#### Gateway
- **Función**: Distribuye información
- **Analogía**: Centro de distribución / Router
- Solo **administra** y **redistribuye** datos
- No toma decisiones
- Valida formato, rango, timestamp de mensajes

#### Control ECU
- **Función**: Toma decisiones
- **Analogía**: Cerebro ejecutivo
- **Analiza** señales
- **Clasifica** fallas (crítica / normal / sin falla)
- **Ejecuta** acciones

---

## Sesión 2 - 21/07/2026: Máquina de Estados, Requisitos y Rúbrica

### Tema Central

Cierre de la teoría de la evaluación: **máquina de estados detallada**, **requisitos funcionales** y **rúbrica/mecánica de entrega**.

### Estudiantes Nuevos

Se integraron 3 estudiantes al curso (total: **15 estudiantes**, **5 equipos de 3**):
- **Camila Olguín** — estudiante de preparatoria
- **Ramón** — profesional (industria de almacenamiento), fuerte en C/Python, interesado en robótica/automotriz
- **Alejandro** — nuevo integrante

Los nuevos no cursaron el Rango 0; se apoyarán en grabaciones y en sesiones de setup de Linux.

### Máquina de Estados del ACU (Detallada)

Estados propuestos (mínimo 5 requeridos, sin máximo, nombres editables):

```
INIT → SELF_TEST
SELF_TEST → OPERATIONAL | DEGRADED | SAFE_STATE
OPERATIONAL → DEGRADED (falla menor) | SHUTDOWN (apagado)
DEGRADED → OPERATIONAL (se recupera) | SAFE_STATE (empeora)
SAFE_STATE → SHUTDOWN (única salida)
SHUTDOWN → terminal (sin regreso a INIT)
```

**Ejemplo de temperatura**: límite 120°C; detectar 121°C → DEGRADED (prender ventilador); si sube a 150-160°C → SAFE_STATE.

**Recomendación**: empezar por el camino feliz (INIT → SELF_TEST → OPERATIONAL → SHUTDOWN) y luego agregar variantes.

### Validación de Ciclos Perdidos (Gateway)

Nuevo detalle sobre validación por timestamp — con ciclo de 200 ms:
- Mensaje 300 ms, anterior 100 ms → Δ = 200 → **válido**
- Mensaje 500 ms, anterior 100 ms → Δ = 400 → **ciclo perdido → inválido**

### Requisitos Funcionales

**Estructura**: `[El sistema X] + [deberá] + [acción] + [condición]`

> "El sistema (Gateway) deberá validar que la velocidad se encuentre dentro del rango permitido (0-250 km/h) antes de enviarla al ACU de control."

- ❌ Vago: "El sistema deberá funcionar correctamente"
- ✅ Atómico/verificable: "El sistema deberá marcar como inválido un valor de acelerador menor a 0% o mayor a 100%"

**Se requieren mínimo 10 requisitos** por equipo; el pseudocódigo debe cumplirlos.

### Rúbrica (100 puntos)

| Criterio | Puntos |
|----------|--------|
| Pseudocódigo | 35 |
| Máquina de estados | 25 |
| Requerimientos | 20 |
| Presentación (video) | 20 |

Evaluación mayormente **cualitativa**: importa el flujo claro/coherente, que la máquina de estados coincida con el pseudocódigo y que se cumplan los requisitos propios. NO se evalúa optimización de código ni el proceso, solo resultados.

### Mecánica de Entrega

- **Presentación en video** (YouTube/Drive), duración y formato libres — no exposición en clase
- Tarea + equipos publicados en Classroom el 21/07
- 22-23/07: clases dedicadas a **dudas** (sin tema nuevo)
- **Entrega: lunes 27/07** (martes 28/07 máximo)
- Trabajar solo es válido pero se advierte la carga
- Regla: no se avanza de rango hasta que todos aprueben

### Notas Técnicas de la Sesión

- Validaciones **en secuencia** en PSeInt (no hay hilos; hilos se verán en C++)
- El usuario ingresa valores de señales a mano (sin random en PSeInt)
- Agregar señales a futuro es barato; cambiar la **estructura** es costoso
- Todo se basa en 2 ACUs: **Gateway** (valida) y **Control** (decide)
- Proyecto acumulativo: Rango 1 introduce **Git** para versionar; luego OOP, testing y meta embebida (placa o simulación)
- IA permitida, pero hay que **entender y validar** lo que genera
- Setup Linux: **Debian vía WSL** (`wsl --install -d Debian`); Raspbian descartado (muy pesado); VM Debian existente es aceptable

---

## Sesión 3 - 22/07/2026: Dudas, Repaso de la Evaluación y Setup del Entorno

### Tema Central

Sesión **sin tema nuevo**: repaso acelerado de toda la evaluación para un estudiante que se integra, y **troubleshooting en vivo** del entorno WSL + Debian.

### Precisiones sobre la Clasificación de Señales

Regla explícita del profesor:

- **VÁLIDA** ⟺ dentro de rango **Y** en tiempo
- **INVÁLIDA** ⟺ fuera de rango (ej. velocidad negativa)
- **AUSENTE** ⟺ se perdió la coherencia temporal (timeout)

> **Ausente ≠ fuera de rango.** Ejemplo: la señal tiene valor correcto pero debía refrescarse cada 10-100 ms y lleva 10 s sin actualizarse → deja de ser confiable.

Un **cuarto estado** (señal completamente errónea) es opcional; con dos clasificaciones es suficiente para aprobar.

### Estructura del Mensaje

Cadena con los valores de las señales **+ estatus**. Dos opciones:
- **Estatus por señal** (recomendado — el Gateway actualiza el estatus de cada señal)
- **Estatus general** del mensaje (más fácil, aceptable)

Los datos los ingresa el **usuario** en este hito. Diseño libre: una cadena por ciclo (cada cadena = nuevo tiempo) o un mensaje por sensor. Se sugiere probar con valores y tiempos inválidos.

### Aclaraciones sobre la Máquina de Estados

- **INIT**: primera parte del pseudocódigo — `estado ← INIT` + inicializar señales (velocidad 0, batería 11-12 V, RPM 0…)
- **SELF_TEST**: revisa que las variables iniciales no sean atípicas (velocidad ≠ 0 al encender no tiene sentido; batería con voltaje bajo hace fallar la prueba)
- **La máquina NO es cíclica**: de SHUTDOWN no se vuelve a INIT sin reiniciar. El "llavazo" apagado→encendido es una **acción externa**; en simulación = detener y volver a ejecutar el programa
- **La máquina de estados no representa el funcionamiento completo**: solo dice qué estados hay y cómo se pasa de uno a otro. El **pseudocódigo y el diagrama son cosas distintas**
- Faltan flechas en el diagrama de ejemplo: debe poder llegarse a **SHUTDOWN** desde OPERATIONAL y DEGRADED

### Cómo Llegar a los 10 Requisitos

Estrategia sugerida para quien no conoce el dominio:
1. **5 requisitos de señales** — uno por señal: *"El Gateway deberá revisar que la señal X esté dentro del rango [min, max]"*
2. **Requisitos del ACU de Control** — ej. *"deberá cambiar el estatus a DEGRADED si la temperatura supera 100 °C"*, *"a SAFE_STATE si el voltaje es menor a 9 V"*

Mejora de especificidad: en vez de "dentro del rango permitido", escribir "**dentro del rango de 0 a 250**".

> Lo importante es **respetar el formato**; el contenido técnico se irá mejorando. Los requisitos **deben cumplirse en el pseudocódigo**.

### Hitos del Proyecto (ciclo completo)

| Hito | Actividad |
|------|-----------|
| **0 (actual)** | Diseño conceptual: pseudocódigo + máquina de estados + requisitos |
| **1** | Pasar a **código** C++ con **Git** y repositorio versionado |
| **2** | Refactor a **OOP** (clases) |
| **3** | **Autodiagnóstico** |
| **4** | Arquitectura con **mejores prácticas** |
| **5** | **Optimización de memoria** |

**Git** se verá en 1-2 clases rápidas al arrancar C++. Requisito del hito 1: **no crear carpetas nuevas por versión** — versionar la misma carpeta en el repositorio.

### Setup del Entorno (troubleshooting en vivo)

**Aclaración sobre WSL**: no es una VM clásica, es un **subsistema** administrado por Microsoft; más ligero y vive aparte. Que Windows 10/11 separe los archivos del subsistema de los del sistema **es normal**. `/mnt` monta el disco de Windows.

**El problema real encontrado**: los `apt install` fallaban porque nunca se corrió `apt update`.

```bash
sudo apt update                          # PRIMERO (lista de paquetes)
sudo apt upgrade                         # DESPUÉS
sudo apt install build-essential git gdb
sudo apt install cmake                   # se verá más adelante
g++ --version && git --version           # verificar
```

> **Regla**: toda distribución Linux recién instalada requiere `update` + `upgrade`. No se actualiza sola como Windows.

**Compilación manual** (así se trabajará, sin depuradores del IDE por ahora):
```bash
g++ source.cpp -o source
./source
```

Otros: nombre correcto es `build-essential` (singular); `Ctrl+C` destraba la terminal; desde PowerShell admin → `wsl --list` y `wsl -d Debian`; copiar/pegar en la terminal de Windows es poco confiable.

### Visual Studio Professional vs VS Code

- VS Code: más fácil y básico → hitos 0-1. Professional: especializado en C/C++, algunas funciones avanzadas requieren **licencia**
- **Nadie tiene que cambiarse por ahora**; migración prevista para el hito 1 o 2 (el profesor lo consultará con la academia)
- La extensión de WSL de VS Code **no existe** en Professional; usar **Ver → Terminal → Debian**
- Contexto de industria: las funciones avanzadas se usan más para **C** que para C++. Mucho código del carro sigue siendo **C** (radares gen. 5 hacia atrás son puro C; los nuevos combinan o son puro C++)
- **Depuradores del IDE: no usarlos aún** — se trabaja en terminal por control y limpieza; debuggear en este entorno es distinto y se verá después

### Notas Administrativas

- **Asistencia libre** en esta sesión
- Grabación del 21/07 publicada en Classroom durante la clase
- Se integra un estudiante nuevo; se le recomienda ver **mínimo las dos últimas grabaciones** (ECU + máquina de estados) y la de setup de Linux
- Dudas por chat del curso o WhatsApp en cualquier momento

---

## Señales en Vehículos

### Definición

Una **señal** es una variable que cambia con el tiempo, enviada por un sensor.

**Características:**
- Discretas (valores en puntos)
- Llevan timestamp (marca de tiempo)
- Tienen unidad de medida
- Rango válido definido
- Tasa de refresco (actualización periódica)

### Propiedades que Define una Señal

1. **¿Qué representa?** - Significado físico (velocidad, temperatura, etc.)
2. **¿Qué unidad?** - Km/h, °C, RPM, %, V
3. **¿De dónde viene?** - Sensor específico
4. **¿A dónde va?** - Qué ECU la recibe
5. **¿Rango válido?** - Mínimo y máximo aceptable
6. **¿Tipo de dato?** - Entero, flotante, booleano
7. **¿Tasa de refresco?** - Cada cuánto se actualiza (ms, μs)

### Estados de una Señal

| Estado | Condición | Acción |
|--------|-----------|--------|
| **VÁLIDA** | Dentro de rango + no vieja | Procesar normalmente |
| **INVÁLIDA** | Fuera de rango | Marcar como error |
| **AUSENTE** | Timeout (no se actualiza) | Considerar desconocida |

### Señales Propuestas para la Evaluación

(Opcionales - pueden cambiar)

| Señal | Rango | Unidad | Nota |
|-------|-------|--------|------|
| Velocidad | 0-250 | Km/h | No correlaciona directamente con RPM |
| RPM | 0-8,000 | Revoluciones/min | Mide velocidad de giro del motor |
| Temperatura | -40 a 150 | °C | -40°C a 105°C normal; >105 falla |
| Acelerador | 0-100 | % | Posición del pedal |
| Voltaje | 9-16 | V | <12V batería descargada; <9 falla crítica |

---

## Mensajes

### Definición

Un **mensaje** es un contenedor que agrupa varias **señales relacionadas** para transmisión eficiente.

**Estructura:**
```
Mensaje "Motor"
├── RPM: 1000
├── Temperatura: 95°C
├── Estado: OK
└── Timestamp: 50000ms
```

**Ventaja**: Enviar 1 mensaje (3 señales) en lugar de 3 mensajes (1 cada uno)

---

## Flujo de Datos Completo

```
1. SENSOR
   Genera valor (ej: 115°C)
   │
2. MENSAJE
   Agrupa valores de múltiples sensores
   │
3. GATEWAY
   Valida:
   - ¿Formato válido?
   - ¿Rango correcto?
   - ¿Timestamp coherente?
   │
4. ECU CONTROL
   Analiza:
   - ¿Qué significa el valor?
   - ¿Hay falla?
   - ¿Qué acción tomar?
   │
5. ACTUADOR
   Ejecuta (ej: prende ventilador)
   │
6. PANEL/USUARIO
   Muestra información (ej: testigo en tablero)
```

---

## Clasificación de Estados del Sistema

El profesor propone **6 estados** para una ACU:

| Estado | Significado | Comportamiento |
|--------|-------------|---|
| **INIT** | Inicialización | Sistema realiza autotests |
| **OPERATIONAL** | Normal | Sistema funciona completamente |
| **DEGRADE** | Falla leve | Funciona con limitaciones (ej: velocidad máxima reducida) |
| **SAFE_STATE** | Falla crítica | Sistema se limita drasticamente o apaga (ej: prender testigo "Check Engine") |
| **OFF** | Apagado | Sistema desactivado |
| (Opcional) **ERROR** | Alternativa a SAFE_STATE | Algunos prefieren este nombre |

### Cuándo cambiar estado

**→ DEGRADE:**
- Falla no crítica (ej: batería bajando a 11.9V)
- Sistema continúa operando
- Se activa advertencia (luz amarilla)

**→ SAFE_STATE:**
- Falla crítica (ej: voltaje <9V, temperatura >150°C)
- Sistema se protege
- Se activa alarma (luz roja)
- Limita operaciones

---

## Primera Evaluación: Diseño de ACU

### Objetivo

Crear el **diseño lógico** (no implementación) de una ACU funcional para un vehículo simple.

### Entregables

**Documento que contenga:**

1. **Definición de 5+ Señales**
   - Nombre
   - Rango válido
   - Unidad
   - Qué sensor la genera
   - Qué ECU la recibe
   - Tasa de refresco
   - ¿Qué pasa si es inválida?
   - ¿Qué pasa si se ausenta?

2. **Definición de Mensajes**
   - ID único
   - Señales que agrupa
   - Quién lo genera
   - Quién lo recibe
   - Cómo se valida

3. **Máquina de Estados en Pseudocódigo**
   - ECU Gateway (valida datos)
   - ECU Control (toma decisiones)
   - Transiciones claras
   - Reglas de decisión

4. **Reglas de Validación**
   - Condicionales específicas
   - Ejemplo: "Si temp > 105°C → DEGRADE"
   - Ejemplo: "Si voltaje < 9V → SAFE_STATE"

### Formato y Proceso

| Aspecto | Detalle |
|---------|---------|
| **Lenguaje** | Pseudocódigo PSeInt (por ahora) |
| **Trabajo** | Equipos de 3 personas (individual permitido, con advertencia de carga) |
| **Equipos** | 5 equipos totales (15 estudiantes) — asignados por el profesor |
| **Libertad** | Cada equipo propone su versión (pueden ser similares) |
| **Defensa** | Video explicando la solución (YouTube/Drive, duración libre) |
| **Deadline** | Lunes 27/07 (martes 28/07 máximo) |

### Rúbrica (definida el 21/07)

| Criterio | Puntos |
|----------|--------|
| Pseudocódigo | 35 |
| Máquina de estados | 25 |
| Requerimientos (mín. 10) | 20 |
| Presentación (video) | 20 |
| **Total** | **100** |

### Cronograma Actualizado

| Fecha | Actividad |
|-------|-----------|
| 20/07 | Teoría completa |
| 21/07 | Máquina de estados, requisitos, rúbrica; tarea + equipos publicados |
| 22/07 | ✅ Dudas + repaso de la evaluación + setup WSL/Debian y compilación con g++ |
| 23/07 | Dudas; revisión de **avances** de los equipos |
| 24-26/07 | Desarrollo de propuesta en equipos |
| 27/07 (lunes) | **Último día de entrega** (28/07 máximo) |
| 27-28/07 | Inicia nuevo temario (Rango 1) |

### Iteraciones Futuras

- **Bloque 1→2**: Agregar simulación de sensores en C++
- **Bloque 2→3**: Convertir a OOP (ECU como clases)
- **Bloque 3+**: Ejecutar en microcontrolador real (ESP32)

---

## Conceptos Clave Aprendidos

### Definiciones

| Término | Definición | Ejemplo |
|---------|-----------|---------|
| **ECU** | Unidad electrónica de control | Motor ECU controla inyectores |
| **Gateway** | Distribuidor de mensajes | Recibe de motor, envía a panel |
| **Señal** | Variable que cambia con tiempo | Velocidad = 65 Km/h |
| **Mensaje** | Grupo de señales relacionadas | Motor {RPM: 1000, Temp: 95°C} |
| **Timestamp** | Marca de tiempo | Tiempo desde encendido del motor |
| **Timeout** | Tiempo máximo sin actualizar | Si no recibe en 100ms = AUSENTE |
| **SAFE_STATE** | Estado seguro ante crisis | Motor apagado por falla crítica |
| **DEGRADE** | Funcionalidad limitada | Velocidad máxima 80 Km/h |

### Regla de Oro

> **"El ECU transforma una MEDICIÓN FÍSICA en una DECISIÓN LÓGICA"**

La temperatura es solo un número. El ECU decide: "Prender ventilador" o "No hacer nada"

---

## Preguntas Frecuentes Respondidas

**P: ¿Por qué múltiples ECUs si podrían estar en una?**  
R: Especialización, redundancia, procesamiento paralelo, facilidad de debugging.

**P: ¿Qué es un motor bóxer?**  
R: Cilindros acostados (opuestos). Usado en Volkswagen, Subaru. Más potente pero más caro de reparar.

**P: ¿Cómo sabe el ECU qué hora es?**  
R: No usa reloj universal. Cuenta desde que se enciende el vehículo (timestamp relativo).

**P: ¿Qué pasa si un sensor falla completamente?**  
R: Gateway marca como AUSENTE, ECU Control interpreta como falla y cambia a SAFE_STATE.

**P: ¿Puede el voltaje ser mayor a 16V?**  
R: Sí, pero es sobrecarga. Daña componentes. Por eso el rango máximo es 16V.

**P: ¿Agregar señales nuevas después obliga a rediseñar todo?** *(21/07)*  
R: No. Agregar señales es barato (una validación extra en el mismo flujo). Lo costoso es cambiar la estructura de los 2 ACUs (Gateway + Control).

**P: ¿Cómo instalar el Linux del curso?** *(21/07)*  
R: Debian vía WSL (`wsl --install -d Debian` en PowerShell como admin). No requiere particionar. Raspbian descartado (muy pesado). Una VM Debian existente también es válida.

**P: WSL me separó los archivos del subsistema de los de Windows, ¿es normal?** *(22/07)*  
R: Sí. WSL no es una VM clásica sino un **subsistema** de Microsoft; vive aparte y no afecta los archivos de la computadora. `/mnt` monta el disco de Windows dentro de Linux.

**P: `sudo apt install` no encuentra los paquetes, ¿qué falta?** *(22/07)*  
R: Correr **`sudo apt update`** (y luego `upgrade`) antes de instalar. Una distribución recién instalada tiene la lista local de paquetes vacía y, a diferencia de Windows, no se actualiza sola.

**P: ¿Sigo con Visual Studio Professional o me cambio a VS Code?** *(22/07)*  
R: No pasa nada, sigue con el que tengas mientras encuentres los comandos. La migración a Professional está prevista para el hito 1 o 2. En Professional la terminal de Debian está en **Ver → Terminal** (la extensión de WSL es exclusiva de VS Code).

**P: ¿Cómo redacto requisitos si no conozco estos sistemas?** *(22/07)*  
R: Respeta el formato. 5 requisitos de señales (uno por señal con su rango) + requisitos del ACU de Control (cambios de estado por umbral). Lo exigible es que **se cumplan en el pseudocódigo**.

---

## Diferencias vs Week 2

| Aspecto | Week 2 | Week 3 |
|--------|--------|--------|
| **Concepto** | Máquinas de estado genéricas | ECU automotrices específicas |
| **Ejemplo** | Torniquete | Control de motor / Gateway |
| **Complejidad** | 2-3 estados | 6 estados + validación |
| **Datos** | Booleanos, contadores | Señales continuas, rangos |
| **Trabajo** | Individual | Equipos de 3 |
| **Entregas** | Pseudocódigo + Python | Diseño lógico + defensa |

---

## Recursos Generados

- Presentación con diagramas de ECU (PDF pendiente, mejorado)
- Tablas de señales y rangos
- Ejemplos de validación en pseudocódigo
- Estructura de la evaluación

---

## Próximos Pasos

### Para Estudiantes

1. **Revisar la tarea en Classroom** (equipos, rúbrica, diapositivas)
2. **22-23/07**: Traer dudas a clase; nuevos configurar Debian/WSL
3. **Semana/fin de semana**: Desarrollar los 3 entregables (pseudocódigo, máquina de estados, 10 requisitos)
4. **Grabar video** de presentación y subirlo (YouTube/Drive)
5. **27/07 (lunes)**: Entregar (28/07 máximo)

### Para Profesor

1. Subir tarea, equipos y material "tuneado" (diagramas) a Classroom ✓ (21/07)
2. Agregar a los estudiantes nuevos al WhatsApp/Classroom
3. Atender dudas en sesiones 22-23/07 y apoyar setup Linux de nuevos
4. Revisar videos y entregas; emitir calificaciones
5. Preparar material del Rango 1 (C++, Git) para el 27-28/07

---

## Estadísticas de la Semana

| Métrica | Valor |
|---------|-------|
| Sesiones completadas | 3 |
| Sesiones planeadas | 5 (con posibilidad de extender) |
| Conceptos introducidos | 15+ |
| Duración sesión 1 | 287 minutos (4h 47 min) |
| Duración sesión 2 | ~60 minutos |
| Duración sesión 3 | ~60 minutos (dudas + soporte técnico) |
| Estudiantes registrados | 15 (3 nuevos: Camila, Ramón, Alejandro) |
| Equipos formados | 5 (de 3 personas cada uno) |
| Evaluaciones activas | 1 (Diseño de ACU — entrega 27/07) |

---

**Última actualización**: 22/07/2026  
**Completitud**: 3/5 sesiones  
**Estado**: En progreso  
**Próxima sesión**: 23/07/2026 (dudas + revisión de avances de los equipos)

