---
fecha: 2026-07-14
bloque: 0→1
duracion: ~120 minutos
participantes:
  - Profesor
  - Ismael
  - Genaro (Genny)
  - Arturo
  - Otros alumnos
recursos:
  - transcript.txt (disponible en la misma carpeta)
---

# Resumen de la sesión de clase

**Contexto general:** El profesor enseña **comandos básicos de Linux** necesarios para navegar el sistema de archivos, crear/modificar archivos, y buscar contenido. Se enfatiza la importancia de dominar la terminal para trabajar con código en entornos embebidos y desarrollo en general.

## Puntos principales

**1. Recapitulación de distribuciones Linux (WSL)**
Se confirmó que:
- **Ubuntu y Debian** son muy parecidas; Ubuntu está basada en Debian.
- Se estandarizó **Debian** para la clase para evitar problemas de compatibilidad futuros en temas avanzados.
- Para **Mac**, la solución es Docker (más seguro que dual-boot o máquina virtual).
- Los comandos básicos de terminal no cambian significativamente entre distribuciones Linux.

**2. Comandos fundamentales de Linux**

**ls** (list):
- Mostrar contenido de la carpeta actual
- Variantes: `ls -l` (formato detallado con permisos), `ls -a` (mostrar archivos ocultos), `ls -lh` (tamaño en formato legible), `ls *.txt` (filtrar por extensión)
- Ejemplo: `ls -la` muestra todos los archivos incluyendo los ocultos con detalles

**pwd** (print working directory):
- Mostrar la ruta actual del usuario en el sistema
- Ejemplo: `pwd` devuelve `/home/oscar`

**cd** (change directory):
- Cambiar de carpeta: `cd carpeta_nombre`
- Retroceder una carpeta: `cd ..`
- Volver al inicio (home): `cd` o `cd ~`
- Autocompletado: escribir el inicio de un nombre y presionar **Tab** para completar automáticamente
- Si hay ambigüedad (ej. "programa" y "programas"), presionar **Tab** nuevamente itera entre opciones

**mkdir** (make directory):
- Crear una carpeta: `mkdir nueva_carpeta`
- Ejemplo: `mkdir ATA_8-9` crea la carpeta "ATA_8-9" en la ubicación actual

**touch**:
- Crear un archivo vacío: `touch archivo.txt`
- No edita, solo crea el contenido inicial

**cat** (concatenate):
- Ver contenido de un archivo: `cat archivo.txt`
- Muestra todo el contenido de un vistazo (para archivos pequeños)

**nano**:
- Editor de texto en terminal para editar archivos
- Atajos:
  - `Ctrl+O`: guardar (pide confirmar nombre del archivo)
  - `Ctrl+X`: salir
  - `Ctrl+K`: cortar línea (requiere selección adicional)
  - `Ctrl+U`: pegar línea
  - `Ctrl+G`: mostrar ayuda

**echo**:
- Escribir texto a un archivo o imprimir en pantalla
- `echo "hola mundo"`: imprime "hola mundo" en la terminal
- `echo "contenido" > archivo.txt`: sobrescribe el archivo (una flecha)
- `echo "contenido" >> archivo.txt`: añade al final del archivo (dos flechas)
- Ejemplo práctico: añadir líneas a un archivo de configuración o log

**head** y **tail**:
- `head archivo.txt`: muestra las primeras líneas
- `tail archivo.txt`: muestra las últimas líneas
- `head -n 2 archivo.txt`: muestra las primeras 2 líneas
- `tail -n 1 archivo.txt`: muestra la última línea
- Útil para archivos grandes donde `cat` sería incómodo

**less**:
- Visor de archivos grande con navegación por páginas
- Atajos:
  - Flechas arriba/abajo: navegar
  - `/` (diagonal): buscar texto
  - `q`: salir
- Ejemplo: `less archivo.txt` permite leer un archivo grande sin imprimirlo completo

**cp** (copy):
- Copiar archivo: `cp archivo.txt copia.txt`
- Crea una copia exacta con nuevo nombre

**mv** (move):
- Mover archivo a otra carpeta: `mv archivo.txt carpeta/`
- Renombrar archivo: `mv archivo_viejo.txt archivo_nuevo.txt`
- La utilidad es dual: mover o renombrar (refactorizar)

**rm** (remove):
- Borrar archivo: `rm archivo.txt`
- **Advertencia**: no hay papelera de reciclaje en terminal, es irreversible

**find**:
- Buscar archivos por nombre: `find . -name "archivo.txt"`
- Buscar archivos con extensión: `find . -name "*.cpp"`
- Buscar carpetas: `find . -type d -name "carpeta_nombre"`
- Muy útil cuando tienes muchos archivos y no recuerdas la ubicación
- Ejemplo: `find . -name "*.txt"` lista todos los archivos de texto en el directorio actual y subdirectorios

**grep**:
- Buscar texto dentro de archivos: `grep "palabra" archivo.txt`
- Buscar en múltiples archivos: `grep "palabra" *.cpp`
- Opción case-insensitive: `grep -i "Palabra" archivo.txt`
- Mejor que find cuando buscas contenido, no nombres de archivos

**3. Uso práctico: crear y modificar archivos en la terminal**
Se demostró cómo:
- Crear una carpeta: `mkdir ATA_8-9`
- Entrar a la carpeta: `cd ATA_8-9`
- Crear archivo: `touch notas.txt`
- Añadir contenido con echo: `echo "Buenas noches" >> notas.txt`
- Ver contenido: `cat notas.txt`
- Editar con nano: `nano notas.txt`
- Crear archivo de código C++: `nano hola.cpp` (crea y edita simultáneamente)

Ejemplo de código básico en C++ creado con nano:
```cpp
#include <iostream>
using namespace std;
int main() {
  cout << "Hola mundo";
  return 0;
}
```

**4. Búsqueda de ayuda en la terminal**
- Se intentó `man ls` (manual page) pero **no estaba disponible en WSL/Debian**
- Alternativa: revisar documentación oficial de Debian/Linux en línea
- Se mencionó que hay comandos con variantes de `help` que sí funcionan

**5. Diferencia entre editar con nano y cat**
- **cat**: solo lectura, rápido para ver contenido
- **nano**: permite modificar, más cómodo, pero menos práctico para archivos enormes
- Para archivos muy grandes mejor usar `less` para lectura o `nano` solo si necesitas cambios

## Siguiente paso

**Próxima sesión:** Continuar con más comandos de Linux (especialmente `grep` en profundidad, `tar` para comprimir, `chmod` para permisos). Después de dominar la terminal, se introducirá **programación en C** con ejemplos prácticos compilados dentro de Debian vía WSL.

**Tarea sugerida:** Practicar los comandos básicos en la propia máquina (crear carpetas, archivos, navegar, buscar).
