# Docker setup para Curso de C++

Ambiente containerizado para desarrollar y compilar programas en C++ durante el curso.

## Requisitos

- Docker y Docker Compose instalados
- Mac M1/M2/M3 (o cambiar `linux/arm64` a `linux/amd64` en el Dockerfile)

## Quick Start

**Con Makefile (recomendado):**

```bash
# Setup completo (build + up)
make setup

# Entrar al contenedor
make docker-shell

# Formatear archivos C++
make format-cpp
```

**Manual con docker-compose:**

```bash
# Construir la imagen (primera vez)
docker-compose build

# Iniciar el contenedor
docker-compose up -d

# Entrar interactivo
docker-compose run --rm cpp-course bash
```

## Compilar un programa C++

Dentro del contenedor:

```bash
cd /workspace
g++ -o programa programa.cpp
./programa
```

O desde afuera (Mac/Linux):

```bash
docker-compose exec cpp-course g++ -o programa src/programa.cpp
docker-compose exec cpp-course ./programa
```

## Herramientas disponibles

- **g++/gcc** — Compiladores C/C++
- **make** — Build automation
- **gdb** — Debugger
- **valgrind** — Memory analysis
- **git** — Control de versiones
- **vim/nano** — Editores de texto

## Volúmenes

- `/workspace` → Tu carpeta del proyecto (sincronizado en tiempo real)
- `/root/.bash_history` → Histórico de comandos (persistente)

## Detener el contenedor

```bash
docker-compose down
```

## Limpiar todo

```bash
docker-compose down -v  # Elimina volúmenes también
docker system prune     # Limpia imágenes no usadas
```

## Troubleshooting

**Error: "Cannot connect to Docker daemon"**
- Verifica que Docker está corriendo: `docker info`

**Error: "Platform linux/arm64 not supported"**
- Cambiar en Dockerfile: `FROM debian:bookworm-slim` (sin `--platform`)

**El contenedor se cierra inmediatamente**
- Usar `-it` flags para terminal interactiva

## Compilar y ejecutar un programa de ejemplo

```bash
# Desde tu Mac/terminal
docker-compose run --rm cpp-course bash -c "
  cd /workspace
  g++ -Wall -Wextra -o hello src/hello.cpp
  ./hello
"
```

## Makefile - Comandos útiles

El proyecto incluye un Makefile para simplificar tareas comunes:

```bash
make help              # Ver todos los targets disponibles
make docker-build      # Construir imagen Docker
make docker-up         # Iniciar contenedor
make docker-down       # Detener contenedor
make docker-shell      # Entrar a shell interactivo
make setup             # Build + Up (setup completo)
make status            # Ver estado del contenedor
make format-cpp        # Formatear archivos C++ (como black en Python)
make compile FILE=...  # Compilar un archivo específico
make clean             # Limpiar archivos compilados (.o, ejecutables)
```

### Ejemplo: Formatear y compilar

```bash
# 1. Formatear todos los archivos C++ según .clang-format
make format-cpp

# 2. Compilar un archivo
make compile FILE=src/hello.cpp

# 3. El ejecutable se encuentra en /workspace
docker-compose exec cpp-course ./hello
```

## Configuración de formato (clang-format)

El archivo `.clang-format` define el estilo de código:
- Indentación: 4 espacios
- Ancho de línea: 100 caracteres
- Estilo: LLVM + Allman braces
- Espacios después de palabras clave (if, for, while)

Edita `.clang-format` si necesitas ajustar el formato.

## Para estudiantes

Todos comparten el mismo ambiente Docker, garantizando que:
- Los compiladores son idénticos
- Las versiones de librerías son consistentes
- El formato de código es uniforme (clang-format)
- Los bugs de "me funciona en mi máquina" se minimizan
