# Contexto: Diseño de ACU (Electronic Control Unit)

## Resumen

Primera evaluación del curso: Diseño lógico de un **ACU (Electronic Control Unit)** para sistemas automotrices. Introducción a la arquitectura de control electrónico de vehículos.

**Fecha**: 20-28/07/2026  
**Bloque**: 1 (Especialidad Automotriz)  
**Evaluación**: Trabajo en equipos de 3 personas  
**Formato**: Diseño lógico + defensa de propuesta

---

## ¿Qué es una ACU/ECU?

### Definición

**ACU = Electronic Control Unit** (Unidad Electrónica de Control)

La "computadora del vehículo" que:
- Recibe señales de sensores
- Procesa información
- Toma decisiones
- Controla actuadores
- Comunica con otras ACUs
- Detecta y reporta fallas

### Fórmula Básica

```
ENTRADA (Sensor) → PROCESAMIENTO → DECISIÓN → SALIDA (Actuador)
```

### Concepto Clave

> **"El ACU transforma una MEDICIÓN FÍSICA en una DECISIÓN LÓGICA"**

**Ejemplo:**
- Temperatura medida: 115°C
- Límite crítico: 105°C
- Decisión: "115 > 105" → Prender ventilador
- Acción ejecutada: Ventilador activado

---

## Arquitectura del Sistema

### Componentes Hardware

1. **Microcontrolador** - Procesa el código
2. **Memoria** - Almacena datos (volátil en vehículos)
3. **Fuente de alimentación** - 12-14V típico
4. **Entradas/Salidas (I/O)** - Conectadas a sensores y actuadores
5. **Interfaces de comunicación** - CAN, Ethernet, etc.

### Componentes Software

- Código embebido (lo que programaremos)
- Funciones de diagnóstico
- Mecanismos de seguridad
- Validación de datos

---

## Arquitectura Zonal

Los vehículos modernos dividen el control en **zonas**:

| ECU | Zona | Responsabilidad |
|-----|------|---|
| Engine ECU | Motor | Inyección, ignición, combustible |
| Gateway ECU | Centro | Distribuye mensajes (como un router) |
| Control ECU | Control | Toma decisiones basadas en datos |
| Transmission ECU | Transmisión | Cambios automáticos |
| Brake ECU | Frenos | ABS, frenado automático |
| Airbag ECU | Seguridad | Bolsas de aire |

---

## Conceptos Fundamentales

### Señales

Una **señal** es una variable que cambia con el tiempo, enviada por un sensor.

**Propiedades:**
- Nombre (ej: "Velocidad")
- Rango válido (ej: 0-250 Km/h)
- Unidad (ej: Km/h)
- Origen - qué sensor la genera (ej: sensor de rueda)
- Destino - qué ACU la recibe (ej: Panel del conductor)
- Tasa de refresco (ej: cada 100ms)

**Estados:**
- **VÁLIDA** - Dentro de rango + actualizada
- **INVÁLIDA** - Fuera de rango
- **AUSENTE** - No se actualizó en el tiempo esperado (timeout)

### Mensajes

Un **mensaje** agrupa varias señales relacionadas para transmisión eficiente.

**Ejemplo: Mensaje "Motor"**
```
ID: 0x100
Señales:
- RPM: 1000
- Temperatura: 95°C
- Estado: OK
Timestamp: 50000ms
```

### Gateway vs Control

#### Gateway ECU
- Recibe datos crudos
- Valida formato, rango, timestamp
- Distribuye a otras ACUs
- Solo **administra** información

#### Control ECU
- Recibe datos validados del Gateway
- Analiza señales
- Clasifica fallas (crítica/normal/sin falla)
- Ejecuta acciones
- Cambia estado del sistema

### Estados del Sistema

| Estado | Significado | Cuando usar |
|--------|-------------|---|
| **INIT** | Inicialización | Al encender, autotests |
| **OPERATIONAL** | Normal | Sistema funciona completamente |
| **DEGRADE** | Falla leve | Funciona con limitaciones |
| **SAFE_STATE** | Falla crítica | Sistema se limita o apaga |
| **OFF** | Apagado | Sistema desactivado |

---

## Flujo de Datos Completo

```
1. SENSOR genera valor
   ↓
2. Se construye MENSAJE (agrupa valores)
   ↓
3. GATEWAY recibe
   - Valida formato ✓
   - Valida rango ✓
   - Valida timestamp ✓
   ↓
4. GATEWAY envía a CONTROL
   ↓
5. CONTROL analiza
   - ¿Hay falla?
   - ¿Es crítica?
   ↓
6. CONTROL ejecuta ACCIÓN
   - Prender ventilador
   - Cambiar estado
   - Activar alarma
   ↓
7. ACTUADOR ejecuta
8. PANEL informa al usuario
```

---

## Primera Evaluación: Diseño de ACU

### Objetivo

Crear el **diseño lógico** (no implementación) de una ACU funcional.

### Entregables

**Un documento que contenga:**

#### 1. Definición de 5+ Señales

Para CADA señal, especificar:
- Nombre (ej: Velocidad)
- ¿Qué representa? (ej: Velocidad del vehículo)
- Unidad (ej: Km/h)
- Rango válido (ej: 0-250)
- Origen - sensor (ej: Sensor de velocidad en ruedas)
- Destino - ACU que la recibe (ej: Panel)
- Tasa de refresco (ej: Cada 100ms)
- ¿Qué pasa si es inválida? (ej: Marcar error)
- ¿Qué pasa si se ausenta? (ej: SAFE_STATE)

#### 2. Definición de Mensajes

Para CADA mensaje:
- ID único (ej: 0x100)
- ¿Qué señales contiene? (lista)
- ¿Quién lo genera? (sensor/ACU)
- ¿Quién lo recibe? (ACU)
- ¿Cómo se valida? (reglas)

#### 3. Máquina de Estados (Pseudocódigo)

Implementar en PSeInt:
- ACU Gateway
  - Recibe mensaje
  - Valida (formato, rango, tiempo)
  - Envía al Control si es válido
- ACU Control
  - Recibe datos validados
  - Analiza condiciones
  - Ejecuta acciones
  - Cambia estado

#### 4. Reglas de Decisión

Especificar condicionales:
- "Si temperatura > 105°C → DEGRADE"
- "Si voltaje < 9V → SAFE_STATE"
- "Si rpm > 7000 → Limitar aceleración"
- Etc.

### Proceso

| Fase | Duración | Qué hacer |
|------|----------|-----------|
| Teoría (20/07) | 1 sesión | Aprender conceptos |
| Dudas (21/07) | 1 sesión | Resolver preguntas |
| Desarrollo (22-27/07) | 5 días | Propuesta en equipo |
| Presentación (28/07) | TBD | Defensa y exposición |

### Equipos

- **Cantidad**: 4 equipos
- **Tamaño**: 3 personas cada uno
- **Libertad**: Cada equipo propone su versión
- **Defensa**: Explicar y justificar decisiones

---

## Señales Propuestas (Opcionales)

Pueden usar estas o proponer otras (mínimo 5):

| Señal | Rango | Unidad | Nota |
|-------|-------|--------|------|
| **Velocidad** | 0-250 | Km/h | Velocidad del vehículo |
| **RPM** | 0-8,000 | Rev/min | Revoluciones por minuto del motor |
| **Temperatura** | -40 a 150 | °C | Temperatura del motor |
| **Acelerador** | 0-100 | % | Posición del pedal acelerador |
| **Voltaje** | 9-16 | V | Voltaje de la batería |

**Interpretación de rangos:**
- Temperatura: <0°C anormal, 0-105 normal, >105 falla
- RPM: 0 motor apagado, >6000 próximo al límite
- Voltaje: <9V falla crítica, 9-12 batería baja, 12-14 normal, >14 sobrecarga

---

## Validación de Datos

### En Gateway

```pseudocódigo
Si velocidad está entre 0 y 250 Entonces
    velocidad_válida ← Verdadero
Sino
    velocidad_válida ← Falso
FinSi

// Verificar si no es demasiado vieja
Si tiempo_actual - tiempo_último < 100ms Entonces
    señal_activa ← Verdadero
Sino
    señal_activa ← Falso  // AUSENTE
FinSi
```

### En Control

```pseudocódigo
Si velocidad_válida Y señal_activa Entonces
    // Procesar normalmente
    
    Si temperatura > 105 Entonces
        estado ← DEGRADE
    FinSi
    
    Si voltaje < 9 Entonces
        estado ← SAFE_STATE
    FinSi
Sino
    // Señal no confiable
    estado ← SAFE_STATE
FinSi
```

---

## Ejemplos Concretos

### Ejemplo 1: Falla de Temperatura

```
Sensor reporta: 115°C
Gateway valida: ¿115 está en -40 a 150? SÍ ✓
Gateway envía a Control

Control recibe: Temperatura = 115°C (válida)
Control analiza: ¿115 > 105? SÍ
Control decide: DEGRADE
Control ejecuta: 
  - Limita velocidad máxima a 100 Km/h
  - Prendio ventilador
  - Activa testigo en panel
```

### Ejemplo 2: Falla de Voltaje Crítica

```
Sensor reporta: 7.5V (batería muere)
Gateway valida: ¿7.5 está en 9-16? NO ✗
Gateway marca: INVÁLIDA
Gateway NO envía a Control (o envía como inválida)

Control detecta: Señal inválida
Control decide: SAFE_STATE
Control ejecuta:
  - Apaga sistemas no esenciales
  - Cierra puertas (seguridad)
  - Prepara motor para apagarse
```

---

## Diferencia: Gateway vs Control

### Gateway (Validador)

```
Entrada: Mensaje crudo de sensor
├─ ¿Formato correcto? (número, no texto)
├─ ¿Rango válido? (0-250 si es velocidad)
├─ ¿Timestamp coherente? (no retroceder en tiempo)
└─ Salida: VÁLIDO o INVÁLIDO
```

### Control (Decisor)

```
Entrada: Señal validada del Gateway
├─ ¿Qué significa este valor?
├─ ¿Hay un problema?
├─ ¿Es crítico o normal?
└─ Salida: Estado del sistema + Acción
```

---

## Iteraciones Futuras (Bloques 2, 3, ...)

### Bloque 1→2: Simulación de Sensores

- Implementar en C++
- Crear sensores virtuales que generen valores
- ACU recibe datos simulados
- Verificar comportamiento

### Bloque 2→3: Orientado a Objetos

- Convertir ACU a clases
- `class Gateway`, `class ControlECU`
- Herencia y polimorfismo
- Relaciones entre objetos

### Bloque 3+: Embebida Real

- Ejecutar en ESP32 (microcontrolador)
- Conectar sensores reales
- Comunicación CAN entre ECUs
- Código optimizado para memoria limitada

---

## Recursos

### Archivos de la Sesión

- `resumen.md` — Resumen completo de la sesión 20/07
- `raw_transcript.txt` — Transcript íntegro de la clase
- `ACU_CONTEXT.md` — Este archivo (guía rápida)
- `SEMANA_RESUMEN.md` — Resumen semanal

### Referencias Externas

- [ECU Architecture](https://en.wikipedia.org/wiki/Electronic_control_unit)
- [CAN Bus Protocol](https://en.wikipedia.org/wiki/CAN_bus) (futuro)
- Vehículos ejemplo: Volkswagen (bóxer), Subaru (bóxer)

---

## Preguntas Frecuentes

**P: ¿Puedo cambiar las señales propuestas?**  
R: Sí, proponer otras es válido (ej: humedad, presión de neumáticos)

**P: ¿Cuántos estados debe tener mi ACU?**  
R: Mínimo 5-6. El profesor propone 6, pero pueden ser 4-8.

**P: ¿Debo implementar en C++ ya?**  
R: No, solo pseudocódigo PSeInt. C++ es para el siguiente bloque.

**P: ¿Puede mi equipo proponer algo muy diferente?**  
R: Sí, cada equipo defiende su diseño. Diferentes enfoques son bienvenidos.

**P: ¿Qué pasa si dos equipos proponen lo mismo?**  
R: Está bien. Lo importante es que entiendas y puedas explicar tu solución.

**P: ¿Necesito meter sensores reales?**  
R: No para esta evaluación. Solo diseño lógico. Sensores reales es futuro.

---

## Checklist de Entrega

- [ ] 5+ señales definidas con todas propiedades
- [ ] 2+ mensajes definidos (Gateway, Control)
- [ ] Máquina de estados en pseudocódigo
- [ ] Reglas de decisión claras (Si... entonces...)
- [ ] Documentación legible y organizada
- [ ] Equipo preparado para defender propuesta

---

**Creado**: 20/07/2026  
**Actualizado**: 20/07/2026  
**Evaluación**: Diseño de ACU (equipos de 3)  
**Deadline**: 28/07/2026

