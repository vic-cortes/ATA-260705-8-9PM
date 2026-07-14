# Docker setup para Curso de C++

Ambiente containerizado para desarrollar y compilar programas en C++ durante el curso.

## Requisitos

- Docker y Docker Compose instalados
- Mac M1/M2/M3 (o cambiar `linux/arm64` a `linux/amd64` en el Dockerfile)

## Quick Start

### 1. Construir la imagen (primera vez)

```bash
docker-compose build
```

### 2. Iniciar el contenedor

```bash
docker-compose up -d
```

O interactivo (recomendado para desarrollo):

```bash
docker-compose run --rm cpp-course /bin/bash
```

### 3. Compilar un programa C++

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

## Para estudiantes

Todos comparten el mismo ambiente Docker, garantizando que:
- Los compiladores son idénticos
- Las versiones de librerías son consistentes
- Los bugs de "me funciona en mi máquina" se minimizan
