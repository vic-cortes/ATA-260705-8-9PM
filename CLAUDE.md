# CLAUDE.md

Guía para trabajar con código en este repositorio de curso de programación.

## Qué es esto

Repositorio para el **Curso de Programación** (Bloque 0 → Bloque 1):

1. **Bloque 0**: Pensamiento algorítmico y pseudocódigo con **PSeInt** (español)
2. **Bloque 1+**: Programación en **C++** (containerizado con Docker)

No hay build system compartido ni librerías externas. Cada parte (PSeInt, C++) es independiente.

## PSeInt (Bloque 0)

`.psc` files son interpretados por el **PSeInt IDE** o su CLI, sin necesidad de compilación.
Generan flowcharts y manejan I/O interactivo. No hay build steps.

## Convenciones de pseudocódigo (PSeInt)

Código en español. Match existing style cuando edites:

- Wrapper: `Algoritmo <Nombre>` ... `FinAlgoritmo`
- Declaraciones: `Definir <var> Como Entero|Real`, arrays: `Dimension nombre[N]`
- **Índices 1-based** (loops: `Para i <- 1 Hasta 5`)
- Assignment: `<-`; I/O: `Escribir` (print), `Leer` (read)
- Control flow: `Para`/`FinPara`, `Mientras`/`FinMientras`, `Si`/`FinSi`
- Indentación: 1 tab dentro de `Algoritmo`
- Mensajes y prompts en español

## Convenciones de C++ (Bloque 1+)

C++ files (`.cpp`, `.h`, `.hpp`) son compilados con `g++` dentro de Docker.

- Estilo: LLVM + Allman braces (configurado en `.clang-format`)
- Indentación: 4 espacios (no tabs)
- Ancho de línea: 100 caracteres
- Formato automático: `make format-cpp`
- Compilación: `make compile FILE=src/programa.cpp`
- Todas las herramientas vía `make` target (ver sección Docker)

## Sesiones de clase

### Estructura de carpetas

Cada sesión se registra en una carpeta bajo `sessions/week_N/YYYY_MM_DD/` con:
- `resumen.md` — resumen estructurado de puntos principales + metadata YAML
- `raw_transcript.txt` — transcript completo de la sesión (sin editar)

### Resúmenes semanales

Cada semana tiene un archivo `SEMANA_RESUMEN.md` con:
- Contexto general de la semana
- Temas principales por sesión
- Progresión temática
- Hitos y evaluaciones
- Conceptos clave establecidos
- Próximos pasos

### Búsqueda de sesiones

**Resúmenes rápidos por semana:**
- `sessions/week_1/SEMANA_RESUMEN.md` — Bloque 0 (pseudocódigo PSeInt)
- `sessions/week_2/SEMANA_RESUMEN.md` — Bloque 0→1 (Linux + máquinas de estado)

**Resúmenes detallados por sesión individual:**
- `sessions/week_N/YYYY_MM_DD/resumen.md` — Contenido específico de la clase
- `sessions/week_N/YYYY_MM_DD/raw_transcript.txt` — Transcript completo

### Temas principales por bloque

**Bloque 0 (Week 1):**
- Pensamiento algorítmico
- Condicionales y ciclos en PSeInt
- Menús (Según/switch)
- Validación de entrada
- Arreglos (arrays)

**Bloque 0→1 (Week 2):**
- Comandos Linux (terminal)
- Herramientas de desarrollo (WSL, Debian, build-essential)
- **Máquinas de estado** (fundamental para sistemas automotrices)
- Diagramas de transición
- Implementación en PSeInt y C++

## Docker & Makefile (Bloque 1+)

Ambiente containerizado para C++. **Sin instalación local de compiladores.**

**Setup rápido:**

```bash
make setup              # Build image + start container
make docker-shell       # Entrar al contenedor
make format-cpp         # Formatear archivos C++ (como black)
make compile FILE=...   # Compilar un archivo
make docker-down        # Detener contenedor
make help               # Ver todos los targets
```

**Archivos:**
- `Dockerfile` — Imagen con g++, gdb, valgrind, clang-format
- `docker-compose.yml` — Servicio `cpp-curso` con volumen sincronizado
- `.clang-format` — Estilo de código (LLVM + Allman, 4-space, 100 col)
- `DOCKER.md` — Documentación completa

**Desarrollo:** Código en `/workspace` sincronizado en tiempo real. Compila y ejecuta dentro del contenedor.
Misma versión de compilador para todos (sin bugs de "me funciona en mi máquina").

## Máquinas de Estado (State Machines)

Concepto fundamental para especialidad automotriz. Se introduce en **Bloque 0→1**.

### Definición

Una máquina de estado es un sistema que:
- Reporta constantemente su estado/estatus
- Cambia de estado solo en respuesta a eventos
- Fórmula: `Estado(t+1) = f(Estado(t), Evento)`

**Regla de oro:** "No basta preguntar qué ocurrió, sino **en qué estado estaba el sistema**"

### Componentes

- **Estado**: situación actual del sistema (ej. 0=apagado, 1=encendido)
- **Evento**: disparador que provoca cambio (ej. presionar botón, señal de sensor)
- **Transición**: cambio de un estado a otro
- **Acción**: operación ejecutada durante/después de transición

### Representación

**Diagrama de transición:**
- Círculos = estados
- Flechas = transiciones (etiquetadas con evento)
- Lazos = ciclos cerrados (regresan al origen)

**Tabla de transición:**
| Estado Actual | Evento | Nuevo Estado |
|---|---|---|
| Cerrada | Detecta | Abriendo |
| Abriendo | Fin apertura | Abierta |

### Implementación en PSeInt

```pseudocodigo
Algoritmo MáquinaEstado
  Definir estado Como Entero
  Definir evento Como Entero
  Definir activo Como Lógico
  
  estado ← 0      // Estado inicial
  activo ← Verdadero
  
  Mientras activo Hacer
    // Reportar estado
    Según estado Hacer
      Caso 0:
        Escribir "Estado: A"
      Caso 1:
        Escribir "Estado: B"
    FinSegún
    
    // Leer evento
    Leer evento
    
    // Transiciones
    Según estado Hacer
      Caso 0:
        Si evento = 1 Entonces
          estado ← 1
        FinSi
      Caso 1:
        Si evento = 2 Entonces
          estado ← 0
        FinSi
    FinSegún
  FinMientras
FinAlgoritmo
```

### Casos de uso automotrices

- Sensores binarios (encendido/apagado)
- Puertas automáticas (cerrada → abriendo → abierta → cerrando)
- Relevadores (abierto ↔ cerrado)
- Sistemas de control (ECU con múltiples estados)
- Tratamiento de errores (normal → error → reintentar → normal)

### Ciclos infinitos en embebidos

En Arduino/ESP32, las máquinas de estado viven en `loop()`:
```cpp
void loop() {
  switch(estado) {
    case 0: /* hacer algo */ break;
    case 1: /* hacer otra cosa */ break;
  }
}
```

El loop se ejecuta indefinidamente monitoreando sensores y eventos.

## 🔍 Índice del Proyecto (Codebase Memory MCP)

El proyecto está **indexado** con `codebase-memory-mcp`. Para cualquier consulta sobre la estructura, arquitectura o contenido del proyecto, usa las siguientes herramientas:

### Herramientas Disponibles

**1. Explorar la Arquitectura:**
```bash
get_architecture(aspects=['all'])
```
- Ver estructura general del proyecto
- Componentes principales
- Dependencias

**2. Buscar Funciones/Clases/Archivos:**
```bash
search_graph(name_pattern="*turniquete*")
search_graph(label="file")
```
- Encontrar archivos por patrón
- Localizar funciones/clases
- Buscar por etiquetas

**3. Obtener Código Específico:**
```bash
get_code_snippet(qualified_name="Algoritmo_Torniquete")
```
- Extraer código exacto de una función/archivo
- Obtener rangos de líneas específicas

**4. Rastrear Llamadas y Flujos:**
```bash
trace_path("function_name", mode="calls")
trace_path("function_name", mode="data_flow")
```
- Ver qué llama a una función
- Entender flujos de datos
- Analizar dependencias

**5. Buscar en el Código:**
```bash
search_code("máquina de estado")
search_code("torniquete")
```
- Búsqueda de texto en todo el proyecto
- Patrones de código

### Archivo de Índice

- **Ubicación:** `.codebase-memory/graph.db.zst`
- **Tipos:** 278 nodos, 276 relaciones
- **Contenido:** Estructura completa del proyecto indexada
- **Compartible:** Commit este archivo para compartir el índice con el equipo

### Cuándo Usar

✅ **Úsalo para:**
- Explorar la estructura del proyecto
- Encontrar archivos/funciones específicas
- Entender relaciones entre componentes
- Analizar dependencias
- Localizar código relacionado
- Auditoría de código

❌ **No lo uses para:**
- Leer contenido de archivos (usa `Read` directamente)
- Ediciones (edita con `Edit`)
- Operaciones de git (usa `Bash`)

### Ejemplo de Consulta

**"¿Dónde está definida la máquina de estados del torniquete?"**
```
search_graph(name_pattern="*torniquete*")
→ Encuentras los archivos .psc
```

**"¿Qué archivos usan máquinas de estado?"**
```
search_code("Segun estado Hacer")
→ Encuentras todos los archivos con esta patrón
```

**"¿Cuál es la estructura completa del proyecto?"**
```
get_architecture(aspects=['all'])
→ Ves toda la arquitectura indexada
```
