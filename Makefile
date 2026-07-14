.PHONY: help docker-build docker-up docker-down docker-shell format-cpp clean

# Variables
DOCKER_IMAGE = cpp-curso
DOCKER_COMPOSE = docker compose
CPP_FILES = $(shell find . -type f \( -name "*.cpp" -o -name "*.h" -o -name "*.hpp" \) -not -path "*/\.*")
CLANG_FORMAT = clang-format -i

help:
	@echo "Makefile para Curso de C++"
	@echo ""
	@echo "Targets disponibles:"
	@echo "  make docker-build    - Construir imagen Docker"
	@echo "  make docker-up       - Iniciar contenedor (background)"
	@echo "  make docker-shell    - Entrar a shell interactivo"
	@echo "  make docker-down     - Detener contenedor"
	@echo "  make format-cpp      - Formatear archivos C++ con clang-format"
	@echo "  make clean           - Limpiar archivos compilados"
	@echo ""

# Docker targets
docker-build:
	@echo "🔨 Construyendo imagen Docker..."
	$(DOCKER_COMPOSE) build

docker-up:
	@echo "🚀 Iniciando contenedor..."
	$(DOCKER_COMPOSE) up -d
	@echo "✅ Contenedor corriendo"

docker-down:
	@echo "🛑 Deteniendo contenedor..."
	$(DOCKER_COMPOSE) down
	@echo "✅ Contenedor detenido"

docker-shell:
	@echo "📂 Abriendo shell interactivo..."
	$(DOCKER_COMPOSE) run --rm cpp-course bash

# Formatting target
format-cpp:
	@if [ -z "$(CPP_FILES)" ]; then \
		echo "❌ No se encontraron archivos C++"; \
		exit 1; \
	fi
	@echo "🎨 Formateando archivos C++..."
	$(DOCKER_COMPOSE) run --rm cpp-course sh -c " \
		cd /workspace && \
		$(CLANG_FORMAT) $(CPP_FILES) && \
		echo '✅ Formateo completado' \
	"

# Compile target (ejemplo para compilar un archivo)
compile:
	@if [ -z "$(FILE)" ]; then \
		echo "❌ Uso: make compile FILE=src/programa.cpp"; \
		exit 1; \
	fi
	@echo "⚙️  Compilando $(FILE)..."
	$(DOCKER_COMPOSE) run --rm cpp-course sh -c " \
		cd /workspace && \
		g++ -Wall -Wextra -std=c++17 -o $$(basename $(FILE) .cpp) $(FILE) && \
		echo '✅ Compilado: $$(basename $(FILE) .cpp)' \
	"

# Clean target
clean:
	@echo "🧹 Limpiando archivos compilados..."
	find . -type f \( -name "*.o" -o -name "*.out" \) -delete
	find . -type f -executable ! -path "*/\.*" ! -path "*/.git/*" -delete 2>/dev/null || true
	@echo "✅ Limpieza completada"

# All-in-one setup
setup: docker-build docker-up
	@echo "✅ Setup completado. Usa 'make docker-shell' para entrar al contenedor"

# Status check
status:
	@echo "📊 Estado del contenedor:"
	$(DOCKER_COMPOSE) ps
