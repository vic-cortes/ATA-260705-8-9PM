# Usa la versión ligera oficial con la arquitectura nativa de tu Mac M1
FROM --platform=linux/arm64 debian:bookworm-slim

# Instala herramientas de desarrollo para C++ (compilación, debugging, análisis)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    g++ \
    gcc \
    make \
    gdb \
    valgrind \
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
