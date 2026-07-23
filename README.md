# Curso de Programación - ATA-260705-8-9PM

Repositorio oficial del **Curso de Programación** (Bloque 0 → Bloque 1+) impartido por Óscar Godíz.

## Estructura

```
├── sessions/
│   ├── week_1/          # Bloque 0: Pseudocódigo PSeInt
│   │   ├── SEMANA_RESUMEN.md
│   │   ├── 2026_07_06/, 2026_07_07/, 2026_07_08/, 2026_07_09/
│   │   └── Ejercicios: MenuCalificaciones, validación, arrays
│   │
│   ├── week_2/          # Bloque 0→1: Linux + Máquinas de estado
│   │   ├── SEMANA_RESUMEN.md
│   │   ├── 2026_07_13/, 2026_07_14/, 2026_07_15/, 2026_07_16/
│   │   └── Temas: Terminal Linux, state machines, setup C++
│   │
│   └── week_3/          # Bloque 1: ECU y sistemas automotrices
│       ├── SEMANA_RESUMEN.md
│       ├── ECU_CONTEXT.md
│       ├── 2026_07_20/, 2026_07_21/
│       └── excercise/   # Implementación ECU en Python (ecu.py, variables.py, utils.py)
│
├── CLAUDE.md            # Guía para desarrollo en este repo
├── Dockerfile           # Ambiente C++ containerizado
├── docker-compose.yml
├── .clang-format        # Estilo de código (LLVM + Allman)
└── Makefile             # Automatización de compilación/formato

```

## Bloques

### Bloque 0: Pensamiento Algorítmico (PSeInt)
- Estructura entrada → proceso → salida
- Condicionales, ciclos, menús
- Arreglos y validación
- **Evaluación**: Proyecto pseudocódigo en equipos

### Bloque 1+: Programación en C++
- Comandos Linux (terminal)
- **Máquinas de estado** (state machines)
- Compilación y debugging
- Estructuras de datos
- Especialización: Vehículos o IA

### Bloque 1: ECU - Sistemas Automotrices
- **ECU (Electronic Control Unit)**: arquitectura y roles
- Gateway vs Control: validación y decisión
- Señales, mensajes y validación de rangos
- Máquina de estados del ECU (INIT → SELF_TEST → OPERATIONAL → ...)
- Implementación en Python (`sessions/week_3/excercise/`)
- **Evaluación**: Diseño de ACU (equipos)

## 📖 Navegación de Sesiones

- **[SESIONES.md](SESIONES.md)** ⭐ — Índice centralizado de todas las sesiones por semana, fecha y tema
- **[CLAUDE.md](CLAUDE.md)** — Convenciones de código, estructura del proyecto, máquinas de estado

### Resúmenes Semanales

- [Week 1 - Bloque 0](sessions/week_1/SEMANA_RESUMEN.md) — Pseudocódigo PSeInt
- [Week 2 - Bloque 0→1](sessions/week_2/SEMANA_RESUMEN.md) — Linux + Máquinas de estado
- [Week 3 - Bloque 1](sessions/week_3/SEMANA_RESUMEN.md) — ECU y sistemas automotrices