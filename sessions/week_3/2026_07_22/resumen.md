---
title: "Sesión Week 3 - 2026_07_22"
date: 2026-07-22
week: 3
bloque: "1"
temas:
  - "Sesión de dudas (sin tema nuevo)"
  - "Repaso rápido de la evaluación para estudiante nuevo"
  - "Clasificación de señales: válida / inválida / ausente"
  - "Máquina de estados del ACU (repaso de transiciones)"
  - "Redacción de requisitos verificables"
  - "Setup de entorno: WSL + Debian + build-essential"
  - "Compilación manual con g++ desde terminal Linux"
  - "Visual Studio Professional vs Visual Studio Code"
duracion_minutos: 60
tipo_sesion: "dudas + soporte técnico"
---

# Sesión 3 - Miércoles 22/07/2026
## Sesión de Dudas: Repaso de la Evaluación y Setup del Entorno Linux

### Contexto General

- **Bloque**: 1 (Especialidad Automotriz)
- **Tipo de sesión**: Dudas y soporte — **no hay tema nuevo**
- **Objetivo**: Poner al día a estudiantes nuevos y dejar el entorno de desarrollo listo para el Rango 1
- **Estructura**: ~50% repaso acelerado de la evaluación, ~50% troubleshooting en vivo de WSL/Debian

---

## 1. Presentación del Profesor (para estudiante nuevo)

**Óscar Godínez** — perfil compartido con el grupo:

- Ingeniero en Mecatrónica, Maestro en Ciencias, doctorante en Ciencias de la Ingeniería
- **+4 años en industria automotriz**, principalmente en **Continental**
- Desarrollo de tecnología para distintas marcas de vehículos y plataformas
- Especialidad: **algoritmos de radar embebidos** — con foco en **optimización de memoria** y rendimiento

**Nota**: se integra un estudiante nuevo (aún cursando su carrera, por terminar). Se le indica revisar las grabaciones — no todas, pero **mínimo las dos últimas** (ECU + máquina de estados) y la de configuración de Linux.

---

## 2. Repaso Acelerado de la Evaluación

### Modelo básico de una ECU

```
Entradas (sensores) → Procesamiento (validar / decidir) → Salidas (actuadores, alarmas, mensajes)
```

Ejemplo: se recibe temperatura de un sensor → se compara contra el límite (105 °C) → si es mayor, se decide **activar ventilador** o **limitar la operación**.

**Idea central**: se toma una **medición física** y se convierte en una **decisión lógica**, y después se ejecuta algo.

- Si la temperatura está apenas sobre el umbral → activar ventilador puede bastar
- Si sigue subiendo → limitar operación (algo está mal en el motor)

### Por qué son dos ACUs

| ACU | Rol |
|-----|-----|
| **Gateway** | Recibe mensajes (cadenas con valores de sensores), **valida** rango / formato / coherencia temporal, **filtra** y **reenvía** al ACU de control |
| **Control** | **Analiza y evalúa** las señales ya clasificadas, aplica condiciones y **decide el cambio de estado** de la máquina |

Si el Gateway marca una señal como inválida, igual se la manda al Control — el Control decide qué hacer con esa marca (ej. "una señal inválida me lleva a falla").

### Origen de los datos en este hito

- **No hay simulación todavía**: los valores los mete el **propio usuario** por teclado
- Opciones de diseño (libre elección del equipo):
  - Una **cadena por ciclo** con todos los valores (cada cadena = un nuevo tiempo)
  - O un **mensaje por sensor**
- Se sugiere jugar con **valores inválidos** y **tiempos inválidos** para probar el flujo
- En el **siguiente hito** (ya en código) se podrán simular señales o generar randoms

---

## 3. Clasificación de Señales

Regla dada por el profesor:

| Clasificación | Condición |
|---------------|-----------|
| **VÁLIDA** | Sí y solo sí está **dentro del rango** **Y** llega **en tiempo** |
| **INVÁLIDA** | Está **fuera de rango** (ej. velocidad negativa) |
| **AUSENTE** | Se perdió la **coherencia temporal** (timeout) |

**Ejemplo de ausencia**: la señal viene correcta en valor, pero debería refrescarse cada 10/100 ms y no se actualiza en 10 s → ya no es confiable → se trata como inválida.

> **Ausente ≠ fuera de rango.** Son causas distintas de invalidez.

**Opcional**: se puede agregar un **cuarto estado** para señales que no cumplen ninguna de las dos condiciones (señal completamente errónea). Con dos clasificaciones es suficiente para aprobar.

El Gateway también debe verificar que **no haya señales atípicas** y que no se hayan **perdido datos en ciertos ciclos**.

---

## 4. Estructura del Mensaje

Un mensaje es una **cadena** que entrega los valores de las señales **más un estatus**.

| Opción | Descripción | Recomendación |
|--------|-------------|---------------|
| **Estatus por señal** | El Gateway cambia el estatus de cada señal individualmente | ✅ Mejor diseño |
| **Estatus general** | Un solo estatus para todo el mensaje | Más fácil, aceptable |

### Flujo del mensaje

```
Se genera la señal
   ↓
Se construye el mensaje con las señales
   ↓
Gateway lo recibe y lo valida
   ↓
Gateway lo distribuye al ACU de Control
   ↓
Control revisa las señales:
   • ¿Alguna inválida?          → error
   • ¿Todas válidas pero alguna elevada? → DEGRADED (sobrecalentamiento ligero)
   • ¿Falla crítica? (ej. batería 8 V)   → SAFE_STATE
```

**Ejemplo crítico**: batería marcando **8 V** → "esa batería está muerta" → directo a **SAFE_STATE**. Por debajo de 9 V ya se considera crítica.

---

## 5. Máquina de Estados (repaso)

### Definición operativa

Una máquina de estados es un sistema que **reporta su estatus constantemente**, y el **nuevo estatus depende del anterior + una acción/evento**.

Elementos a definir:
1. **Estados posibles**
2. **Acciones de cada estado** (qué pasa mientras estás en él)
3. **Eventos** que producen los cambios
4. **Condiciones de la transición**
5. **Estado inicial** (el default)

Notación: `Estado actual + Evento → Nuevo estado`

**Ejemplo simple**: una lámpara — dos estados (apagada/encendida), el evento es el botonazo, sin acciones internas. Nota importante: no en todas las máquinas la misma acción produce el mismo resultado; una misma acción puede llevar a estados distintos según el estado de origen.

### Los 6 estados propuestos

| Estado | Rol |
|--------|-----|
| **INIT** | Estado default/inicial; inicializa variables y señales |
| **SELF_TEST** | Revisa que las variables iniciales no sean atípicas |
| **OPERATIONAL** | Estado de ciclado normal; actualiza y revisa señales cada ciclo |
| **DEGRADED** | Fallas mínimas / recuperables |
| **SAFE_STATE** | Fallas graves; **sin salida** salvo apagar |
| **SHUTDOWN** | Apagado solicitado por el usuario |

### Qué hace INIT concretamente

Es la primera parte del pseudocódigo:
- `estado_actual ← INIT`
- Inicializar señales: velocidad en 0, batería en 11-12 V (valores buenos), RPM en 0, etc.

### Qué revisa SELF_TEST

Verifica que las variables iniciales sean coherentes:
- Las que deben estar en cero, que estén en cero (una velocidad ≠ 0 al encender el carro no tiene sentido)
- Si la batería arranca con voltaje bajo → el self test sale mal
- Es un buen lugar para "jugar" con valores iniciales malos y probar las 3 salidas

### Transiciones

```
INIT → SELF_TEST                        (única transición posible desde INIT)
SELF_TEST → OPERATIONAL                 (sin fallas)
SELF_TEST → DEGRADED                    (falla chiquita)
SELF_TEST → SAFE_STATE                  (falla crítica)
OPERATIONAL → DEGRADED                  (falla menor en algún ciclo)
DEGRADED → OPERATIONAL                  (se recupera)
DEGRADED → SAFE_STATE                   (la falla no se recupera y se vuelve crítica)
OPERATIONAL → SAFE_STATE                (falla crítica directa)
SAFE_STATE → SHUTDOWN                   (única salida: apagar el vehículo)
OPERATIONAL / DEGRADED → SHUTDOWN       ("llavazo" de apagado)
SHUTDOWN → (terminal)
```

### Aclaración importante: la máquina NO es cíclica

No hay forma de pasar de **SHUTDOWN a INIT** sin reiniciar todo. Lo que lleva de SHUTDOWN a INIT es el **"llavazo"** de apagado + encendido, que es una **acción externa del usuario**. En la simulación: detener la ejecución del programa y volver a ejecutarlo.

> **La máquina de estados no representa el funcionamiento completo del sistema**: solo indica qué estados hay y cómo se pasa de uno a otro. El **pseudocódigo y el diagrama son cosas distintas** (el pseudocódigo muestra operaciones y decisiones).

### Flujo del pseudocódigo (ejemplificación)

```
Inicio del programa
  → Inicializar variables (INIT)
  → SELF_TEST: revisar variables
      • Todo bien  → OPERATIONAL
      • Algo mal   → estado de error
  → OPERATIONAL: leer y validar mensajes en ciclo
      Cada ciclo preguntar:
        ¿Hay falla crítica?  → SAFE_STATE
        ¿Hay falla no crítica? → DEGRADED
        Si no hay falla       → seguir en OPERATIONAL
  → En DEGRADED, cada ciclo:
        ¿La falla empeoró a crítica? → SAFE_STATE
        ¿El sistema se recuperó?     → OPERATIONAL
        Si no                        → seguir en DEGRADED
  → SAFE_STATE: única pregunta = "¿solicitar apagado?"
        Sí → SHUTDOWN
        No → permanece en SAFE_STATE
```

**Nota del profesor**: al diagrama de ejemplo le faltan flechas — cada equipo debe poder irse a **SHUTDOWN** desde OPERATIONAL, DEGRADED o donde considere.

---

## 6. Requisitos Funcionales

### Fórmula

```
[El sistema X] + [deberá] + [acción verificable] + [condición]
```

| Calidad | Ejemplo |
|---------|---------|
| ❌ Vago | "El sistema deberá funcionar correctamente" → no dice nada, no se puede testear |
| ✅ Válido | "El sistema (Gateway) deberá validar que la velocidad se encuentre dentro del rango permitido antes de enviarla al ACU de Control" |
| ✅✅ Mejor | "…que la velocidad se encuentre **dentro del rango de 0 a 250** antes de enviarla al ACU de Control" (más específico) |
| ✅ Válido | "El sistema deberá marcar como inválido cualquier valor de acelerador menor a 0% o mayor a 100%" |

### Estrategia sugerida para llegar a 10 requisitos

Ante la duda "no conozco estos sistemas, mis requisitos van a tener la forma pero pueden ser tontería":

1. **5 requisitos de señales** (uno por cada señal): *"El Gateway deberá revisar que la señal X esté dentro del rango [min, max]"*
2. **Requisitos del ACU de Control**, por ejemplo:
   - *"El ACU de Control deberá cambiar el estatus de la máquina de estados a DEGRADED si la señal de temperatura supera el umbral de 100 °C"*
   - *"El ACU de Control deberá cambiar el estatus de la máquina de estados a SAFE_STATE si el voltaje de la batería es menor a 9 V"*

**Regla clave**: los requisitos deben **cumplirse en el pseudocódigo**. Si defines rangos para las 5 señales, el pseudocódigo debe mostrar esas 5 validaciones.

> No importa si el contenido técnico no es perfecto — lo que importa es **respetar el formato** y aprender la mecánica de redactar requisitos, porque con ellos nos vamos a basar cuando empecemos a hacer código.

---

## 7. Entregables y Mecánica (recordatorio)

1. **Pseudocódigo** (Gateway + Control)
2. **Máquina de estados** (diagrama)
3. **Mínimo 10 requisitos**
4. **Video** explicando qué hicieron y cómo lo pensaron

La **rúbrica está en la tarea** del Classroom, indica cuánto vale cada entregable.

### Grabaciones subidas

El profesor subió al Classroom, en vivo durante la clase, la grabación del **martes 21 de julio (20:00 h)** desde Drive. Se aclaró el orden de las clases previas (quedaron "revueltas" la semana pasada: lunes = primera parte de la tarea, martes = segunda parte, jueves = máquinas de estados, miércoles = otra). Hay ~8-10 clases en total desde el 7 de julio.

**Canal de dudas**: chat del curso o WhatsApp, en cualquier momento — incluso sin haber visto las grabaciones.

---

## 8. Visión del Ciclo de Desarrollo (hitos)

El profesor explicó por qué insiste en un buen diseño desde ahora: este entregable es el **esqueleto** de todo lo que sigue.

| Hito | Actividad |
|------|-----------|
| **Hito 0 (actual)** | Diseño conceptual: pseudocódigo + máquina de estados + requisitos |
| **Hito 1** | Pasarlo a **código** (C++), con **Git** y repositorio versionado |
| **Hito 2** | Refactorizar a **orientado a objetos** (clases) |
| **Hito 3** | **Autodiagnóstico** |
| **Hito 4** | Arquitectura con **mejores prácticas** |
| **Hito 5** | **Optimización de memoria** |

**Sobre Git** (tema que sigue): se verá en paralelo al inicio de C++, en una o dos clases rápidas. Requisito para el siguiente hito: **no crear carpetas nuevas por versión** — la misma carpeta debe estar **versionada** en el repositorio entre hito e hito.

**Meta final**: que el software se vuelva **embebido en una placa**, o se simule si no se consigue hardware. Por eso se trabaja sobre **Debian** (base de Ubuntu, más ligero y óptimo; es lo que se usa normalmente en desarrollo de esta área).

---

## 9. Soporte Técnico en Vivo: WSL + Debian (caso de Jorge)

Buena parte de la sesión fue troubleshooting compartiendo pantalla.

### Situación inicial

- Instaló **Visual Studio Professional** (no VS Code), después de verlo en la clase muestra del administrador Alfonso
- Instaló **WSL**, y le apareció un ícono independiente de **Debian**
- Al abrirlo, `ls` no mostraba `System32` como en las clases grabadas, sino los archivos del subsistema Linux

### Aclaración: qué es WSL

- **No es una máquina virtual clásica** — es un **subsistema** administrado por Microsoft
- Es una versión mucho más pequeña y ligera que una VM
- **Vive aparte** del sistema Windows y no afecta los archivos de la computadora
- Que los archivos estén separados **es normal** en Windows 10/11; existen comandos para trasvasar archivos entre sistema y subsistema

### Terminal integrada

- En **Visual Studio Professional**: menú **Ver → Terminal**, y ahí aparece la pestaña de **Debian**, además de Símbolo del sistema y PowerShell
- `/mnt` corresponde al disco duro de Windows montado dentro de Linux
- La extensión de WSL **no aparece** en el gestor de extensiones de Visual Studio Professional (es de VS Code)
- Alternativa usada: abrir desde PowerShell **como administrador**:
  ```powershell
  wsl --list        # verificar que reconoce la distribución
  wsl -d Debian     # entrar (respetar la "D" mayúscula)
  ```

### El problema real: falta de `apt update`

Los `sudo apt install` fallaban con "no le encuentra". Causa: **nunca se corrió `apt update` ni `apt upgrade`** tras instalar Debian, así que la lista local de paquetes estaba vacía.

```bash
sudo apt update     # PRIMERO — actualiza la lista de paquetes
sudo apt upgrade    # DESPUÉS — actualiza los paquetes instalados
```

> **Regla**: siempre que instales una distribución Linux nueva, hay que aplicar `update` y `upgrade`. A diferencia de Windows, la mayoría no se actualiza sola.

### Instalación de herramientas

```bash
sudo apt install build-essential git gdb
sudo apt install cmake        # se verá más adelante
```

Errores de tecleo encontrados en vivo: se escribió `essentials` (con "s" final) varias veces — el nombre correcto es **`build-essential`**, en singular.

### Verificación

```bash
g++ --version
git --version
```

### Compilación y ejecución manual

```bash
g++ source.cpp -o source
ls              # aparece el ejecutable
./source        # ejecutar
```

Se compiló y ejecutó correctamente un ejercicio en C++ de la clase muestra (una especie de ejemplo de clúster con vectores, mensajes y alertas). El profesor pidió que le compartieran ese código para revisarlo, porque se parece a lo que se hará en el hito 1: *"una máquina de estados un poco más avanzada donde ustedes van a estar generando valores y viendo cómo responden"*.

### Otros detalles prácticos

- **Copiar/pegar** en la terminal de Windows es poco confiable — el profesor pegó el comando en el chat para que lo copiaran
- Si la terminal se traba: **Ctrl+C** cancela la ejecución y se vuelve a intentar
- Reiniciar Visual Studio tras la instalación para que apliquen ciertos cambios
- Todo el trabajo del curso será **en Linux**, no compilando desde PowerShell de Windows

---

## 10. Visual Studio Professional vs Visual Studio Code

| Aspecto | VS Code | VS Professional |
|---------|---------|-----------------|
| Curva de aprendizaje | Más fácil, más básico | Más complejo |
| Enfoque | General, ligero | Especializado en C/C++ y herramientas de compilación |
| Limitaciones | — | Algunas funciones avanzadas requieren **licencia** |
| Plan del curso | Hito 0 y 1 | Migración prevista en hito 1 o 2 |

**Decisión**: por ahora **nadie tiene que cambiarse**. El profesor lo consultará con la academia; si se puede, la mudanza se adelanta al hito 1. Quien ya conozca Professional puede usarlo desde ahora sin problema. La intención es que el grupo **conozca ambos mundos**.

**Contexto de industria**: las funciones avanzadas de Professional se usan más para **C solito** que para C++. En la industria automotriz mucho código del carro **se sigue haciendo en C** — los radares de generación 5 hacia atrás son puro C; los nuevos ya combinan o son puro C++. Ahí sí se requerían licencias pagadas (además, publicar/vender software hecho con Visual Studio exige licencia con Microsoft). En contexto académico no hay problema.

### Sobre depuradores

Por ahora **no usar los depuradores del IDE** — se trabajará en "pura comandera" porque es más limpia y se controla más. Más adelante se enseñará a debuggear, ya que **debuggear en este entorno es distinto al debug de otros lenguajes** y es un tema denso.

---

## Preguntas Respondidas

**P: Tengo la idea abstracta de los requerimientos, pero no conozco estos sistemas; algunas cosas van a tener la forma pero pueden ser pura tontería.**
R: No hay problema. Lo importante es **respetar el formato**. Con 5 requisitos de señales (uno por señal, con su rango) y algunos del ACU de Control (cambios de estado por umbral) es suficiente. Lo que sí se exige es que esos requisitos **se cumplan en el pseudocódigo**.

**P: ¿Puedo preguntar por chat o WhatsApp?**
R: Sí, en cualquier momento — mientras veas las grabaciones o incluso sin verlas.

**P (Jorge): Instalé WSL y me generó un ícono de Debian aparte; no me aparece `System32` con `ls`. ¿Es normal?**
R: Sí. WSL es un **subsistema**, no una VM clásica; vive aparte y Windows separa los archivos del subsistema de los del sistema. No afecta nada.

**P (Jorge): ¿Cómo integro la terminal de Debian en Visual Studio Professional?**
R: **Ver → Terminal** → pestaña Debian. La extensión de WSL de VS Code no está disponible en Professional. Alternativa: PowerShell como admin → `wsl -d Debian`.

**P (Jorge): ¿Me recomiendas seguir con Visual Studio Professional o cambiarme?**
R: No pasa nada, sigue con el que tengas mientras encuentres los comandos. En algún punto todos migran a Professional.

**P (Jorge): ¿El código se compilará ya con el sistema Linux?**
R: Sí, todo va a ser con Linux (tanto en VS Code como en Professional), no en la PowerShell de Windows.

---

## Notas Administrativas

- **Asistencia libre hoy** — no cuenta como falta
- La grabación del martes 21/07 quedó publicada en Classroom durante la clase
- Próxima sesión (23/07): revisión de **avances** de los equipos; quien tenga algo específico que checar, se revisa

---

**Duración**: ~60 minutos
**Tipo**: Sesión de dudas + soporte técnico (sin tema nuevo)
**Próxima sesión**: 23/07/2026 (revisión de avances)
**Entrega de evaluación**: Lunes 27/07/2026 (máximo martes 28/07)
