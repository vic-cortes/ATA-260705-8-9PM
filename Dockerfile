# Imagen ligera oficial multi-arquitectura.
# Sin --platform: Docker usa la arquitectura nativa del host
# (arm64 en Mac M1, amd64 en Linux). Así funciona nativo en ambos.
FROM debian:bookworm-slim

# Instala herramientas de desarrollo para C++ (compilación, debugging, análisis, formatting)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    g++ \
    gcc \
    make \
    gdb \
    valgrind \
    clang-format \
    git \
    vim \
    nano \
    wget \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Define el directorio de trabajo dentro del contenedor
WORKDIR /workspace

# Comando por defecto al arrancar el contenedor
CMD ["/bin/bash"]
