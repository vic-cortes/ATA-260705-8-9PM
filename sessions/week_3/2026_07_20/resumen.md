---
title: "Sesión Week 3 - 2026_07_20"
date: 2026-07-20
week: 3
bloque: "1"
temas:
  - "Evaluación torniquete (revisión)"
  - "ECU - Electronic Control Unit"
  - "Arquitectura de sistemas automotrices"
  - "Señales y mensajes en vehículos"
  - "Primera evaluación: Diseño de ACU"
duracion_minutos: 287
estudiantes_presentes: 12
---

# Sesión 1 - Miércoles 20/07/2026
## ECU y Sistemas Automotrices

### Contexto General

- **Bloque**: 1 (Transición a C++)
- **Especialidad**: Automotriz
- **Evaluación**: Primera evaluación formal del curso
- **Formato**: Trabajo en equipos (equipos de 3 personas)

---

## 1. Revisión de Tarea: Torniquete (20 min)

### Presentación de Alejandro

Alejandro presentó su solución del torniquete en PSeInt:

**Estructura de su código:**
- Variables booleanas: `moneda`, `ejecutar`
- Estados: `bloqueado` (0), `desbloqueado` (1)
- Ciclo principal: `Mientras ejecutar`
- Menú interactivo con 3 opciones: moneda (1), empujar (2), salir (3)

**Lógica de transiciones:**
1. **Insertar moneda** → Desbloquea torniquete
2. **Empujar sin moneda** → Acceso denegado, permanece bloqueado
3. **Empujar con moneda** → Registra paso, vuelve a bloquear, incrementa contador
4. **Salir (opción 3)** → Termina programa

**Mejora sugerida por profesor:**
- Agregar estado **ESPERANDO**: Timeout que rebloquea el torniquete automáticamente si no se empuja en N segundos
- Implementar temporizador usando ciclos o `wait`
- Ejemplo de máquina con más de 2 estados

---

## 2. Introducción a ECU (60 min)

### ¿Qué es un ECU?

**ECU = Electronic Control Unit** (Unidad Electrónica de Control)

- Es la "computadora del vehículo"
- Recibe señales de sensores
- Procesa información
- Toma decisiones
- Controla actuadores
- Comunica con otras ECUs
- Detecta y reporta fallas

**Función central:**
```
ENTRADA (sensores) → PROCESAMIENTO → DECISIÓN → SALIDA (actuadores)
```

### Regla de Oro

> "El ECU transforma una **medición física** en una **decisión lógica**"

**Ejemplo práctico:**
- Sensor de temperatura reporta: 115°C
- Límite de operación: 105°C
- Decisión: Activar ventilador
- Acción: Ventilador prendido → Ruido característico

---

## 3. Componentes del ECU

### Hardware

1. **Microcontrolador** - Circuito integrado que ejecuta el código
2. **Memoria** - Generalmente volátil (se pierde al apagar)
3. **Fuente de alimentación** - Sistema de 12V-14V en vehículos
4. **Entradas/Salidas (I/O)** - Conectadas a sensores y actuadores vía arnés
5. **Interfaces de comunicación** - CAN, Ethernet, etc.

### Software

- Código embebido (lo que haremos nosotros)
- Funciones de diagnóstico
- Mecanismos de seguridad

---

## 4. Arquitectura Zonal de Vehículos Modernos

### Concepto

En lugar de una arquitectura centralizada, los vehículos modernos usan **Arquitectura Zonal**:
- Divide el vehículo en **zonas**
- Cada zona tiene su propia ECU
- Las ECUs se comunican entre sí

### Ejemplo de zonas:

1. **Motor ECU** - Control del motor, inyectores, ignición
2. **Transmisión ECU** - Control de cambios automáticos
3. **Frenos ECU** - Sistema antibloqueo (ABS), frenado automático
4. **Airbag ECU** - Control de bolsas de aire
5. **Dirección ECU** - Dirección asistida, ADAS
6. **Carrocería ECU** - Puertas, ventanas, luces
7. **Gateway ECU** - Distribuidor central de información

---

## 5. Gateway y Control

### Gateway
- **Función**: Actúa como router/distribuidor de mensajes
- **Analogía**: Centro de distribución (como una API)
- Recibe datos de múltiples fuentes
- Decide dónde enviar cada información
- Solo administra y redistribuye información

**Ejemplo:**
- Recibe: datos de motor, frenos, sensores
- Decide: enviar a panel (para usuario), a control (para decisiones), a diagnóstico

### Control ECU
- **Función**: Toma decisiones basadas en datos
- Analiza señales
- Clasifica fallas (crítica, normal, sin falla)
- Cambia estado del sistema
- Ejecuta acciones (ej: prender ventilador)

---

## 6. Señales en Vehículos (45 min)

### Definición

Una **señal** es una variable que cambia con el tiempo, reportada por sensores.

**Características:**
- **Discretas**: Valores en puntos (no continuos), aunque pueden aproximarse a continuos
- **Con timestamp**: Cada valor lleva marca de tiempo para coherencia
- **Unidades**: Km/h, RPM, °C, Voltios, %

### Propiedades de una Señal

1. **Representación** - ¿Qué representa? (ej: velocidad del vehículo)
2. **Unidad** - ¿En qué se mide? (Km/h, m/s)
3. **Origen** - ¿De dónde viene? (Sensor de velocidad en ruedas)
4. **Destino** - ¿A dónde va? (Panel, ECU de control)
5. **Rango válido** - ¿Qué valores son aceptables?
6. **Tipo de dato** - Entero, flotante, booleano
7. **Tasa de refresco** - ¿Cada cuánto se actualiza?

### Estados de una Señal

1. **VÁLIDA** - Dentro de rango + no es muy vieja
2. **INVÁLIDA** - Fuera de rango
3. **AUSENTE** - Timeout: No se actualizó en el tiempo esperado

### Ejemplo: Velocidad

| Propiedad | Valor |
|-----------|-------|
| Representa | Velocidad del vehículo |
| Unidad | Km/h (0-250) |
| Origen | Sensor en ruedas |
| Destino | Panel, ECU control |
| Rango válido | 0 a 250 Km/h |
| Tipo dato | Flotante |
| Tasa refresco | Milisegundos |
| Válido | Ej: 65 Km/h ✓ |
| Inválido | Ej: -40 Km/h ✗ |
| Ausente | No recibe datos hace 2 segundos ⚠ |

### Propuestas del Profesor para ACU

**Mínimo 5 señales (opcionales, pueden cambiar):**

1. **Velocidad** - 0 a 250 Km/h
2. **RPM (Revoluciones Por Minuto)** - 0 a 8,000 RPM
   - Velocidad de giro del motor
   - No necesariamente proporcional a velocidad (depende del cambio)
3. **Temperatura del motor** - -40°C a 150°C
4. **Acelerador (Throttle)** - 0% a 100%
5. **Voltaje de batería** - 9 a 16 Voltios
   - <12V indica batería descargada
   - >14V indica sobrecarga

---

## 7. Mensajes

### Definición

Un **mensaje** es un contenedor que agrupa múltiples señales relacionadas.

**Estructura:**
- ID del mensaje (identificador único)
- Una o más señales
- Timestamp
- Estado de validez
- Información de diagnóstico (opcional)

### Ejemplo: Mensaje "Motor"

```
Mensaje: Motor
├── RPM: 1000
├── Temperatura: 20°C
├── Estado: OK
└── Timestamp: 50000ms
```

**Ventaja:** En lugar de enviar 3 mensajes (1 por señal), enviamos 1 mensaje con 3 señales.

---

## 8. Flujo de Señales en ECU

### Proceso de validación

```
1. Sensor genera valor
   ↓
2. Se construye mensaje (agrupa valores)
   ↓
3. Gateway recibe mensaje
   ↓
4. Gateway valida:
   - ¿Formato correcto?
   - ¿Rango válido?
   - ¿Timeout válido?
   ↓
5. Si es válido → ECU Control
   ↓
6. ECU Control:
   - Analiza señal
   - Clasifica falla (crítica/normal/sin falla)
   - Cambia estado del sistema
   - Ejecuta acción
```

### Ejemplo completo

**Entrada:**
- Sensor de temperatura: 115°C
- Límite crítico: 105°C

**En Gateway:**
- Rango válido: -40 a 150°C
- 115°C ✓ está en rango
- Enviar a ECU Control

**En ECU Control:**
- Evalúa: ¿115°C > 105°C? SÍ
- Clasificación: Falla crítica
- Estado: SAFE_STATE (estado seguro)
- Acción: Prender ventilador automático

---

## 9. Clasificación de Fallas

### Estados del Sistema

El profesor propone **6 estados** para el ACU:

1. **INIT** - Inicialización, pruebas del sistema
2. **OPERATIONAL** - Sistema funcionando normalmente
3. **DEGRADE** - Falla normal, funciona con limitaciones
4. **SAFE_STATE** - Falla crítica, limitación severa de operación
5. **OFF** - Sistema apagado
6. (Opcional) **ERROR** - Estado de error (alternativa a SAFE_STATE)

### Criterios para cambiar estado

**DEGRADE:**
- Falla mínima, no crítica
- Ejemplo: Batería baja (11.9V)
- Sistema continúa operando

**SAFE_STATE (o ERROR):**
- Falla crítica
- Ejemplo: Voltaje muy bajo (<9V)
- Sistema se limita o apaga
- Activar testigo en panel ("Check Engine")

---

## 10. Primera Evaluación: Diseño ACU (60 min)

### Objetivo

Crear el **diseño lógico** de una ACU para sistemas automotrices.

### Entregable: Documento con

1. **Definición de señales** (mínimo 5)
   - Nombre
   - Rango válido
   - Unidad
   - Origen (sensor)
   - Destino (ACU)
   - Tasa de refresco
   - ¿Qué pasa si es inválida?
   - ¿Qué pasa si se ausenta?

2. **Definición de mensajes**
   - ID del mensaje
   - Señales que contiene
   - Componente que lo genera
   - Componente que lo recibe
   - Cómo se valida

3. **Máquina de estados** (pseudocódigo)
   - 2 ECUs: Gateway + Control
   - Gateway: Valida datos
   - Control: Toma decisiones
   - Usar máquina de estados

4. **Reglas de validación** (condicionales)
   - Si temperatura > 105°C → DEGRADE
   - Si voltaje < 9V → SAFE_STATE
   - Etc.

### Especificaciones Técnicas

- **Lenguaje**: Pseudocódigo en PSeInt (por ahora)
- **Formato**: Documento estructurado + pseudocódigo
- **Próximas iteraciones**:
  - Bloque 1→2: Agregar señales simuladas en C++
  - Bloque 2→3: Convertir a OOP (ECU como objetos)
  - Bloque 3+: Embebida real en microcontrolador (ESP32)

---

## 11. Contexto Futuro

### Visión a largo plazo

El profesor espera que los estudiantes desarrollen un ACU **funcional y realista** que:
- Simule comportamiento real de vehículos
- Use patrones de la industria automotriz
- Pueda ejecutarse en microcontrolador (ESP32)
- Sea escalable a múltiples ECUs

### Tecnologías mencionadas

- **ESP32** - Microcontrolador económico (posible destino final)
- **Jetson Nano** - Mini computadora (costosa)
- **Raspberry Pi** - Mini computadora (usada en algunos proyectos)
- **BigBone Black** - Similar a Raspberry

**Nota sobre motores:**
- **Motor bóxer** - Cilindros acostados (Volkswagen, Subaru)
- Más potente, más eficiente que motores normales
- Más caros de reparar

---

## 12. Organizacion y Próximos Pasos

### Grupos de trabajo

- **Cantidad**: 12 estudiantes presentes
- **Formato**: Equipos de 3 personas
- **Total**: 4 equipos de 3
- **Libertad**: Cada equipo propone su versión de ACU
- **Beneficio**: Ver diferentes puntos de vista, defensa de propuestas

### Cronograma

| Fecha | Actividad |
|-------|-----------|
| Hoy (20/07) | Teoría completa, pensar en propuesta |
| Mañana (21/07) | Resolver dudas sobre teoría |
| Semana (20-28/07) | Desarrollo de propuesta |
| Siguiente | Presentación y defensa de ACU |

### Tarea para esta noche

1. **Pensar en señales**: ¿Cuáles 5+ señales usaremos?
2. **Definir rangos**: Valores mínimo-máximo para cada señal
3. **Pensar en fallas**: ¿Qué es crítico? ¿Qué es degradación?
4. **Discutir en equipo** (si ya se forman)

---

## Conceptos Clave

### Definiciones importantes

| Término | Definición |
|---------|-----------|
| **ECU** | Unidad electrónica que controla sistemas del vehículo |
| **Gateway** | Distribuidor de mensajes entre ECUs |
| **Señal** | Variable que cambia con el tiempo (ej: velocidad) |
| **Mensaje** | Contenedor de varias señales relacionadas |
| **Timestamp** | Marca de tiempo para coherencia de datos |
| **Timeout** | Tiempo máximo sin actualizar una señal |
| **SAFE_STATE** | Estado seguro ante falla crítica |
| **DEGRADE** | Estado con funcionalidad limitada |
| **Arquitectura zonal** | Dividir vehículo en zonas con ECU cada una |

---

## Preguntas Respondidas

- ¿Por qué múltiples ECUs? → Procesamiento paralelo, redundancia, especialización
- ¿Qué es un motor bóxer? → Cilindros acostados (Subaru, VW)
- ¿Cómo se mide tiempo? → Desde que se enciende el vehículo (no reloj universal)
- ¿Qué pasa si falla un sensor? → Gateway marca como AUSENTE, ECU entra en SAFE_STATE

---

## Recursos Generados

- Presentación con arquitectura de ECUs (diagramas en LaTeX - a mejorar en PDF)
- Ejemplos de señales y rangos
- Reglas de validación en pseudocódigo
- Documentación será compartida en PDF (más legible)

---

**Duración real**: ~287 minutos (4h 47 min)  
**Próxima sesión**: 21/07/2026 (aclaraciones de dudas)  
**Entrega de evaluación**: Semana del 20-28/07/2026

