---
fecha: 2026-07-13
bloque: 0→1
duracion: ~120 minutos
participantes:
  - Profesor
  - Ofelia
  - Tomas
  - Otros alumnos
recursos:
  - raw_transcript.txt (disponible en la misma carpeta)
---

# Resumen de la sesión de clase

**Contexto general:** El profesor revisa la tarea del bloque 0 (MenuCalificaciones con validación de rangos), introduce **funciones en PSeInt** (subprocesos y funciones que retornan valores), y comienza el **setup del ambiente de desarrollo para Bloque 1** instalando Linux (Debian) vía WSL en Windows con las herramientas necesarias para compilar C++.

## Puntos principales

**1. Revisión de tarea: MenuCalificaciones (Ofelia)**
Se revisó en vivo el código de Ofelia para validación de calificaciones. El profesor identificó dos errores comunes:
- **Error 123** (identificador en uso): causado por redimensionar arrays dinámicamente dentro de bucles. Solución: declarar el array con un tamaño fijo (ej. 100) **antes** de los ciclos, no dentro.
- **Lógica invertida en validación**: el while que controlaba el rango estaba al revés. En vez de `mientras calificación sea mayor a 0 y menor a 10`, debería ser `mientras calificación sea menor a 0 o mayor a 10` (para pedir reintentos si está fuera de rango).

Se enfatizó que aunque el código quedó "espaguetti", **lo importante es que funcione primero**; la compacidad y elegancia vienen después, cuando se desarrolla la práctica.

**2. Funciones en PSeInt (subprocesos y funciones con retorno)**
Se enseñó que PSeInt permite **subprocesos** (similar a funciones) que pueden recibir parámetros e incluso retornar valores:
- **SubProceso**: para procedimientos que no retornan nada (ej. `SubProceso saludo(nombre)` que solo imprime).
- **Función**: para operaciones que retornan un valor. Ejemplo práctico: función `calcular(base, altura)` que calcula el área de un triángulo y retorna el resultado.
- Se aclaró que el **nombre de la variable** que guarda el resultado debe coincidir con el nombre de la función para que el retorno funcione correctamente.

Nota: El profesor reconoció que PSeInt es relativamente nuevo para él, pero confirmó que esta característica existe y es útil para modularizar código.

**3. Evaluación final del Bloque 0**
El profesor recordó que la evaluación del Bloque 0 será un **proyecto de pseudocódigo más elaborado**, trabajando posiblemente en equipos de 2-3 personas. Mencionó que para los alumnos de **Vehiculos** (8-9 y 9-10), el proyecto será especial: definir un **mini ACU** (Sistema de Control Automotriz) con pseudocódigo, comenzando con:
- Señales de entrada/salida
- Requerimientos del sistema
- Estructura general (sin necesidad de todo el ACU completo)

Este proyecto se irá complementando en bloques posteriores.

**4. Setup de Linux vía WSL en Windows 10/11**
Se inició la instalación de un ambiente Linux containerizado usando **WSL** (Windows Subsystem for Linux) en lugar de máquinas virtuales o dual-boot:
- **Ventajas**: no gasta casi espacio, no requiere reboot ni partición, se instala/desinstala fácilmente.
- **Distribución elegida**: **Debian** (se estandarizó para toda la clase, aunque Ubuntu/Fedora también son opciones).
- **Alternativa para Mac**: Docker fue sugerido como solución más segura que dual-boot en macOS (para no afectar garantía ni estabilidad del sistema).

Comandos básicos presentados:
- `wsl --list --verbose`: listar distribuciones instaladas
- `wsl --install -d Debian`: instalar Debian
- `wsl --shutdown`: apagar todos los servicios WSL
- `wsl --unregister <nombre>`: desinstalar una distribución
- `wsl -d Debian`: iniciar la distribución

**5. Instalación de herramientas en Debian**
Una vez dentro de Debian, se ejecutaron actualizaciones e instalación de paquetes:
```bash
sudo apt update        # Actualizar índice de paquetes
sudo apt upgrade -y    # Actualizar paquetes (-y evita confirmación)
sudo apt install build-essential gdb git make nano
```

Herramientas instaladas:
- **build-essential**: compilador GCC y herramientas para compilar C/C++
- **gdb**: debugger de GNU para depuración
- **git**: control de versiones
- **make**: automatización de compilaciones
- **nano**: editor de texto simple para terminal (se mencionó vim/emacs como alternativas más avanzadas)

**6. Verificación del ambiente**
Se validó que todo estuviera correctamente instalado:
```bash
gcc --version   # verificar compilador C
g++ --version   # verificar compilador C++
git --version   # verificar control de versiones
```

Todas las herramientas reportaron versiones correctas, indicando que el ambiente está listo para programar en C++.

**7. Visual Studio Code + WSL**
Se mencionó que VS Code tiene integración nativa con WSL, permitiendo editar código en VS Code (en Windows) mientras se compila/ejecuta dentro del entorno Linux, sin necesidad de trabajar exclusivamente en terminal. Esto será configurado posteriormente.

## Siguiente paso

**Próxima sesión:** Configurar Visual Studio Code integrado con WSL y enseñar comandos básicos de Linux (cd, ls, pwd, mkdir, etc.) antes de comenzar con C++ en Bloque 1. Los alumnos deben tener Debian instalado y funcional en sus máquinas para la próxima clase.
