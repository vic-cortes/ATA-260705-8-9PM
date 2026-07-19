# Solución: Máquina de Estados del Torniquete

## Descripción

Pseudocódigo que emula un torniquete (turnstile) con dos estados:
- **Bloqueado**: No permite el paso
- **Desbloqueado**: Permite el paso

## Tabla de Transiciones

| Estado Actual | Evento | Siguiente Estado | Acción |
|---|---|---|---|
| Bloqueado | Moneda | Desbloqueado | Permitir paso |
| Bloqueado | Empujar | Bloqueado | Denegar paso |
| Desbloqueado | Empujar | Bloqueado | Registrar paso |
| Desbloqueado | Moneda | Desbloqueado | Mantener desbloqueado |

---

## Pseudocódigo PSeInt - Solución Completa

```pseudocodigo
Algoritmo Torniquete
  Definir estado Como Entero              // 0 = Bloqueado, 1 = Desbloqueado
  Definir evento Como Entero              // 1 = Moneda, 2 = Empujar
  Definir salir Como Lógico
  Definir contador_pasos Como Entero
  
  // Inicialización
  estado ← 0                              // Estado inicial: Bloqueado
  salir ← Falso
  contador_pasos ← 0
  
  Escribir "╔════════════════════════════════════╗"
  Escribir "║     MÁQUINA DE ESTADOS TORNIQUETE  ║"
  Escribir "╚════════════════════════════════════╝"
  
  Mientras salir = Falso Hacer
    // Mostrar estado actual
    Escribir ""
    Escribir "────────────────────────────────────"
    Si estado = 0 Entonces
      Escribir "🔒 ESTADO ACTUAL: BLOQUEADO"
    Sino
      Escribir "🔓 ESTADO ACTUAL: DESBLOQUEADO"
    FinSi
    Escribir "────────────────────────────────────"
    
    // Mostrar estadísticas
    Escribir "Pasos registrados: " contador_pasos
    Escribir "────────────────────────────────────"
    
    // Menú de eventos
    Escribir "Eventos disponibles:"
    Escribir "1 = Insertar moneda"
    Escribir "2 = Empujar torniquete"
    Escribir "0 = Salir"
    Escribir "Selecciona evento: " Sin Saltar
    Leer evento
    
    Escribir ""
    
    // MÁQUINA DE ESTADOS: Procesar evento según estado actual
    Según estado Hacer
      
      // ============================================
      // ESTADO 0: BLOQUEADO
      // ============================================
      Caso 0:
        Según evento Hacer
          
          // Evento: Insertar moneda en estado Bloqueado
          Caso 1:
            Escribir "💰 Moneda insertada"
            Escribir "✓ Torniquete DESBLOQUEADO - Puedes pasar"
            estado ← 1                  // Transición: Bloqueado → Desbloqueado
            
          // Evento: Empujar en estado Bloqueado
          Caso 2:
            Escribir "❌ ACCESO DENEGADO - El torniquete está bloqueado"
            Escribir "⚠️  Inserta una moneda para desbloquear"
            // No cambia de estado, permanece en Bloqueado (0)
            
          // Salir
          Caso 0:
            salir ← Verdadero
            Escribir "👋 Programa terminado"
            
          // Opción inválida
          Por Defecto:
            Escribir "❌ Evento inválido"
        FinSegún
      
      // ============================================
      // ESTADO 1: DESBLOQUEADO
      // ============================================
      Caso 1:
        Según evento Hacer
          
          // Evento: Empujar en estado Desbloqueado
          Caso 2:
            Escribir "✅ Paso registrado"
            contador_pasos ← contador_pasos + 1
            Escribir "🔒 Torniquete BLOQUEADO nuevamente"
            estado ← 0                  // Transición: Desbloqueado → Bloqueado
            
          // Evento: Insertar moneda en estado Desbloqueado
          Caso 1:
            Escribir "💰 Moneda insertada"
            Escribir "ℹ️  Ya está desbloqueado - Puedes pasar"
            // No cambia de estado, permanece en Desbloqueado (1)
            
          // Salir
          Caso 0:
            salir ← Verdadero
            Escribir "👋 Programa terminado"
            
          // Opción inválida
          Por Defecto:
            Escribir "❌ Evento inválido"
        FinSegún
      
    FinSegún
    
  FinMientras
  
  // Resumen final
  Escribir ""
  Escribir "╔════════════════════════════════════╗"
  Escribir "║           RESUMEN FINAL            ║"
  Escribir "╚════════════════════════════════════╝"
  Escribir "Total de personas que pasaron: " contador_pasos
  Escribir "Estado final: " Si estado = 0 Entonces "BLOQUEADO" Sino "DESBLOQUEADO" FinSi
  
FinAlgoritmo
```

---

## Comparación con Máquina de la Lámpara

### Similitudes

| Aspecto | Lámpara | Torniquete |
|---------|---------|-----------|
| **Estructura base** | `Mientras ... Hacer` + `Según estado` | `Mientras ... Hacer` + `Según estado` |
| **Estados** | 2 (Apagada, Encendida) | 2 (Bloqueado, Desbloqueado) |
| **Variable de control** | `salir` booleano | `salir` booleano |
| **Eventos** | 1 evento (Botón) | 2 eventos (Moneda, Empujar) |
| **Transiciones** | Anidadas en `Según estado` | Anidadas en `Según estado` |

### Diferencias

| Aspecto | Lámpara | Torniquete |
|---------|---------|-----------|
| **Complejidad** | 1 evento que alterna estados | 2 eventos, diferentes acciones por estado |
| **Tabla de transiciones** | 2×1 (2 estados, 1 evento) | 2×2 (2 estados, 2 eventos) |
| **Lógica** | Simple: toggle siempre | Más compleja: contexto importante |
| **Contador** | No tiene | Sí (contador_pasos) |
| **Caso especial** | Misma acción en ambos estados | Acciones diferentes por combinación |

### Código de Lámpara (Para Referencia)

```pseudocodigo
Algoritmo Lampara
  Definir estado Como Entero
  Definir botón Como Entero
  Definir salir Como Lógico
  
  estado ← 0
  salir ← Falso
  
  Mientras salir = Falso Hacer
    Escribir "Estado: " Si estado = 0 Entonces "APAGADA" Sino "ENCENDIDA" FinSi
    Escribir "1 = Botón, 2 = Salir"
    Leer botón
    
    Según estado Hacer
      Caso 0:
        Si botón = 1 Entonces
          estado ← 1
          Escribir "✓ Lámpara encendida"
        Sino
          salir ← Verdadero
        FinSi
      
      Caso 1:
        Si botón = 1 Entonces
          estado ← 0
          Escribir "✓ Lámpara apagada"
        Sino
          salir ← Verdadero
        FinSi
    FinSegún
  FinMientras
FinAlgoritmo
```

---

## Ejemplo de Ejecución

```
╔════════════════════════════════════╗
║     MÁQUINA DE ESTADOS TORNIQUETE  ║
╚════════════════════════════════════╝

────────────────────────────────────
🔒 ESTADO ACTUAL: BLOQUEADO
────────────────────────────────────
Pasos registrados: 0
────────────────────────────────────
Eventos disponibles:
1 = Insertar moneda
2 = Empujar torniquete
0 = Salir
Selecciona evento: 2

❌ ACCESO DENEGADO - El torniquete está bloqueado
⚠️  Inserta una moneda para desbloquear

────────────────────────────────────
🔒 ESTADO ACTUAL: BLOQUEADO
────────────────────────────────────
Pasos registrados: 0
────────────────────────────────────
Eventos disponibles:
1 = Insertar moneda
2 = Empujar torniquete
0 = Salir
Selecciona evento: 1

💰 Moneda insertada
✓ Torniquete DESBLOQUEADO - Puedes pasar

────────────────────────────────────
🔓 ESTADO ACTUAL: DESBLOQUEADO
────────────────────────────────────
Pasos registrados: 0
────────────────────────────────────
Eventos disponibles:
1 = Insertar moneda
2 = Empujar torniquete
0 = Salir
Selecciona evento: 2

✅ Paso registrado
🔒 Torniquete BLOQUEADO nuevamente

────────────────────────────────────
🔓 ESTADO ACTUAL: DESBLOQUEADO
────────────────────────────────────
Pasos registrados: 1
────────────────────────────────────
...
```

---

## Análisis de Transiciones

### De Estado BLOQUEADO (0)

```
BLOQUEADO + Moneda → DESBLOQUEADO (acción: permitir paso)
BLOQUEADO + Empujar → BLOQUEADO (acción: denegar paso)
```

**Interpretación:**
- La moneda es el "permiso" para pasar
- Empujar sin moneda no hace nada (máquina permanece bloqueada)

### De Estado DESBLOQUEADO (1)

```
DESBLOQUEADO + Empujar → BLOQUEADO (acción: registrar paso)
DESBLOQUEADO + Moneda → DESBLOQUEADO (acción: mantener desbloqueado)
```

**Interpretación:**
- Empujar es la acción de "pasar" → automáticamente se bloquea
- Insertar más moneda no tiene efecto (ya estaba permitido)

---

## Pseudocódigo Alternativo (Con Comentarios Detallados)

```pseudocodigo
Algoritmo Torniquete_Comentado
  // Variables de estado
  Definir estado Como Entero              // Máquina de estados actual
  Definir evento Como Entero              // Evento generado por usuario
  Definir salir Como Lógico               // Condición de terminación
  Definir contador_pasos Como Entero      // Auditoría: cuántas personas pasaron
  
  // Inicialización de máquina de estados
  estado ← 0                              // Estado inicial siempre: BLOQUEADO
  salir ← Falso                           // Ciclo continúa hasta que sea verdadero
  contador_pasos ← 0                      // Ninguna persona ha pasado aún
  
  // Ciclo principal de máquina de estados
  Mientras salir = Falso Hacer
    
    // PASO 1: Reportar estado actual al usuario
    Escribir "Estado actual: " Si estado = 0 Entonces "BLOQUEADO" Sino "DESBLOQUEADO" FinSi
    
    // PASO 2: Leer evento del usuario
    Escribir "¿Qué sucede?"
    Escribir "1 = Insertar moneda"
    Escribir "2 = Empujar"
    Leer evento
    
    // PASO 3: Procesar transición
    // La transición depende TANTO del estado actual COMO del evento
    Según estado Hacer
      
      // RAMA 1: Si estamos en BLOQUEADO
      Caso 0:
        Según evento Hacer
          // Sub-caso: Moneda en BLOQUEADO → DESBLOQUEADO
          Caso 1:
            estado ← 1
            Escribir "✓ Permitir paso"
          // Sub-caso: Empujar en BLOQUEADO → se mantiene BLOQUEADO
          Caso 2:
            Escribir "✗ Denegar paso"
        FinSegún
      
      // RAMA 2: Si estamos en DESBLOQUEADO
      Caso 1:
        Según evento Hacer
          // Sub-caso: Empujar en DESBLOQUEADO → BLOQUEADO
          Caso 2:
            contador_pasos ← contador_pasos + 1
            estado ← 0
            Escribir "✓ Registrar paso"
          // Sub-caso: Moneda en DESBLOQUEADO → se mantiene DESBLOQUEADO
          Caso 1:
            Escribir "ℹ️  Ya está permitido"
        FinSegún
      
    FinSegún
    
  FinMientras
  
  Escribir "Total personas: " contador_pasos
  
FinAlgoritmo
```

---

## Puntos Clave Aprendidos

### 1. **Tabla de Transiciones es Crítica**

La tabla proporcionada es la "receta" de la máquina:
```
(Estado, Evento) → Nuevo Estado + Acción
```

Seguirla exactamente evita errores de lógica.

### 2. **Dos Niveles de Decisión**

```pseudocodigo
Según estado Hacer
  Caso 0:
    Según evento Hacer
      // Decisión anidada
    FinSegún
FinSegún
```

Primero: "¿En qué estado estoy?"  
Segundo: "¿Qué evento ocurrió?"  
Resultado: Transición correcta

### 3. **Acciones son Independientes de Transición**

- Transición: cambio de estado (`estado ← nuevo`)
- Acción: lo que "hace" la máquina (`Escribir`, `contador ← ...`)

Ambas ocurren juntas, pero son conceptualmente distintas.

### 4. **Estados sin Cambio**

Hay casos donde el evento ocurre pero el estado NO cambia:
```
BLOQUEADO + Empujar → BLOQUEADO (no transiciona)
DESBLOQUEADO + Moneda → DESBLOQUEADO (no transiciona)
```

Esto es **válido y esperado** en máquinas reales.

---

## Variaciones Posibles (Para Ampliar Aprendizaje)

### Versión 1: Torniquete con Timeout
```pseudocodigo
// Agregar: si pasan 5 segundos desbloqueado sin empujar, volver a bloquear
```

### Versión 2: Torniquete Bidireccional
```pseudocodigo
// Estados: Bloqueado entrada, Bloqueado salida, Desbloqueado
// Eventos: Moneda entrada, Moneda salida, Empujar, Detecta persona
```

### Versión 3: Torniquete con Error
```pseudocodigo
// Estados adicionales: ERROR (si se atasca)
// Evento: Falla mecánica
// Acción: Alertar al personal de mantenimiento
```

---

## Checklist de Comprensión

- ✅ Entiendo la tabla de transiciones
- ✅ Sé por qué hay dos `Según` (anidados)
- ✅ Reconozco cuándo cambia de estado vs. cuándo no
- ✅ Puedo identificar acciones vs. transiciones
- ✅ Podría dibujar el diagrama de estados
- ✅ Podría modificar la máquina para agregar un estado nuevo

---

## Resumen

La máquina de estados del torniquete es un ejemplo **ligeramente más complejo** que la lámpara porque:

1. Tiene **dos eventos distintos** (no uno que alterna)
2. Requiere **tomar decisiones contextuales** (la misma moneda tiene efecto diferente según si está bloqueado o no)
3. Incluye **auditoría** (contador de pasos)
4. Modela un **sistema real** (acceso a lugares)

Es el patrón perfecto para entender máquinas de estado en sistemas embebidos automotrices, donde:
- Los sensores generan eventos variados
- El mismo evento puede significar cosas diferentes según el estado actual
- Se necesita registrar (logging) lo que sucede
