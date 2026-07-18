# Máquinas de Estado: Material Complementario

Profundización y ejemplos prácticos en pseudocódigo, Python y C++ para entender y aplicar máquinas de estado en sistemas embebidos automotrices.

---

## 📚 Índice

1. [Teoría Profunda](#teoría-profunda)
2. [Ejemplos en PSeInt](#ejemplos-en-pseint)
3. [Ejemplos en Python](#ejemplos-en-python)
4. [Ejemplos en C++](#ejemplos-en-c)
5. [Casos de Uso Automotrices](#casos-de-uso-automotrices)
6. [Ejercicios Prácticos](#ejercicios-prácticos)

---

## Teoría Profunda

### Definición Formal

Una **máquina de estados finitos (FSM - Finite State Machine)** se define formalmente como:

```
M = (Q, Σ, δ, q₀, F)

Donde:
  Q   = conjunto de estados finitos
  Σ   = alfabeto de eventos (entrada)
  δ   = función de transición: δ(estado, evento) → nuevo_estado
  q₀  = estado inicial
  F   = conjunto de estados finales (aceptación)
```

**Ejemplo simplificado:**
```
Máquina de lámpara:
  Q   = {Apagada, Encendida}
  Σ   = {Botón}
  δ   = {(Apagada, Botón) → Encendida, (Encendida, Botón) → Apagada}
  q₀  = Apagada
  F   = {Apagada} (estado final después de terminar)
```

### Tipos de Máquinas de Estado

#### 1. **Máquinas Deterministas (DFA)**
- Dado un estado y evento, hay **exactamente un** nuevo estado
- Predecibles, fáciles de debuggear
- Más comunes en sistemas embebidos

#### 2. **Máquinas No-Deterministas (NFA)**
- Dado un estado y evento, puede haber **múltiples** nuevos estados posibles
- Más complejas, menos usadas en control de sistemas

#### 3. **Máquinas de Moore**
- La salida depende **solo del estado actual**
- Salida = f(estado)
- Útil para sistemas donde la acción es independiente del evento

#### 4. **Máquinas de Mealy**
- La salida depende **del estado actual Y del evento**
- Salida = f(estado, evento)
- Más eficiente, requiere menos estados

**Ejemplo comparativo (Puerta automática):**

**Moore** (salida = estado):
```
Estado: Cerrada        → Acción: Nada
Estado: Abriendo       → Acción: Mover motor arriba
Estado: Abierta        → Acción: Mantener motor arriba
Estado: Cerrando       → Acción: Mover motor abajo
```

**Mealy** (salida = estado + evento):
```
Estado: Cerrada + evento Detecta → Acción: Mover motor arriba
Estado: Abierta  + evento Tiempo → Acción: Mover motor abajo
Estado: Abierta  + evento Obstáculo → Acción: Nada (mantener)
```

### Transiciones vs. Acciones

**Importante:** Distinguir entre:

- **Transición**: cambio de estado (`estado ← nuevo_estado`)
- **Acción**: operación ejecutada (`ejecutar_codigo()`)

Pueden ocurrir:
1. **En la transición**: acción al cambiar de estado
2. **En el estado**: acción mientras se está en el estado
3. **Al salir del estado**: acción antes de abandonar

**Ejemplo en pseudocódigo:**
```pseudocodigo
Si evento = "Botón" Entonces
  // Acción al salir del estado
  apagarLED()
  
  // Transición
  estado ← Nuevo
  
  // Acción en la transición
  prenderLED()
  
  // Acción en el nuevo estado (siguiente iteración)
FinSi
```

### Lazos y Bifurcaciones

**Lazo Cerrado:**
```
A → B → C → A (regresa al origen)
```
Características:
- Sistema cíclico
- Permanente
- Nunca "termina"
- Común en embebidos

**Bifurcación:**
```
Estado A
  ├→ Evento 1 → B
  └→ Evento 2 → C
```
Características:
- Decisión en transición
- Múltiples caminos posibles
- Ejemplo: puerta con persona registrada vs. no registrada

---

## Ejemplos en PSeInt

### Ejemplo 1: Lámpara Simple (Binaria)

```pseudocodigo
Algoritmo Lampara
  Definir estado Como Entero
  Definir boton Como Entero
  Definir salir Como Lógico
  
  estado ← 0  // 0 = apagada, 1 = encendida
  salir ← Falso
  
  Mientras salir = Falso Hacer
    // Mostrar estado actual
    Escribir "────────────────────"
    Si estado = 0 Entonces
      Escribir "🔴 LÁMPARA: APAGADA"
    Sino
      Escribir "🟢 LÁMPARA: ENCENDIDA"
    FinSi
    Escribir "────────────────────"
    
    // Menú de opciones
    Escribir "1 = Presionar botón"
    Escribir "2 = Salir"
    Leer boton
    
    // Procesamiento de evento
    Según boton Hacer
      Caso 1:
        // Transición: cambiar estado
        Si estado = 0 Entonces
          estado ← 1
          Escribir "[→] Lámpara encendida"
        Sino
          estado ← 0
          Escribir "[→] Lámpara apagada"
        FinSi
      
      Caso 2:
        salir ← Verdadero
        Escribir "Programa terminado"
      
      Por Defecto:
        Escribir "❌ Opción inválida"
    FinSegún
  FinMientras
FinAlgoritmo
```

### Ejemplo 2: Semáforo (3 Estados)

```pseudocodigo
Algoritmo Semaforo
  Definir estado Como Entero
  Definir contador Como Entero
  Definir seguir Como Lógico
  
  // Estados: 0=Verde, 1=Amarillo, 2=Rojo
  estado ← 0
  seguir ← Verdadero
  contador ← 0
  
  Mientras seguir Hacer
    // Mostrar estado
    Escribir "─────────────"
    Según estado Hacer
      Caso 0:
        Escribir "🟢 VERDE"
        contador ← contador + 1
        Si contador >= 30 Entonces  // 30 segundos
          estado ← 1
          contador ← 0
        FinSi
      
      Caso 1:
        Escribir "🟡 AMARILLO"
        contador ← contador + 1
        Si contador >= 5 Entonces  // 5 segundos
          estado ← 2
          contador ← 0
        FinSi
      
      Caso 2:
        Escribir "🔴 ROJO"
        contador ← contador + 1
        Si contador >= 20 Entonces  // 20 segundos
          estado ← 0
          contador ← 0
        FinSi
    FinSegún
    
    Escribir "Tiempo: " contador "s"
    Escribir "─────────────"
    Escribir "Presiona ENTER..."
    Leer  // Simular pausa
  FinMientras
FinAlgoritmo
```

### Ejemplo 3: Puerta Automática (Con Bifurcaciones)

```pseudocodigo
Algoritmo PuertaAutomatica
  Definir estado Como Entero
  Definir evento Como Entero
  Definir contador Como Entero
  Definir salir Como Lógico
  
  // Estados: 0=Cerrada, 1=Abriendo, 2=Abierta, 3=Cerrando, 4=Error
  estado ← 0
  contador ← 0
  salir ← Falso
  
  Mientras salir = Falso Hacer
    Escribir "════════════════════════"
    
    // Reportar estado
    Según estado Hacer
      Caso 0:
        Escribir "🚪 Estado: CERRADA"
      Caso 1:
        Escribir "🚪 Estado: ABRIENDO"
      Caso 2:
        Escribir "🚪 Estado: ABIERTA"
      Caso 3:
        Escribir "🚪 Estado: CERRANDO"
      Caso 4:
        Escribir "⚠️  Estado: ERROR"
    FinSegún
    
    // Menú de eventos
    Escribir "════════════════════════"
    Escribir "1 = Detecta persona"
    Escribir "2 = Fin de apertura"
    Escribir "3 = Transcurre tiempo (cierre)"
    Escribir "4 = Detecta obstáculo"
    Escribir "5 = Fin de cierre"
    Escribir "6 = Reiniciar"
    Escribir "0 = Salir"
    Leer evento
    
    // Máquina de estados
    Según estado Hacer
      // ESTADO: Cerrada
      Caso 0:
        Según evento Hacer
          Caso 1:
            estado ← 1
            Escribir "[→] Abriendo..."
          Caso 0:
            salir ← Verdadero
          Por Defecto:
            Escribir "❌ Evento no válido para este estado"
        FinSegún
      
      // ESTADO: Abriendo
      Caso 1:
        Según evento Hacer
          Caso 2:
            estado ← 2
            contador ← 0
            Escribir "[→] Completamente abierta"
          Por Defecto:
            Escribir "❌ Esperando fin de apertura..."
        FinSegún
      
      // ESTADO: Abierta
      Caso 2:
        Según evento Hacer
          Caso 3:
            estado ← 3
            Escribir "[→] Cerrando..."
          Caso 4:
            Escribir "[!] Obstáculo detectado"
            Escribir "[→] Se abre nuevamente"
            estado ← 2
          Por Defecto:
            Escribir "❌ Evento no válido"
        FinSegún
      
      // ESTADO: Cerrando
      Caso 3:
        Según evento Hacer
          Caso 5:
            estado ← 0
            Escribir "[→] Completamente cerrada"
          Caso 4:
            estado ← 4
            Escribir "[!] OBSTÁCULO EN CIERRE"
            Escribir "[!] Entrando en estado ERROR"
          Por Defecto:
            Escribir "❌ Esperando fin de cierre..."
        FinSegún
      
      // ESTADO: Error
      Caso 4:
        Según evento Hacer
          Caso 6:
            estado ← 0
            Escribir "[✓] Sistema reiniciado"
          Por Defecto:
            Escribir "❌ Estado ERROR - Solo opción 6 (reiniciar)"
        FinSegún
    FinSegún
    
    Escribir "════════════════════════"
  FinMientras
  
  Escribir "Programa terminado"
FinAlgoritmo
```

---

## Ejemplos en Python

### Ejemplo 1: Lámpara en Python

```python
class Lampara:
    """Máquina de estados para una lámpara simple"""
    
    def __init__(self):
        self.estado = "apagada"  # Estado inicial
    
    def presionar_boton(self):
        """Evento: presionar botón"""
        if self.estado == "apagada":
            self.estado = "encendida"
            return "💡 Lámpara encendida"
        else:
            self.estado = "apagada"
            return "🔴 Lámpara apagada"
    
    def obtener_estado(self):
        return self.estado.upper()
    
    def run(self):
        """Ejecutar máquina de estados interactiva"""
        while True:
            print(f"\n{'='*30}")
            print(f"Estado: {self.obtener_estado()}")
            print(f"{'='*30}")
            print("1 = Presionar botón")
            print("2 = Salir")
            
            opcion = input("Selecciona: ")
            
            if opcion == "1":
                print(self.presionar_boton())
            elif opcion == "2":
                print("Programa terminado")
                break
            else:
                print("❌ Opción inválida")

# Uso
if __name__ == "__main__":
    lampara = Lampara()
    lampara.run()
```

### Ejemplo 2: Semáforo en Python

```python
class Semaforo:
    """Máquina de estados para un semáforo"""
    
    ESTADOS = ["verde", "amarillo", "rojo"]
    DURACIONES = {"verde": 30, "amarillo": 5, "rojo": 20}
    
    def __init__(self):
        self.estado_actual = 0  # Índice en ESTADOS
        self.contador = 0
    
    @property
    def estado(self):
        return self.ESTADOS[self.estado_actual]
    
    def avanzar_tiempo(self):
        """Simular paso de tiempo"""
        self.contador += 1
        
        duracion = self.DURACIONES[self.estado]
        if self.contador >= duracion:
            self.estado_actual = (self.estado_actual + 1) % len(self.ESTADOS)
            self.contador = 0
            return True  # Cambio de estado
        return False
    
    def mostrar(self):
        emojis = {"verde": "🟢", "amarillo": "🟡", "rojo": "🔴"}
        print(f"{emojis[self.estado]} {self.estado.upper()}: {self.contador}s")
    
    def simular(self, pasos=50):
        """Simular N pasos de tiempo"""
        for i in range(pasos):
            self.mostrar()
            if self.avanzar_tiempo():
                print(f"  ↓ Cambio a {self.estado}")
            import time
            time.sleep(0.1)

# Uso
if __name__ == "__main__":
    semaforo = Semaforo()
    semaforo.simular()
```

### Ejemplo 3: Puerta Automática en Python (Versión Completa)

```python
from enum import Enum
from typing import Dict, Callable

class EstadoPuerta(Enum):
    CERRADA = 0
    ABRIENDO = 1
    ABIERTA = 2
    CERRANDO = 3
    ERROR = 4

class EventoPuerta(Enum):
    DETECTA_PERSONA = "detecta"
    FIN_APERTURA = "abre_fin"
    TIEMPO_TRANSCURRE = "tiempo"
    DETECTA_OBSTACULO = "obstaculo"
    FIN_CIERRE = "cierra_fin"
    REINICIAR = "reinicia"

class PuertaAutomatica:
    """Máquina de estados para puerta automática con transiciones"""
    
    def __init__(self):
        self.estado = EstadoPuerta.CERRADA
        self.evento_anterior = None
    
    def procesar_evento(self, evento: EventoPuerta) -> str:
        """
        Procesar evento según estado actual.
        Retorna: descripción de lo que pasó
        """
        
        # Tabla de transiciones: {(estado, evento): nuevo_estado}
        transiciones = {
            # Desde CERRADA
            (EstadoPuerta.CERRADA, EventoPuerta.DETECTA_PERSONA): 
                EstadoPuerta.ABRIENDO,
            
            # Desde ABRIENDO
            (EstadoPuerta.ABRIENDO, EventoPuerta.FIN_APERTURA):
                EstadoPuerta.ABIERTA,
            
            # Desde ABIERTA
            (EstadoPuerta.ABIERTA, EventoPuerta.TIEMPO_TRANSCURRE):
                EstadoPuerta.CERRANDO,
            (EstadoPuerta.ABIERTA, EventoPuerta.DETECTA_OBSTACULO):
                EstadoPuerta.ABIERTA,  # Se mantiene en ABIERTA
            
            # Desde CERRANDO
            (EstadoPuerta.CERRANDO, EventoPuerta.FIN_CIERRE):
                EstadoPuerta.CERRADA,
            (EstadoPuerta.CERRANDO, EventoPuerta.DETECTA_OBSTACULO):
                EstadoPuerta.ERROR,
            
            # Desde ERROR
            (EstadoPuerta.ERROR, EventoPuerta.REINICIAR):
                EstadoPuerta.CERRADA,
        }
        
        # Buscar transición válida
        clave = (self.estado, evento)
        
        if clave in transiciones:
            nuevo_estado = transiciones[clave]
            self.estado = nuevo_estado
            return self._generar_mensaje(evento, nuevo_estado)
        else:
            return f"❌ Evento inválido en estado {self.estado.name}"
    
    def _generar_mensaje(self, evento: EventoPuerta, nuevo_estado: EstadoPuerta) -> str:
        """Generar mensaje de transición"""
        mensajes = {
            EventoPuerta.DETECTA_PERSONA: "Persona detectada → Abriendo puerta",
            EventoPuerta.FIN_APERTURA: "Puerta completamente abierta",
            EventoPuerta.TIEMPO_TRANSCURRE: "Tiempo transcurrido → Cerrando puerta",
            EventoPuerta.DETECTA_OBSTACULO: "⚠️  Obstáculo detectado",
            EventoPuerta.FIN_CIERRE: "Puerta completamente cerrada",
            EventoPuerta.REINICIAR: "✓ Sistema reiniciado",
        }
        return f"[→] {mensajes.get(evento, 'Transición')} → {nuevo_estado.name}"
    
    def obtener_estado_emoji(self) -> str:
        emojis = {
            EstadoPuerta.CERRADA: "🚪",
            EstadoPuerta.ABRIENDO: "📂",
            EstadoPuerta.ABIERTA: "📂",
            EstadoPuerta.CERRANDO: "🚪",
            EstadoPuerta.ERROR: "⚠️",
        }
        return emojis[self.estado]
    
    def run_interactivo(self):
        """Ejecutar en modo interactivo"""
        eventos_mapa = {
            "1": EventoPuerta.DETECTA_PERSONA,
            "2": EventoPuerta.FIN_APERTURA,
            "3": EventoPuerta.TIEMPO_TRANSCURRE,
            "4": EventoPuerta.DETECTA_OBSTACULO,
            "5": EventoPuerta.FIN_CIERRE,
            "6": EventoPuerta.REINICIAR,
        }
        
        while True:
            print(f"\n{'='*40}")
            print(f"{self.obtener_estado_emoji()} Estado: {self.estado.name}")
            print(f"{'='*40}")
            print("Eventos disponibles:")
            print("1 = Detecta persona")
            print("2 = Fin de apertura")
            print("3 = Transcurre tiempo (cierre)")
            print("4 = Detecta obstáculo")
            print("5 = Fin de cierre")
            print("6 = Reiniciar")
            print("0 = Salir")
            
            opcion = input("Selecciona evento: ").strip()
            
            if opcion == "0":
                print("Programa terminado")
                break
            elif opcion in eventos_mapa:
                evento = eventos_mapa[opcion]
                mensaje = self.procesar_evento(evento)
                print(mensaje)
            else:
                print("❌ Opción no válida")

# Uso
if __name__ == "__main__":
    puerta = PuertaAutomatica()
    puerta.run_interactivo()
```

---

## Ejemplos en C++

### Ejemplo 1: Lámpara en C++

```cpp
#include <iostream>
using namespace std;

enum Estado { APAGADA = 0, ENCENDIDA = 1 };

class Lampara {
private:
    Estado estado;

public:
    Lampara() : estado(APAGADA) {}
    
    void presionar_boton() {
        if (estado == APAGADA) {
            estado = ENCENDIDA;
            cout << "💡 Lámpara encendida\n";
        } else {
            estado = APAGADA;
            cout << "🔴 Lámpara apagada\n";
        }
    }
    
    void mostrar_estado() {
        cout << "Estado: " << (estado == APAGADA ? "APAGADA" : "ENCENDIDA") << endl;
    }
    
    void run() {
        int opcion;
        while (true) {
            cout << "\n==========================\n";
            mostrar_estado();
            cout << "==========================\n";
            cout << "1 = Presionar botón\n";
            cout << "2 = Salir\n";
            cout << "Selecciona: ";
            cin >> opcion;
            
            switch (opcion) {
                case 1:
                    presionar_boton();
                    break;
                case 2:
                    cout << "Programa terminado\n";
                    return;
                default:
                    cout << "❌ Opción inválida\n";
            }
        }
    }
};

int main() {
    Lampara lampara;
    lampara.run();
    return 0;
}
```

### Ejemplo 2: Máquina de Estados Genérica en C++

```cpp
#include <iostream>
#include <map>
#include <functional>
using namespace std;

template<typename Estado, typename Evento>
class MaquinaEstados {
private:
    Estado estado_actual;
    map<pair<Estado, Evento>, pair<Estado, function<void()>>> transiciones;

public:
    MaquinaEstados(Estado inicial) : estado_actual(inicial) {}
    
    void agregar_transicion(
        Estado estado,
        Evento evento,
        Estado nuevo_estado,
        function<void()> accion = []() {}
    ) {
        transiciones[{estado, evento}] = {nuevo_estado, accion};
    }
    
    bool procesar_evento(Evento evento) {
        auto it = transiciones.find({estado_actual, evento});
        if (it != transiciones.end()) {
            it->second.second();  // Ejecutar acción
            estado_actual = it->second.first;  // Cambiar estado
            return true;
        }
        return false;
    }
    
    Estado obtener_estado() const {
        return estado_actual;
    }
};

// Uso con enums
enum EstadoLampara { APAGADA = 0, ENCENDIDA = 1 };
enum EventoLampara { BOTON = 0 };

int main() {
    MaquinaEstados<EstadoLampara, EventoLampara> lampara(APAGADA);
    
    // Definir transiciones
    lampara.agregar_transicion(
        APAGADA, BOTON, ENCENDIDA,
        []() { cout << "💡 Encendiendo...\n"; }
    );
    
    lampara.agregar_transicion(
        ENCENDIDA, BOTON, APAGADA,
        []() { cout << "🔴 Apagando...\n"; }
    );
    
    // Usar
    lampara.procesar_evento(BOTON);
    cout << "Estado actual: " << lampara.obtener_estado() << endl;
    
    lampara.procesar_evento(BOTON);
    cout << "Estado actual: " << lampara.obtener_estado() << endl;
    
    return 0;
}
```

---

## Casos de Uso Automotrices

### 1. Sensor de Proximidad Trasero (Parking)

```pseudocodigo
// Estados: 0=Normal, 1=Alerta, 2=Peligro, 3=Error

// En estado Normal:
//   - Lee distancia del sensor
//   - Si distancia < 1 metro → cambiar a Alerta
//   - Si error en sensor → cambiar a Error

// En estado Alerta:
//   - Sonido leve cada 0.5s
//   - Si distancia < 0.3 metros → cambiar a Peligro
//   - Si distancia > 1 metro → cambiar a Normal

// En estado Peligro:
//   - Sonido constante
//   - Luz roja parpadeante
//   - Si sensor falla → cambiar a Error

// En estado Error:
//   - Mantener último valor conocido
//   - Mensaje en pantalla: "SENSOR FALLA"
//   - Esperar reinicio o sensor recupere
```

### 2. Sistema de Puertas Eléctricas (Bloqueo Infantil)

```
Estados:
  - CERRADA (normal, puerta cerrada)
  - ABRIENDO (proceso de abrir)
  - ABIERTA (puerta abierta)
  - BLOQUEADA_INFANTIL (no responde a comandos traseros)
  - ERROR (puerta no responde)

Eventos:
  - Usuario presiona botón delantero
  - Usuario presiona botón trasero
  - Sensor detecta puerta abierta/cerrada
  - Botón bloqueo infantil se activa/desactiva
  - Timeout (motor no responde en tiempo esperado)

Máquina:
  CERRADA + botón_delantero → ABRIENDO (siempre permite)
  CERRADA + botón_trasero → si(infantil_activo) ERROR else ABRIENDO
  ABRIENDO + sensor_abierto → ABIERTA
  ABIERTA + botón_delantero → CERRANDO (siempre permite)
  ABIERTA + botón_trasero → si(infantil_activo) BLOQUEADA_INFANTIL else CERRANDO
  ... + timeout → ERROR
```

### 3. Control de Transmisión (Marcha/Estacionamiento)

```
Estados:
  - PARK (estacionado)
  - REVERSE (reversa)
  - NEUTRAL (punto muerto)
  - DRIVE (conducción)

Condiciones de transición:
  PARK → DRIVE solo si:
    - Freno presionado
    - RPM del motor en rango normal
    - Puerta cerrada
  
  DRIVE → PARK solo si:
    - Velocidad = 0
    - Freno presionado

  Cualquier estado → ERROR si:
    - Motor se apaga inesperadamente
    - Sensor de posición falla
```

---

## Ejercicios Prácticos

### Ejercicio 1: Semáforo Peatonal
**Dificultad: Fácil**

Diseña una máquina de estados para un semáforo peatonal:
- **Estados**: Rojo, Verde, Parpadeante
- **Eventos**: Botón presionado, Tiempo transcurre
- **Requisitos**:
  - Rojo dura 30s
  - Verde dura 20s
  - Parpadeante dura 5s (parpadea 10 veces)
  - Si botón se presiona en Rojo, inicia cuenta regresiva visible

**Implementa en**: PSeInt y Python

---

### Ejercicio 2: Máquina Expendedora
**Dificultad: Medio**

Máquina que vende refrescos:
- **Estados**: Esperando, Dinero recibido, Seleccionando, Dispensando, Error
- **Eventos**: 
  - Moneda insertada (10, 20, 50 pesos)
  - Botón producto seleccionado
  - Producto agotado
  - Falla mecánica

**Requisitos**:
- Refresco cuesta 30 pesos
- Si falta dinero, esperar más monedas
- Si hay suficiente y se selecciona → Dispensar
- Si error → Devolver dinero

**Dibujar**: Tabla de transiciones

---

### Ejercicio 3: Control de Motor DC
**Dificultad: Medio**

Motor que puede estar:
- **Estados**: Parado, Acelerando, Velocidad constante, Desacelerando, Falla
- **Eventos**:
  - Comando arrancar
  - Velocidad objetivo alcanzada
  - Comando frenar
  - Sobrecalentamiento detectado
  - Error sensor RPM

**Requisitos**:
- Acelerar: aumentar PWM gradualmente (10% cada iteración)
- Velocidad constante: mantener PWM actual
- Desacelerar: disminuir PWM gradualmente
- Falla: parar motor, esperar reset

**Implementa en**: C++ con PWM simulado

---

### Ejercicio 4: Puerta Automática Completa
**Dificultad: Difícil**

Mejora el ejemplo de clase:
- **Estados** adicionales: Mantenimiento (prueba de sensores)
- **Eventos** adicionales: 
  - Fallo en sensor de apertura
  - Fallo en sensor de cierre
  - Botón emergencia
  - Timeout genérico
- **Acciones**:
  - Log de cada transición (escribir a archivo)
  - Contador de veces abierta/cerrada
  - Estadísticas de tiempo en cada estado

**Requisitos**:
- Máximo 5 segundos en Abriendo/Cerrando
- Si timeout → ERROR
- En ERROR, intentar reset automático (máximo 3 veces)
- Después de 3 fallos → Requiere intervención manual

**Implementa en**: Python (con logging)

---

## Checklist de Comprensión

Asegúrate de entender:

- [ ] Diferencia entre estado y evento
- [ ] Diferencia entre transición y acción
- [ ] Qué es un lazo cerrado y una bifurcación
- [ ] Por qué usar `switch`/`Según` para máquinas de estado
- [ ] Máquinas deterministas vs no-deterministas
- [ ] Moore vs Mealy
- [ ] Ciclos infinitos en embebidos
- [ ] Cómo debuggear: verificar estado actual antes de actuar
- [ ] Cómo dibujar diagrama de transiciones
- [ ] Casos automotrices: ECU, puertas, sensores

---

## Recursos Adicionales

### Referencias Teóricas
- Introducción a Teoría de Autómatas (Hopcroft & Ullman)
- Patrones de diseño: State Pattern (Gang of Four)
- UML State Machine Diagrams

### Herramientas
- **Draw.io**: Dibujar diagramas de máquinas de estado
- **Graphviz**: Generar diagramas desde código
- **JFLAP**: Simulador de máquinas de estados

### Casos de Estudio Reales
- Arduino State Machine Library
- ROS State Machine Framework (Robotics)
- Qt State Machine Framework (Desktop/Embedded)

---

**Última actualización**: 17/07/2026  
**Autor**: Material complementario generado para profundización  
**Próximos**: Ejercicios solucionados en próximas sesiones
