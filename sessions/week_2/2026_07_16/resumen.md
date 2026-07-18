---
fecha: 2026-07-16
bloque: 0→1
duracion: ~150 minutos
participantes:
  - Profesor
  - Ismael
  - Carlos
  - Otros alumnos (especialidad automotriz)
recursos:
  - transcript.txt (disponible en la misma carpeta)
---

# Resumen de la sesión de clase

**Contexto general:** Introducción fundamental a **máquinas de estados (state machines)**, concepto crítico para sistemas embebidos automotrices. Se combina teoría (diagramas de flujo) con implementación práctica en **PSeInt** usando `switch`/`según`. Esta sesión sienta las bases para proyectos futuros de ACU (Sistema de Control Automotriz).

## Puntos principales

**1. Importancia de máquinas de estados en sistemas automotrices**

Se explicó por qué las máquinas de estado son fundamentales:
- Muchos **componentes del vehículo** funcionan con estados discretos (encendido/apagado, abierto/cerrado, error/normal)
- El **ECU (Engine Control Unit)** y otros sistemas embebidos usan máquinas de estado internamente
- Entender máquinas de estado es **obligatorio** para especialidad automotriz
- A diferencia de sistemas analógicos (continuos), los sistemas automotrices modernos son **discretos** (basados en estados)

**2. Definición y conceptos básicos**

Una **máquina de estados** es:
- Un sistema que reporta constantemente su estado/estatus
- Formalmente: `Estado(t+1) = f(Estado(t), Evento)`
- Componentes clave:
  - **Estado**: situación actual del sistema (ej. encendido = 1, apagado = 0)
  - **Evento**: disparador que provoca cambio (ej. presionar botón, recibir señal)
  - **Transición**: cambio de un estado a otro
  - **Acción**: operación que se ejecuta durante/después de una transición

Ejemplo más simple: lámpara con botón
- **Estados**: apagada (0), encendida (1)
- **Evento**: presionar botón
- **Transición**: apagada → encendida o encendida → apagada

**3. Regla fundamental de máquinas de estado**

> "No basta preguntar qué ocurrió, sino **en qué estado estaba el sistema**"

Ejemplo de la cajuela de auto:
- Presionas el botón de abrir cuando la cajuela está cerrada → se abre
- Presionas el botón de abrir cuando la cajuela ya está abierta → NO sucede nada (el evento depende del estado)
- Por eso siempre debe revisarse el estado actual antes de procesar un evento

**4. Ejemplos de máquinas de estado en la vida real**

**Semáforo**:
- **Estados**: Verde → Amarillo → Rojo → Verde (cíclico)
- **Evento**: paso del tiempo
- **Características**: ciclo cerrado (siempre regresa al inicio)

**Puerta automática (entrada de edificio/gimnasio)**:
- **Estados**: Cerrada → Abriendo → Abierta → Cerrando → Cerrada
- **Eventos**: detecta persona, termina de abrir, termina de cerrar
- **Casos especiales**:
  - Persona registrada: pasa directamente a Abierta
  - Persona no registrada: regresa a Cerrada sin abrir
  - Persona en medio: se para en Cerrando y vuelve a Abierta (bifurcación)

**Relevador (componente electrónico)**:
- **Máquina de estados más simple con dos posiciones**
- **Normalmente abierto** vs **normalmente cerrado**
- Se activa con señal de control
- Máquina binaria: 0 (abierto) ↔ 1 (cerrado)

**Elevador**:
- **Estados**: espera en piso, puerta abriendo, puerta abierta, puerta cerrando, puerta cerrada
- **Eventos**: solicitud de piso, timer para cerrar puerta automáticamente

**5. Diagramas de estado (State Diagrams)**

Un diagrama de estado visualiza:
- **Círculos/óvalos**: estados
- **Flechas**: transiciones (con etiqueta de evento)
- **Lazos**: ciclos (cerrados si regresan al origen)

**Lazo cerrado**: seguir el diagrama siempre lleva al mismo punto (máquina cíclica)
**Lazo abierto**: seguir el diagrama lleva a un punto terminal (requiere intervención manual para resetear)

Ejemplo de **puerta automática compleja** con bifurcación:
```
Cerrada
  ↓ (Detecta persona → Abriendo)
Abriendo
  ↓ (Fin de apertura → Abierta)
Abierta
  ├→ (Tiempo transcurrido → Cerrando)
  └→ (Persona sigue en puerta → Abierta NUEVO)
Cerrando
  ├→ (Fin cierre → Cerrada)
  └→ (Detecta obstáculo → Abierta NUEVO)
```

Este diagrama tiene **dos lazos** (uno principal, uno de bifurcación/excepciones).

**6. Tabla de transición de estados**

Forma alternativa de representar máquinas:
| Estado Actual | Evento | Nuevo Estado |
|---|---|---|
| Cerrada | Detecta persona | Abriendo |
| Abriendo | Fin de apertura | Abierta |
| Abierta | Transcurre tiempo (5s) | Cerrando |
| Cerrando | Fin de cierre | Cerrada |
| Cerrando | Detecta obstáculo | Abierta |

Esta representación es útil para:
- Documentación formal
- Validación (buscar estados olvidados)
- Implementación directa en código

**7. Estados especiales: ERROR**

Muchas máquinas agregan un estado de error:
```
Estado Normal → [Falla] → ERROR
ERROR → [Espera N segundos] → Reintentar
Reintentar → [Éxito] → Estado Normal
Reintentar → [Sigue fallando] → ERROR
```

Ejemplo en puerta automática:
- Si la puerta no puede cerrarse (hay algo atrapado), entra a estado ERROR
- Espera 5 segundos
- Vuelve a intentar cerrar
- Si sigue fallando, permanece en ERROR

**8. Implementación en PSeInt usando `Según` (equivalente a `switch`)**

El profesor presentó un ejemplo completo: **lámpara con botón**

Estructura:
```
Algoritmo Lámpara
  Definir estado Como Entero    // 0=apagada, 1=encendida
  Definir botón Como Entero     // 1=presionar, 2=salir
  Definir salir Como Lógico     // Falso = continuar, Verdadero = terminar
  
  estado ← 0                    // Inicio: apagada
  salir ← Falso
  
  Mientras salir = Falso Hacer
    // Reportar estado actual
    Escribir "Estado actual:"
    Según estado Hacer
      Caso 0:
        Escribir "Lámpara APAGADA"
      Caso 1:
        Escribir "Lámpara ENCENDIDA"
    FinSegún
    
    // Leer acción del usuario
    Escribir "Presiona 1 para botón, 2 para salir"
    Leer botón
    
    // Procesar evento (cambio de estado)
    Según botón Hacer
      Caso 1:
        Si estado = 0 Entonces
          estado ← 1          // Apagada → Encendida
        Sino
          estado ← 0          // Encendida → Apagada
        FinSi
      Caso 2:
        salir ← Verdadero     // Terminar ciclo
      Por Defecto:
        Escribir "Opción inválida"
    FinSegún
  FinMientras
  
  Escribir "Programa terminado"
FinAlgoritmo
```

**Conceptos clave en la implementación**:
- **`switch`/`Según`** en C es ideal para máquinas de estado (no es un condicional `if`, sino un **redirector de flujo**)
- Cada `case` representa un estado
- Se revisa el evento dentro de cada estado
- Las transiciones usan asignaciones simples a la variable `estado`

**9. ¿Por qué `switch` es mejor que `if` para máquinas de estado?**

- **`if`**: revisa condiciones (¿se cumple esto?)
- **`switch`**: recibe un valor y lo redirige a un caso específico (más eficiente y claro para máquinas de estado)
- Una máquina de estado es un "grifo" que redirige la señal según el estado actual

**10. Ciclos infinitos en máquinas de estado**

- Normalmente una máquina de estado vive en un **ciclo infinito** (o muy largo)
- Monitorea constantemente el estado de sensores/eventos
- Ejemplo en placas embebidas (Arduino, ESP32):
  ```cpp
  void loop() {
    switch(estado) {
      case 0: // hacer algo
      case 1: // hacer otra cosa
    }
  }
  ```
- El `loop()` se ejecuta indefinidamente revisando sensores

**11. Feedback del profesor sobre el enfoque de enseñanza**

Se realizó una encuesta informal:
- Algunos alumnos sintieron que el ritmo es lento
- Profesor reconoce que máquinas de estado es un tema denso y poco común de enseñar
- Se enfatizó que el objetivo es entender **dónde aplicar** el conocimiento, no solo memorizar código
- Para especialidad automotriz, se promete orientar más los ejemplos hacia sensores y sistemas de vehículos
- Se aceptaron sugerencias (ej. acelerar temas sencillos, profundizar en complejos)

**12. Planes futuros para máquinas de estado**

- **Tarea**: diseñar una máquina de estados básica en pseudocódigo durante el fin de semana
- **Evaluación del Bloque 0**: incluirá proyecto de máquina de estados (será parte del mini-ACU)
- **Requerimientos**: después de máquinas de estado, se enseñará a pasar requerimientos (texto de cliente) a máquinas de estado formales
- **Ejemplo automotriz**: sensor de proximidad trasero, ECU, sistemas de puertas automáticas

## Siguiente paso

**Próxima sesión:** 
1. Revisar tareas de máquinas de estado (fin de semana)
2. Introducir **requerimientos técnicos**: cómo traducir una descripción de cliente a máquina de estados formal
3. Comenzar con diseño del **mini-ACU** (pequeño Sistema de Control Automotriz)
4. Transición hacia **programación en C** (se verá `switch` de verdad)

**Tarea para el fin de semana**: Diseñar una máquina de estados (ej. puerta automática, botón con LED, sensor binario) en pseudocódigo PSeInt. Dibujar diagrama de transiciones.

**Recordatorio importante**: Para la especialidad automotriz, se promete aumentar ejemplos enfocados en vehículos (sensores, ECU, sistemas de control).
