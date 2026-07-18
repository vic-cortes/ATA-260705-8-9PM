---
fecha: 2026-07-15
bloque: 0→1
duracion: ~90 minutos
participantes:
  - Profesor
  - Arturo
  - Genny
  - Ismael
  - Otros alumnos
recursos:
  - transcript.txt (disponible en la misma carpeta)
---

# Resumen de la sesión de clase

**Contexto general:** Continuación de **comandos Linux**. Se profundiza en herramientas más especializadas (`grep`, `find`, `less`, `head`, `tail`) y se recapitulan los conceptos de permisos, filtrado y búsqueda de contenido. Se enfatiza el uso práctico de la terminal para desarrollo embebido.

## Puntos principales

**1. Recapitulación de comandos básicos**

Se revisaron brevemente los comandos fundamentales de la sesión anterior:
- **ls**: listar contenido (variantes con banderas `-l`, `-a`, `-h`)
- **pwd**: mostrar ubicación actual
- **cd**: cambiar de directorio
- **touch**: crear archivo vacío
- **cat**: ver contenido de archivo

Énfasis en **permisos** mostrados en `ls -l`:
- Primera columna: `d` = directorio, `r` = lectura, `w` = escritura, `x` = ejecución
- Ejemplo: `drwxr-xr-x` significa: directorio con permisos rwx para propietario, r-x para grupo, r-x para otros
- **Nota importante**: Se verán cambios de permisos más adelante (comandos como `chmod`)

**2. Comandos para ver contenido de archivos grandes**

**less** (visor con paginación):
- Comando: `less archivo.txt`
- Crea una interfaz especial donde puedes:
  - Navegar con flechas arriba/abajo
  - Buscar con `/` (diagonal) + palabra: `/ palabra_buscada`
  - Salir con `q`
- Ventaja: no sobrecarga la terminal con texto masivo
- Caso de uso: leer logs grandes, códigos enormes, o archivos de configuración

**head** (primeras líneas):
- `head archivo.txt`: muestra las primeras líneas (típicamente 10)
- `head -n N archivo.txt`: muestra las primeras N líneas
- Caso de uso: revisar rápidamente el inicio de un archivo sin verlo completo

**tail** (últimas líneas):
- `tail archivo.txt`: muestra las últimas líneas
- `tail -n N archivo.txt`: muestra las últimas N líneas
- Caso de uso especial: **monitorear logs en tiempo real** (usado en automatización con Jenkins)
- Ejemplo práctico: en un sistema de CI/CD, `tail` se usa para ver solo el final de un log mientras se sigue escribiendo

**3. Profundidad en `grep` (búsqueda de texto)**

**grep** (global regular expression print):
- Función: buscar un patrón de texto dentro de archivos
- Sintaxis: `grep "patrón" archivo.txt`
- Buscar en múltiples archivos: `grep "patrón" *.extension`

Ejemplos prácticos:
- `grep "hola" notas.txt`: encuentra todas las líneas con "hola"
- `grep "hola" *.cpp`: busca "hola" en todos los archivos .cpp
- Opción `-i` (case-insensitive): `grep -i "HOLA" archivo.txt` encuentra "hola", "Hola", "HOLA", etc.

Diferencia con `find`:
- **find**: busca nombres de archivos (ej. `find . -name "*.txt"`)
- **grep**: busca contenido dentro de archivos (ej. `grep "función" archivo.cpp`)

**4. Cómo editar archivos con nano**

**nano** (editor de texto simple):
- Iniciar: `nano archivo.txt`
- Si el archivo no existe, lo crea
- Modo inserción: simplemente escribe
- Atajos principales:
  - `Ctrl+O`: guardar (pide confirmar nombre)
  - `Ctrl+X`: salir
  - `Ctrl+K`: cortar línea (experimental, requiere selección)
  - `Ctrl+U`: pegar línea (experimental)
  - `Ctrl+G`: ayuda dentro del editor

Nota sobre formas de editar:
- **vim/emacs**: más poderosos pero complicados (se menciona que dejaban malos recuerdos al profesor por no recordar cómo salir)
- **nano**: más amigable para principiantes
- En producción (DevOps), a veces es necesario usar vim/emacs si nano no está disponible

**5. Ejemplo práctico: crear un archivo C++ con nano**

Se demostró crear un pequeño programa:
```cpp
#include <iostream>
using namespace std;
int main() {
  cout << "Hola mundo";
  return 0;
}
```

Notas sobre C++:
- Estructura básica: `#include <iostream>` para entrada/salida
- `using namespace std;` permite usar `cout` sin `std::`
- Función `main()` es el punto de entrada
- `cout`: equivalente a print de pseudocódigo (escribe en pantalla)
- `return 0;` indica fin exitoso de la función (obligatorio para funciones `int`)
- Conceptos más avanzados (void, diferentes tipos de retorno) se verán después

**6. Herramientas de búsqueda avanzada**

**find** (buscar archivos):
- `find . -name "archivo.txt"`: busca en carpeta actual y subdirectorios
- `find . -name "*.cpp"`: busca todos los archivos .cpp
- `find . -type d -name "carpeta"`: busca carpetas específicamente (`-type d`)
- Útil cuando tienes estructura de directorios compleja

**7. Escritura de contenido con echo**

Se revisó nuevamente el uso de redirección:
- `echo "texto" > archivo.txt`: sobrescribe (una flecha)
- `echo "texto" >> archivo.txt`: añade al final (dos flechas)
- Casos de uso:
  - Crear archivos de configuración rápidamente
  - Llenar logs línea por línea
  - Automatización con Jenkins (escribir estados de compilación)

## Siguiente paso

**Próxima sesión:** Introducción a **máquinas de estados** (concept fundamental para sistemas embebidos y automotrices). Se comenzará con diagramas teóricos y luego implementación en **PSeInt** antes de pasar a C++.

**Tarea sugerida:** Continuar practicando navegación y búsqueda en terminal. Familiarizarse con `grep` y `find` para búsquedas eficientes.
