# Torniquete - Máquina de Estados en Python

## Descripción

Implementación en Python de una máquina de estados que emula un torniquete de acceso (turnstile).

- **Estados**: BLOQUEADO (0), DESBLOQUEADO (1)
- **Eventos**: Moneda (1), Empujar (2), Salir (0)
- **Funcionalidad**: Control de acceso con contador de personas

## Archivos

### 1. `torniquete.py` (4.8 KB, 159 líneas)

Script Python con:
- Clase `Torniquete` con máquina de estados
- Enum para estados y eventos
- Interfaz interactiva en terminal
- Contador de personas que pasaron

**Características:**
- ✅ OOP con clases y enums
- ✅ Tabla de transiciones implementada
- ✅ Interfaz amigable con emojis
- ✅ Auditoría (contador de pasos)
- ✅ Fácil de depurar

## Ejecución

### Opción 1: Terminal Directa

```bash
python3 /Users/vic/Documents/repos/github/personal/ATA-260705-8-9PM/sessions/week_2/torniquete.py
```

### Opción 2: VS Code con Debug

**Usando launch.json:**

1. Abre VS Code en la carpeta del proyecto
2. Ve a **Run and Debug** (Ctrl+Shift+D)
3. Selecciona **Python: Torniquete**
4. Presiona **F5** o click en ▶️

**Configuraciones disponibles:**

- **Python: Torniquete** - Ejecuta `torniquete.py` directamente
- **Python: Current File** - Ejecuta el archivo actualmente abierto
- **Python: Debug with Args** - Ejecuta con argumentos personalizados

## Debug en VS Code

### Puntos de Interrupción

1. Haz click en el número de línea para crear un breakpoint
2. Aparecerá un punto rojo
3. Ejecuta con F5
4. El programa se pausará en ese punto

### Controles de Debug

| Tecla | Acción |
|-------|--------|
| F5 | Continuar / Ejecutar |
| F10 | Paso siguiente (Step Over) |
| F11 | Entrar en función (Step Into) |
| Shift+F11 | Salir de función (Step Out) |
| Ctrl+Shift+D | Abrir Debug |
| Shift+Ctrl+L | Agregar breakpoint |

### Variables durante Debug

En la sección **Variables** (lado izquierdo) puedes ver:
- `self.estado` - Estado actual del torniquete
- `self.contador_pasos` - Contador de personas
- `self.activo` - Estado del programa

## Ejemplo de Uso

```
========================================
MÁQUINA DE ESTADOS: TORNIQUETE
========================================

Estado actual: 🔒 BLOQUEADO
Pasos registrados: 0

Eventos disponibles:
  1 = Insertar moneda
  2 = Empujar torniquete
  0 = Salir

Ingresa evento: 2

❌ ACCESO DENEGADO
⚠️  El torniquete está bloqueado
⚠️  Inserta una moneda para desbloquear

Estado actual: 🔒 BLOQUEADO
Pasos registrados: 0

Eventos disponibles:
  1 = Insertar moneda
  2 = Empujar torniquete
  0 = Salir

Ingresa evento: 1

💰 Moneda insertada
✓ Torniquete DESBLOQUEADO - Puedes pasar

Estado actual: 🔓 DESBLOQUEADO
Pasos registrados: 0

Eventos disponibles:
  1 = Insertar moneda
  2 = Empujar torniquete
  0 = Salir

Ingresa evento: 2

✅ Paso registrado
👤 Persona #1 pasó
🔒 Torniquete BLOQUEADO nuevamente

========================================
RESUMEN FINAL
========================================
Total de personas que pasaron: 1
Estado final: BLOQUEADO
========================================
```

## Tabla de Transiciones

| Estado | Evento | Acción | Nuevo Estado |
|--------|--------|--------|---|
| BLOQUEADO | Moneda | Permitir paso | DESBLOQUEADO |
| BLOQUEADO | Empujar | Denegar paso | BLOQUEADO |
| DESBLOQUEADO | Empujar | Registrar paso | BLOQUEADO |
| DESBLOQUEADO | Moneda | Mantener desbloqueado | DESBLOQUEADO |

## Estructura del Código

### Clase Torniquete

```python
class Torniquete:
    def __init__(self)                  # Inicializar
    def mostrar_estado(self) -> str     # Representación del estado
    def procesar_evento(self, evento)   # Procesar evento
    def mostrar_menu(self) -> None      # Menú de opciones
    def mostrar_resumen(self) -> None   # Resumen final
    def ejecutar(self) -> None          # Ciclo principal interactivo
```

### Enums

```python
class Estado(Enum):
    BLOQUEADO = 0
    DESBLOQUEADO = 1

class Evento(Enum):
    MONEDA = 1
    EMPUJAR = 2
    SALIR = 0
```

## Debugging Tips

### 1. Ver estado en cada iteración

Agrega un breakpoint en `procesar_evento()` para ver cómo cambia el estado.

### 2. Verificar transiciones

Inspecciona `self.estado` antes y después de `procesar_evento()`.

### 3. Monitorear contador

Observa `self.contador_pasos` para verificar que se incrementa correctamente.

### 4. Rastrear flujo

Usa **Step Over** (F10) para avanzar línea por línea.

## Comparación: PSeInt vs Python

| Aspecto | PSeInt | Python |
|---------|--------|--------|
| **Sintaxis** | Mientras/Según | while/if/switch |
| **Tipos** | Débiles | Fuertes (Enum) |
| **OOP** | No | Sí (Clases) |
| **Debug** | Limitado | Completo (VS Code) |
| **Performance** | Lento | Rápido |
| **Para aprender** | Excelente | Muy bien |

## Próximos Pasos

1. **Ejecuta el programa** y prueba todos los casos
2. **Agrega breakpoints** y experimenta con el debugger
3. **Modifica el código** para agregar nuevas características
4. **Extiende la máquina** con más estados/eventos

## Variaciones Posibles

- **Timeout**: Bloquear automáticamente después de 30 segundos
- **Bidireccional**: Entrada y salida separadas
- **Errores**: Estado ERROR cuando se atasca
- **Logging**: Registrar todas las transiciones en archivo

## Archivos Relacionados

- `torniquete.psc` - Versión en pseudocódigo PSeInt
- `torniquete_simple.psc` - Versión simplificada de PSeInt
- `torniquete_multiples_lenguajes.md` - Implementaciones en C++
- `torniquete_solucion.md` - Documentación completa
- `maquinas_de_estado_complementario.md` - Material educativo

---

**Creado**: 19/07/2026  
**Propósito**: Implementación educativa de máquinas de estado  
**Nivel**: Bloque 0→1 (Transición a C++)
