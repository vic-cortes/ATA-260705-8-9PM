---
semana: 2
fechas: 2026-07-13 a 2026-07-16
bloque: 0→1
duracion_total: ~460 minutos (7.7 horas)
sesiones: 4
participantes_base:
  - Profesor Óscar Godíz
  - Víctor Cortés
  - Ismael
  - Arturo
  - Carlos Caravantes
  - Alejandro Coronado
  - Juan Anuel
  - Fernando Gutiérrez
  - Edweni
  - Ofelia
  - Genaro (Genny)
---

# Resumen Semanal: Semana 2 del Curso

## Contexto General

La Semana 2 marca la **transición de Bloque 0 (pseudocódigo) a Bloque 1 (C++)** y la introducción de conceptos fundamentales para sistemas embebidos automotrices. Se divide en cuatro sesiones progresivas:

1. **Domingo (13/07)**: Revisión de tarea, funciones en PSeInt, setup de Linux vía WSL
2. **Lunes (14/07)**: Comandos básicos de Linux (navegación y manipulación de archivos)
3. **Martes (15/07)**: Comandos avanzados de Linux (búsqueda, visualización de archivos grandes)
4. **Miércoles (16/07)**: **Máquinas de estados** (state machines) - concepto crítico para especialidad automotriz

La semana cierra con introducción a máquinas de estado y tarea de diseño de diagrama de transiciones.

---

## Temas Principales por Sesión

### Sesión 1 (13/07): Cierre de Bloque 0 y Setup de Desarrollo

**Revisión de Tarea: MenuCalificaciones**

Se analizó en vivo el código de Ofelia (validación de rango 0-100):

Errores comunes identificados:
- **Error 123** (identificador duplicado): causado por declarar arrays dentro de ciclos en lugar de antes. Solución: declarar `Dimensión` **fuera** del ciclo con tamaño fijo
- **Lógica invertida**: condicional while mal escrita. Debe ser: "mientras esté **fuera** del rango válido, pedir reintentos"
- **"Código espaguetti" es aceptable al inicio**: lo importante es que funcione; la elegancia viene con la práctica

Lecciones:
- Validar que cada línea hace lo esperado
- Separar declaración de inicialización
- Probar con casos límite (0, 100, -1, 101)

**Funciones en PSeInt**

Se introdujo modularización con **SubProceso y Función**:

**SubProceso** (sin retorno):
```pseudocodigo
SubProceso saludar(nombre)
    Escribir "Hola, " nombre
FinSubProceso
```

**Función** (con retorno):
```pseudocodigo
Función area <- calcularArea(base, altura)
    area <- (base * altura) / 2
FinFunción
```

Nota: El **nombre de la variable que retorna debe coincidir con el nombre de la función**.

Beneficio: Reutilizar código, separación de responsabilidades.

**Setup de Linux (Windows Subsystem for Linux - WSL)**

Decisión: Estandarizar **Debian** (no Ubuntu) para evitar problemas de compatibilidad futuros.

Razones:
- Ubuntu está basado en Debian pero es más pesado
- Debian casi no consume espacio en WSL
- Para Mac: usar **Docker** (más seguro que dual-boot)
- Los comandos básicos de terminal son casi idénticos en ambas

Instalación en Windows 10/11:
```bash
wsl --install -d Debian        # Instalar Debian
wsl -d Debian                  # Iniciar Debian
```

Instalación de herramientas esenciales:
```bash
sudo apt update                # Actualizar índice
sudo apt upgrade -y            # Actualizar paquetes
sudo apt install build-essential gdb git make nano
```

Herramientas instaladas:
- **build-essential**: compilador GCC/G++ para C/C++
- **gdb**: debugger GNU
- **git**: control de versiones
- **make**: automatización de compilaciones
- **nano**: editor de texto terminal

Validación:
```bash
gcc --version   # Verificar C
g++ --version   # Verificar C++
git --version   # Verificar Git
```

Próximo: Visual Studio Code integrado con WSL.

---

### Sesión 2 (14/07): Comandos Linux Básicos

**Enfoque**: Dominar la terminal para navegar, crear y manipular archivos.

**Comandos Fundamentales:**

| Comando | Función | Ejemplo |
|---------|---------|---------|
| `ls` | Listar contenido | `ls -lah` (detallado, con ocultos, tamaño legible) |
| `pwd` | Mostrar ubicación actual | `pwd` → `/home/oscar` |
| `cd` | Cambiar directorio | `cd carpeta`, `cd ..` (retroceder), `cd ~` (home) |
| `mkdir` | Crear carpeta | `mkdir ATA_8-9` |
| `touch` | Crear archivo vacío | `touch notas.txt` |
| `cat` | Ver contenido de archivo | `cat archivo.txt` |
| `cp` | Copiar archivo | `cp original.txt copia.txt` |
| `mv` | Mover/renombrar | `mv archivo.txt nuevo_nombre.txt` |
| `rm` | Borrar archivo | `rm archivo.txt` (SIN recuperación) |

**Características importantes:**

- **Autocompletado con Tab**: escribir inicio + Tab completa el nombre
- **Iteración de opciones**: Tab múltiple itera entre similares (ej. "programa" y "programas")
- **Permisos** (en `ls -l`): `rwxrwxrwx` = lectura, escritura, ejecución para propietario/grupo/otros
- **Filtrado**: `ls *.txt` lista solo archivos .txt

**Flujo práctico:**
```bash
cd /home/oscar
mkdir ATA_8-9
cd ATA_8-9
touch notas.txt
echo "Contenido" >> notas.txt      # Añadir (dos flechas)
cat notas.txt                       # Ver contenido
nano notas.txt                      # Editar
```

---

### Sesión 3 (15/07): Comandos Linux Avanzados

**Enfoque**: Herramientas especializadas para búsqueda y visualización.

**Comandos para ver contenido de archivos grandes:**

**less** (visor con navegación):
- Comando: `less archivo.txt`
- Navega con flechas, busca con `/`, sale con `q`
- Ideal: logs enormes, código grande, sin sobrecargar terminal

**head** (primeras líneas):
```bash
head archivo.txt           # Primeras 10 líneas
head -n 5 archivo.txt      # Primeras 5 líneas
```

**tail** (últimas líneas):
```bash
tail archivo.txt           # Últimas 10 líneas
tail -n 1 archivo.txt      # Última línea
```

Caso de uso especial: Monitorear logs en tiempo real durante compilaciones/despliegues (usado en Jenkins CI/CD).

**Búsqueda de contenido:**

**grep** (buscar texto dentro de archivos):
```bash
grep "palabra" archivo.txt              # Buscar en un archivo
grep "palabra" *.cpp                    # Buscar en todos los .cpp
grep -i "Palabra" archivo.txt           # Sin diferenciar mayúsculas
```

Diferencia con `find`:
- **find**: busca **nombres de archivos** → `find . -name "*.txt"`
- **grep**: busca **contenido dentro de archivos** → `grep "función" archivo.cpp`

**find** (buscar archivos):
```bash
find . -name "archivo.txt"              # Buscar por nombre
find . -name "*.cpp"                    # Buscar por extensión
find . -type d -name "carpeta"          # Buscar solo carpetas (-type d)
```

**Edición con nano:**

Atajos en nano:
- `Ctrl+O`: guardar (pide confirmar nombre)
- `Ctrl+X`: salir
- `Ctrl+K`: cortar línea
- `Ctrl+U`: pegar línea
- `Ctrl+G`: ayuda

Nota: vim/emacs más poderosos pero complicados (el profesor ha "quedado atrapado" sin poder salir de vim).

**Escritura de contenido:**

```bash
echo "hola" > archivo.txt               # Sobrescribir (una flecha)
echo "hola" >> archivo.txt              # Añadir al final (dos flechas)
```

Usado en automatización para llenar logs y archivos de configuración.

---

### Sesión 4 (16/07): Máquinas de Estados (State Machines)

**Importancia**: Concepto fundamental para especialidad automotriz. Muchos componentes del vehículo usan máquinas de estado.

**Definición:**

Una máquina de estado es un sistema que:
- Reporta constantemente su estado/estatus
- Cambia de estado solo en respuesta a eventos
- **Fórmula**: `Estado(t+1) = f(Estado(t), Evento)`

**Regla de oro:**
> "No basta preguntar qué ocurrió, sino **en qué estado estaba el sistema**"

Ejemplo: cajuela de auto
- Si está cerrada y presionas "abrir" → se abre
- Si está abierta y presionas "abrir" → no pasa nada (mismo evento, diferente estado = diferente resultado)

**Ejemplos en la vida real:**

1. **Semáforo** (cíclico):
   - Verde → Amarillo → Rojo → Verde
   - Evento: tiempo transcurrido
   - Lazo cerrado (siempre regresa al inicio)

2. **Puerta automática** (compleja):
   - Estados: Cerrada → Abriendo → Abierta → Cerrando → Cerrada
   - Eventos: detecta persona, fin de apertura, fin de cierre
   - Bifurcaciones: persona en medio → regresa a Abierta

3. **Relevador** (binario):
   - Estados: Abierto (0) ↔ Cerrado (1)
   - Evento: señal de control
   - Máquina más simple

4. **Elevador** (múltiples estados):
   - Espera → Puerta abriendo → Abierta → Puerta cerrando → Cerrada
   - Eventos: solicitud de piso, timer

**Componentes del diagrama:**

- **Círculos**: estados
- **Flechas**: transiciones (con evento etiquetado)
- **Lazo**: ciclo (cerrado = regresa al origen, abierto = terminal)

Ejemplo de puerta con bifurcación:
```
Cerrada
  ↓ (Detecta persona)
Abriendo
  ↓ (Fin de apertura)
Abierta
  ├→ (Tiempo 5s) → Cerrando
  └→ (Obstáculo) → Abierta (NUEVO)
Cerrando
  ├→ (Fin cierre) → Cerrada
  └→ (Obstáculo) → Abierta (NUEVO)
```

**Tabla de transiciones** (alternativa a diagrama):
| Estado | Evento | Nuevo Estado |
|--------|--------|--------------|
| Cerrada | Detecta | Abriendo |
| Abriendo | Fin | Abierta |
| Abierta | Tiempo | Cerrando |
| Cerrando | Fin | Cerrada |
| Cerrando | Obstáculo | Abierta |

**Estados especiales: ERROR**

Muchas máquinas agregan estado de error:
```
Normal → [Falla] → ERROR
ERROR → [Espera 5s] → Reintentar
Reintentar → [Éxito] → Normal
Reintentar → [Sigue fallando] → ERROR
```

**Implementación en PSeInt usando Según (switch)**

Estructura básica - Lámpara con botón:

```pseudocodigo
Algoritmo Lámpara
  Definir estado Como Entero      // 0=apagada, 1=encendida
  Definir botón Como Entero       // 1=presionar, 2=salir
  Definir salir Como Lógico       // Control del ciclo
  
  estado ← 0
  salir ← Falso
  
  Mientras salir = Falso Hacer
    // Reportar estado actual
    Escribir "Estado actual:"
    Según estado Hacer
      Caso 0:
        Escribir "Lámpara APAGADA"
      Caso 1:
        Escribir "Lámpara ENCENDIDA"
    FinSegún
    
    // Leer evento
    Escribir "1=Botón, 2=Salir"
    Leer botón
    
    // Procesar evento
    Según botón Hacer
      Caso 1:
        Si estado = 0 Entonces
          estado ← 1    // Transición: Apagada → Encendida
        Sino
          estado ← 0    // Transición: Encendida → Apagada
        FinSi
      Caso 2:
        salir ← Verdadero
      Por Defecto:
        Escribir "Opción inválida"
    FinSegún
  FinMientras
  
  Escribir "Programa terminado"
FinAlgoritmo
```

**Conceptos clave:**

- **`switch`/`Según`** es ideal (no es condicional, es un "redirector de flujo")
- Ciclos infinitos en máquinas de estado (permanente monitoreo de sensores)
- Transiciones = asignaciones simples a la variable de estado
- Verificar estado **antes** de actuar

**¿Por qué switch es mejor que if?**

- `if`: revisa condiciones ("¿se cumple esto?")
- `switch`: redirige según valor ("¿a qué estado voy?")
- Máquinas de estado son máquinas de "redireccionamiento"

**Ciclos embebidos:**

En Arduino/ESP32:
```cpp
void loop() {
  switch(estado) {
    case 0: // hacer algo
    case 1: // hacer otra cosa
  }
}
```

El `loop()` se ejecuta infinitamente monitoreando sensores.

**Feedback del profesor:**

Se realizó encuesta informal sobre velocidad de clase:
- Algunos sienten que es lenta
- Profesor reconoce que máquinas de estado es tema denso
- Objetivo: entender **dónde aplicar**, no solo memorizar
- Se promete mayor orientación a sistemas automotrices

---

## Progresión Temática de la Semana

```
Sesión 1: CIERRE DE BLOQUE 0 + SETUP DESARROLLO
  └─ Revisión de tarea (arrays, validación)
  └─ Funciones en PSeInt (modularización)
  └─ Setup Linux vía WSL (Debian + herramientas)

Sesión 2: TERMINAL LINUX - NAVEGACIÓN
  └─ Comandos básicos (ls, pwd, cd, mkdir, touch)
  └─ Manipulación de archivos (cp, mv, rm)
  └─ Edición con nano

Sesión 3: TERMINAL LINUX - BÚSQUEDA Y VISUALIZACIÓN
  └─ Visor de archivos (less, head, tail)
  └─ Búsqueda de contenido (grep, find)
  └─ Automatización (echo con redirección)

Sesión 4: MÁQUINAS DE ESTADO
  └─ Teoría (definición, componentes, ejemplos)
  └─ Diagramas de transición
  └─ Implementación en PSeInt con Según/switch
  └─ Casos de uso automotrices
```

---

## Hitos y Evaluaciones

| Fecha | Evento | Estado |
|-------|--------|--------|
| 13/07 | Revisión MenuCalificaciones | Completada |
| 16/07 | Tarea: Diseño de máquina de estados | Propuesta |
| ~17-18/07 | Evaluación Bloque 0 (en equipos) | Próxima |
| 18/07+ | Bloque 1: C++ básico | Pendiente |

---

## Conceptos Clave Establecidos

1. **Linux Terminal**: Herramienta esencial para desarrollo embebido
2. **Comandos de navegación**: Navegar sin interfaz gráfica
3. **Grep vs Find**: Búsqueda de contenido vs. nombres
4. **Máquinas de estado**: Paradigma fundamental en sistemas automotrices
5. **Estado + Evento**: Duo inseparable para definir transiciones
6. **Switch/Según**: Estructura ideal para máquinas de estado
7. **Diagramas de transición**: Herramienta de diseño antes de código
8. **Lazo cerrado/abierto**: Características de máquinas cíclicas
9. **Casos de error**: Estados especiales para manejo de fallos
10. **Ciclos infinitos**: Monitoreo permanente en sistemas embebidos

---

## Próximos Pasos

1. **Alumnos:**
   - Practicar comandos Linux en propia máquina
   - Diseñar diagrama de máquina de estados (fin de semana)
   - Implementar máquina de estados en PSeInt
   - Preparar evaluación Bloque 0 (con máquina de estado incluida)

2. **Profesor:**
   - Revisar tarea de diseño de máquinas de estado
   - Evaluar Bloque 0 con criterio de máquinas de estado
   - Preparar introducción a **requerimientos técnicos** (cómo traducir cliente → máquina formal)
   - Iniciar Bloque 1: C++ con conceptos de máquina de estado aplicados

3. **Especialización (Automotriz):**
   - Mini-ACU con máquinas de estado
   - Sensores y sistemas de control (ECU)
   - Comunicación CAN entre componentes

---

## Notas Transversales

- **Herramientas oficiales del curso**: PSeInt, VS Code + WSL, Make, g++, gdb
- **Estándar de distribución**: Debian para todos (excepto Mac con Docker)
- **Filosofía de terminal**: Más poder, menos interfaz gráfica (necesario en producción/embebido)
- **Máquinas de estado**: No es optional; es obligatorio para especialidad automotriz
- **Transición Bloque 0→1**: Pseudocódigo → C++ (mismos conceptos, sintaxis diferente)
- **Mentalidad de arquitecto**: Diseñar (diagrama) antes de codificar
- **Contactos industriales**: Continental, Sidec, Airbus (experiencia real en el aula)

---

## Cambios Respecto a Week 1

- **Introducción de Linux**: Cambio importante del pseudocódigo puro a terminal
- **Máquinas de estado**: Tema nuevo, foundation para especialización automotriz
- **Menos teoría, más práctica**: Comandos Linux se practican inmediatamente
- **Énfasis en diseño**: Diagramas antes de código (especialmente máquinas de estado)
