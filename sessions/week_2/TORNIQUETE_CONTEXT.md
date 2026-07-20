# Contexto: Máquina de Estados del Torniquete

## Resumen

Implementación educativa de una máquina de estados que emula un torniquete de acceso (turnstile). Disponible en múltiples lenguajes para comparar enfoques.

**Fecha creación**: 19/07/2026  
**Bloque**: 0→1 (Transición de PSeInt a C++)  
**Temas**: Máquinas de estado, transiciones, auditoría

---

## Archivos del Proyecto

### Pseudocódigo (PSeInt)
- **`torniquete.psc`** (95 líneas)
  - Versión completa con interfaz visual
  - Usa `Si/FinSi` para máquina de estados
  - Ejecutable en extensión PSeInt de VS Code
  - Sintaxis compatible con PSeInt web y local

- **`torniquete_simple.psc`** (50 líneas)
  - Versión minimalista
  - Misma lógica, menos output
  - Ideal para aprender la esencia

### Python (OOP + Debugging)
- **`torniquete.py`** (159 líneas)
  - Clase `Torniquete` con máquina de estados
  - Enums tipo-seguros: `Estado`, `Evento`
  - Interfaz interactiva en terminal
  - Debuggable en VS Code

- **`.vscode/launch.json`**
  - 3 configuraciones de debug
  - Target: `torniquete.py`
  - Completo con integración de terminal

### Documentación
- **`torniquete_solucion.md`** (444 líneas)
  - Solución completa en pseudocódigo
  - Comparación PSeInt ↔ Lámpara
  - Análisis de transiciones
  - Ejemplos de ejecución

- **`torniquete_multiples_lenguajes.md`** (554 líneas)
  - Implementaciones: PSeInt, Python, C++
  - Versiones simples → avanzadas
  - Comparativa de lenguajes
  - Ejercicios prácticos

- **`README_TORNIQUETE.md`** (Nuevo)
  - Guía de uso y ejecución
  - Tutorial de debugging en VS Code
  - Tips y variaciones
  - Estructura del código

- **`maquinas_de_estado_complementario.md`** (923 líneas)
  - Material educativo profundo
  - Teoría de FSM
  - Ejercicios progresivos
  - Casos de uso automotrices

---

## Tabla de Transiciones

| Estado | Evento | Acción | Nuevo Estado |
|--------|--------|--------|---|
| BLOQUEADO (0) | Moneda (1) | Permitir paso | DESBLOQUEADO (1) |
| BLOQUEADO (0) | Empujar (2) | Denegar paso | BLOQUEADO (0) |
| DESBLOQUEADO (1) | Empujar (2) | Registrar paso | BLOQUEADO (0) |
| DESBLOQUEADO (1) | Moneda (1) | Mantener desbloqueado | DESBLOQUEADO (1) |

---

## Cómo Usar

### Ejecutar en Terminal
```bash
# PSeInt
# Abrir en extensión de VS Code o IDE de PSeInt

# Python
python3 sessions/week_2/torniquete.py
```

### Debugging en VS Code

**Setup:**
1. Asegúrate que `.vscode/launch.json` exista (ya está incluido)
2. Instala extensión Python de Microsoft (si no la tienes)

**Ejecutar:**
1. Ve a **Run and Debug** (`Ctrl+Shift+D`)
2. Selecciona **Python: Torniquete**
3. Presiona **F5**

**Debugging:**
- **F10**: Siguiente línea
- **F11**: Entrar en función
- **Shift+F11**: Salir de función
- Click en línea de código: crear/remover breakpoint

---

## Concepto Central: Máquina de Estados

```
ENTRADA (Evento)
    ↓
┌─────────────────────┐
│ Estado Actual       │
│ + Evento            │
│ = Transición        │
└─────────────────────┘
    ↓
SALIDA (Nuevo Estado + Acción)
    ↓
┌─────────────────────┐
│ Reportar Estado     │
│ Ejecutar Acción     │
│ Repetir             │
└─────────────────────┘
```

### Regla de Oro
> "No basta preguntar qué ocurrió, sino **en qué estado estaba el sistema**"

La misma moneda tiene diferente efecto en BLOQUEADO vs DESBLOQUEADO.

---

## Estructura del Código Python

```python
class Torniquete:
    estado: Estado              # 0=BLOQUEADO, 1=DESBLOQUEADO
    contador_pasos: int         # Auditoría
    activo: bool                # Control del loop
    
    def procesar_evento(evento: Evento) -> str:
        # Tabla de transiciones
        if estado == BLOQUEADO:
            if evento == MONEDA:
                estado = DESBLOQUEADO  # Transición
                return "✓ Desbloqueado"  # Acción
            elif evento == EMPUJAR:
                return "✗ Denegar"      # Sin transición
        
        elif estado == DESBLOQUEADO:
            if evento == EMPUJAR:
                contador_pasos += 1
                estado = BLOQUEADO
                return f"✓ Paso #{contador_pasos}"
```

---

## Comparativa: PSeInt vs Python

| Aspecto | PSeInt | Python |
|---------|--------|--------|
| **Lenguaje** | Pseudocódigo (español) | Programación real |
| **Paradigma** | Procedural | OOP + Functional |
| **Tipos** | Débiles | Fuertes (Enum) |
| **Debug** | IDE básico | VS Code completo |
| **Performance** | Intérprete lento | CPython rápido |
| **Para Aprender** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| **Para Producción** | ❌ | ✅ |

---

## Ejemplo de Ejecución

### Caso 1: Acceso Denegado
```
Estado: BLOQUEADO
Evento: Empujar
Resultado: ❌ ACCESO DENEGADO (no cambia estado)
```

### Caso 2: Acceso Permitido
```
Estado: BLOQUEADO
Evento: Moneda
Resultado: ✓ DESBLOQUEADO (transición)

Estado: DESBLOQUEADO
Evento: Empujar
Resultado: ✅ Paso registrado (vuelve a BLOQUEADO)
```

---

## Extensiones Sugeridas

### Nivel 1: Básico
- [ ] Agregar timeout (auto-bloqueo después de 30s)
- [ ] Persistencia (guardar contador en archivo)
- [ ] Logging (registrar todas las transiciones)

### Nivel 2: Intermedio
- [ ] Torniquete bidireccional (entrada/salida)
- [ ] Estado de error (máquina se atasca)
- [ ] Validación de moneda (denominación diferente)

### Nivel 3: Avanzado
- [ ] Máquina de estados con tipos genéricos
- [ ] Test suite (unittest)
- [ ] Diagramas automáticos (graphviz)

---

## Archivos Relacionados

- `CLAUDE.md` — Guía general del repositorio (ahora incluye sección Torniquete)
- `SESIONES.md` — Índice de todas las sesiones
- `sessions/week_2/SEMANA_RESUMEN.md` — Resumen de Week 2
- `sessions/week_2/2026_07_16/resumen.md` — Sesión donde se introduce máquinas de estado

---

## Uso en Clase

### Bloque 0 (Pseudocódigo)
- Estudiante aprende máquinas de estado con PSeInt
- Visual y conceptual
- Enfoque en lógica, no en sintaxis

### Bloque 1 (C++)
- Implementación real en lenguaje compilado
- Enums y tipos seguros
- Preparación para embebidos automotrices

### Bonus: Python
- Puente entre conceptual y real
- OOP y debugging
- Fácil de experimentar

---

**Creado**: 19/07/2026  
**Última actualización**: 19/07/2026  
**Versión**: 1.0
