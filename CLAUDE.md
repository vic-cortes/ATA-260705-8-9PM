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

Cada sesión se registra en una carpeta bajo `week_N/YYYY_MM_DD/` con:
- `resumen.md` — resumen estructurado de puntos principales
- `raw_transcript.txt` — transcript completo de la sesión

**Búsqueda rápida:** Consulta [SESIONES.md](SESIONES.md) para un índice de todas las sesiones
por bloque, fecha y tema. Incluye links diretos a resúmenes y transcripts.

**Estructura de resúmenes:** Los archivos `resumen.md` incluyen metadata YAML al inicio
(fecha, bloque, duración, participantes) seguida de puntos principales y siguiente paso.

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
