# Torniquete: Implementación en Múltiples Lenguajes

Soluciones de la máquina de estados del torniquete en PSeInt, Python y C++ para comparar sintaxis y enfoques.

---

## 📌 PSeInt - Versión Limpia

```pseudocodigo
Algoritmo Torniquete
  Definir estado Como Entero
  Definir evento Como Entero
  Definir salir Como Lógico
  Definir contador Como Entero
  
  estado ← 0
  salir ← Falso
  contador ← 0
  
  Mientras salir = Falso Hacer
    Escribir "Estado: " Si estado = 0 Entonces "Bloqueado" Sino "Desbloqueado" FinSi
    Escribir "Contador: " contador
    Escribir "1=Moneda, 2=Empujar, 0=Salir"
    Leer evento
    
    Según estado Hacer
      Caso 0:  // BLOQUEADO
        Según evento Hacer
          Caso 1:  // Moneda
            estado ← 1
            Escribir "✓ Desbloqueado"
          Caso 2:  // Empujar
            Escribir "✗ Denegar"
          Caso 0:
            salir ← Verdadero
        FinSegún
      
      Caso 1:  // DESBLOQUEADO
        Según evento Hacer
          Caso 2:  // Empujar
            contador ← contador + 1
            estado ← 0
            Escribir "✓ Paso registrado"
          Caso 1:  // Moneda
            Escribir "ℹ️  Ya desbloqueado"
          Caso 0:
            salir ← Verdadero
        FinSegún
    FinSegún
  FinMientras
  
  Escribir "Total: " contador
FinAlgoritmo
```

---

## 🐍 Python - Versión Orientada a Objetos

### Versión 1: Clase Simple

```python
class Torniquete:
    """Máquina de estados de torniquete"""
    
    BLOQUEADO = 0
    DESBLOQUEADO = 1
    
    def __init__(self):
        self.estado = self.BLOQUEADO
        self.contador = 0
    
    def insertar_moneda(self):
        """Evento: insertar moneda"""
        if self.estado == self.BLOQUEADO:
            self.estado = self.DESBLOQUEADO
            return "✓ Desbloqueado - Puedes pasar"
        else:
            return "ℹ️  Ya está desbloqueado"
    
    def empujar(self):
        """Evento: empujar torniquete"""
        if self.estado == self.DESBLOQUEADO:
            self.contador += 1
            self.estado = self.BLOQUEADO
            return f"✓ Paso registrado (Total: {self.contador})"
        else:
            return "✗ Acceso denegado - Inserta moneda primero"
    
    def obtener_estado(self):
        """Retornar estado actual"""
        return "Bloqueado" if self.estado == self.BLOQUEADO else "Desbloqueado"
    
    def run_interactivo(self):
        """Ejecutar en modo interactivo"""
        while True:
            print(f"\nEstado: {self.obtener_estado()}")
            print(f"Contador: {self.contador}")
            print("1 = Insertar moneda")
            print("2 = Empujar")
            print("0 = Salir")
            
            opcion = input("Selecciona: ").strip()
            
            if opcion == "1":
                print(self.insertar_moneda())
            elif opcion == "2":
                print(self.empujar())
            elif opcion == "0":
                print(f"Total personas: {self.contador}")
                break
            else:
                print("❌ Opción inválida")

# Uso
if __name__ == "__main__":
    torniquete = Torniquete()
    torniquete.run_interactivo()
```

### Versión 2: Con Enum (Más Profesional)

```python
from enum import Enum

class Estado(Enum):
    BLOQUEADO = 0
    DESBLOQUEADO = 1

class Evento(Enum):
    MONEDA = 1
    EMPUJAR = 2

class TorniqueteAvanzado:
    """Torniquete con máquina de estados explícita"""
    
    def __init__(self):
        self.estado = Estado.BLOQUEADO
        self.contador = 0
    
    def procesar_evento(self, evento: Evento) -> str:
        """Procesar evento según estado actual"""
        
        # Tabla de transiciones
        transiciones = {
            (Estado.BLOQUEADO, Evento.MONEDA): 
                (Estado.DESBLOQUEADO, "✓ Desbloqueado"),
            
            (Estado.BLOQUEADO, Evento.EMPUJAR):
                (Estado.BLOQUEADO, "✗ Denegar"),
            
            (Estado.DESBLOQUEADO, Evento.EMPUJAR):
                (Estado.BLOQUEADO, f"✓ Paso {self.contador + 1}"),
            
            (Estado.DESBLOQUEADO, Evento.MONEDA):
                (Estado.DESBLOQUEADO, "ℹ️  Ya desbloqueado"),
        }
        
        clave = (self.estado, evento)
        if clave in transiciones:
            nuevo_estado, mensaje = transiciones[clave]
            
            # Ejecutar acción antes de transición
            if evento == Evento.EMPUJAR and self.estado == Estado.DESBLOQUEADO:
                self.contador += 1
            
            # Cambiar estado
            self.estado = nuevo_estado
            return mensaje
        
        return "❌ Evento inválido"
    
    def __str__(self):
        return f"Estado: {self.estado.name} | Contador: {self.contador}"
    
    def run_interactivo(self):
        """Ejecutar en modo interactivo"""
        eventos_mapa = {
            "1": Evento.MONEDA,
            "2": Evento.EMPUJAR,
        }
        
        while True:
            print(f"\n{'='*40}")
            print(self)
            print(f"{'='*40}")
            print("1 = Insertar moneda")
            print("2 = Empujar")
            print("0 = Salir")
            
            opcion = input("Selecciona: ").strip()
            
            if opcion == "0":
                print(f"Total personas: {self.contador}")
                break
            elif opcion in eventos_mapa:
                evento = eventos_mapa[opcion]
                mensaje = self.procesar_evento(evento)
                print(mensaje)
            else:
                print("❌ Opción inválida")

# Uso
if __name__ == "__main__":
    torniquete = TorniqueteAvanzado()
    torniquete.run_interactivo()
```

### Versión 3: Con Logging

```python
from enum import Enum
from datetime import datetime
import json

class Estado(Enum):
    BLOQUEADO = 0
    DESBLOQUEADO = 1

class Evento(Enum):
    MONEDA = 1
    EMPUJAR = 2

class TorniqueteConLog:
    """Torniquete que registra todas las transiciones"""
    
    def __init__(self, archivo_log: str = "torniquete.log"):
        self.estado = Estado.BLOQUEADO
        self.contador = 0
        self.archivo_log = archivo_log
        self.historial = []
        self._registrar("INICIO", "Sistema iniciado")
    
    def _registrar(self, tipo: str, mensaje: str):
        """Registrar evento en log"""
        registro = {
            "timestamp": datetime.now().isoformat(),
            "tipo": tipo,
            "mensaje": mensaje,
            "estado": self.estado.name,
            "contador": self.contador
        }
        self.historial.append(registro)
        print(f"[LOG] {registro['timestamp']} - {mensaje}")
    
    def procesar_evento(self, evento: Evento) -> str:
        """Procesar evento con logging"""
        
        transiciones = {
            (Estado.BLOQUEADO, Evento.MONEDA): 
                (Estado.DESBLOQUEADO, "MONEDA_BLOQUEADO"),
            
            (Estado.BLOQUEADO, Evento.EMPUJAR):
                (Estado.BLOQUEADO, "EMPUJAR_BLOQUEADO"),
            
            (Estado.DESBLOQUEADO, Evento.EMPUJAR):
                (Estado.BLOQUEADO, "EMPUJAR_DESBLOQUEADO"),
            
            (Estado.DESBLOQUEADO, Evento.MONEDA):
                (Estado.DESBLOQUEADO, "MONEDA_DESBLOQUEADO"),
        }
        
        clave = (self.estado, evento)
        
        if clave not in transiciones:
            self._registrar("ERROR", f"Evento inválido: {evento.name}")
            return "❌ Evento inválido"
        
        nuevo_estado, tipo_transicion = transiciones[clave]
        
        # Registrar transición
        self._registrar(
            "TRANSICION",
            f"{self.estado.name} + {evento.name} → {nuevo_estado.name}"
        )
        
        # Ejecutar acción
        if evento == Evento.EMPUJAR and self.estado == Estado.DESBLOQUEADO:
            self.contador += 1
            self._registrar("PASO", f"Persona #{self.contador} pasó")
        
        # Cambiar estado
        self.estado = nuevo_estado
        
        return f"✓ {tipo_transicion}"
    
    def guardar_log(self):
        """Guardar historial en archivo JSON"""
        with open(self.archivo_log, 'w') as f:
            json.dump(self.historial, f, indent=2)
        print(f"✓ Log guardado en {self.archivo_log}")
    
    def mostrar_estadisticas(self):
        """Mostrar estadísticas finales"""
        print("\n" + "="*50)
        print("ESTADÍSTICAS FINAL")
        print("="*50)
        print(f"Total de personas: {self.contador}")
        print(f"Total de transiciones: {len(self.historial)}")
        print(f"Estado final: {self.estado.name}")
        
        # Contar eventos
        eventos_conteo = {}
        for reg in self.historial:
            tipo = reg['tipo']
            eventos_conteo[tipo] = eventos_conteo.get(tipo, 0) + 1
        
        print("\nEventos registrados:")
        for tipo, conteo in eventos_conteo.items():
            print(f"  {tipo}: {conteo}")

# Uso
if __name__ == "__main__":
    torniquete = TorniqueteConLog()
    
    # Simular uso
    eventos = [Evento.EMPUJAR, Evento.MONEDA, Evento.EMPUJAR, 
               Evento.MONEDA, Evento.EMPUJAR]
    
    for evento in eventos:
        torniquete.procesar_evento(evento)
        input("Presiona ENTER para siguiente evento...")
    
    torniquete.guardar_log()
    torniquete.mostrar_estadisticas()
```

---

## ⚙️ C++ - Versión Compilada

### Versión 1: Simple

```cpp
#include <iostream>
using namespace std;

enum Estado { BLOQUEADO = 0, DESBLOQUEADO = 1 };

class Torniquete {
private:
    Estado estado;
    int contador;

public:
    Torniquete() : estado(BLOQUEADO), contador(0) {}
    
    void insertar_moneda() {
        if (estado == BLOQUEADO) {
            estado = DESBLOQUEADO;
            cout << "✓ Desbloqueado\n";
        } else {
            cout << "ℹ️  Ya está desbloqueado\n";
        }
    }
    
    void empujar() {
        if (estado == DESBLOQUEADO) {
            contador++;
            estado = BLOQUEADO;
            cout << "✓ Paso " << contador << " registrado\n";
        } else {
            cout << "✗ Denegar\n";
        }
    }
    
    void mostrar_estado() {
        cout << "Estado: " << (estado == BLOQUEADO ? "Bloqueado" : "Desbloqueado") 
             << " | Contador: " << contador << endl;
    }
    
    void run() {
        int opcion;
        while (true) {
            cout << "\n==========================\n";
            mostrar_estado();
            cout << "==========================\n";
            cout << "1 = Insertar moneda\n";
            cout << "2 = Empujar\n";
            cout << "0 = Salir\n";
            cout << "Selecciona: ";
            cin >> opcion;
            
            switch (opcion) {
                case 1:
                    insertar_moneda();
                    break;
                case 2:
                    empujar();
                    break;
                case 0:
                    cout << "Total: " << contador << endl;
                    return;
                default:
                    cout << "❌ Opción inválida\n";
            }
        }
    }
};

int main() {
    Torniquete torniquete;
    torniquete.run();
    return 0;
}
```

### Versión 2: Con Máquina de Estados Explícita

```cpp
#include <iostream>
#include <map>
#include <string>
using namespace std;

enum Estado { BLOQUEADO = 0, DESBLOQUEADO = 1 };
enum Evento { MONEDA = 1, EMPUJAR = 2 };

class TorniqueteAvanzado {
private:
    Estado estado;
    int contador;
    
    // Tabla de transiciones
    map<pair<Estado, Evento>, pair<Estado, string>> transiciones;
    
    void inicializar_transiciones() {
        transiciones[{BLOQUEADO, MONEDA}] = 
            {DESBLOQUEADO, "✓ Desbloqueado"};
        transiciones[{BLOQUEADO, EMPUJAR}] = 
            {BLOQUEADO, "✗ Denegar"};
        transiciones[{DESBLOQUEADO, EMPUJAR}] = 
            {BLOQUEADO, "✓ Paso registrado"};
        transiciones[{DESBLOQUEADO, MONEDA}] = 
            {DESBLOQUEADO, "ℹ️  Ya desbloqueado"};
    }

public:
    TorniqueteAvanzado() : estado(BLOQUEADO), contador(0) {
        inicializar_transiciones();
    }
    
    string procesar_evento(Evento evento) {
        auto clave = make_pair(estado, evento);
        
        if (transiciones.find(clave) == transiciones.end()) {
            return "❌ Evento inválido";
        }
        
        auto [nuevo_estado, mensaje] = transiciones[clave];
        
        // Acción: incrementar contador si pasa
        if (evento == EMPUJAR && estado == DESBLOQUEADO) {
            contador++;
            estado = nuevo_estado;
            return "✓ Paso " + to_string(contador) + " registrado";
        }
        
        estado = nuevo_estado;
        return mensaje;
    }
    
    void mostrar_estado() const {
        cout << "Estado: " 
             << (estado == BLOQUEADO ? "Bloqueado" : "Desbloqueado")
             << " | Contador: " << contador << endl;
    }
    
    int obtener_contador() const {
        return contador;
    }
    
    void run() {
        int opcion;
        while (true) {
            cout << "\n==========================\n";
            mostrar_estado();
            cout << "==========================\n";
            cout << "1 = Insertar moneda\n";
            cout << "2 = Empujar\n";
            cout << "0 = Salir\n";
            cout << "Selecciona: ";
            cin >> opcion;
            
            if (opcion == 1) {
                cout << procesar_evento(MONEDA) << endl;
            } else if (opcion == 2) {
                cout << procesar_evento(EMPUJAR) << endl;
            } else if (opcion == 0) {
                cout << "Total personas: " << contador << endl;
                return;
            } else {
                cout << "❌ Opción inválida\n";
            }
        }
    }
};

int main() {
    TorniqueteAvanzado torniquete;
    torniquete.run();
    return 0;
}
```

---

## 📊 Comparación de Enfoques

| Aspecto | PSeInt | Python | C++ |
|---------|--------|--------|-----|
| **Sintaxis** | Mientras/Según | while/if/dict | while/switch/map |
| **OOP** | No | Sí (Clases) | Sí (Clases) |
| **Type Safety** | Débil | Débil | Fuerte (enums) |
| **Rendimiento** | N/A | Interpretado | Compilado |
| **Debugging** | Simple | Fácil | Requiere debugger |
| **Para aprender** | ✅ Excelente | ✅ Muy bien | ⚠️ Más complejo |
| **Para producción** | ❌ No | ⚠️ Sí | ✅ Excelente |

---

## 🎯 Lecciones Clave por Lenguaje

### PSeInt
- Máquina de estados es estructura básica: `Mientras` + `Según` anidado
- No tienes que pensar en tipos, solo en lógica
- Ideal para aprender el concepto

### Python
- Puedes usar clases para encapsular lógica
- Diccionarios hacen tablas de transiciones legibles
- Enum es más seguro que números mágicos
- Fácil agregar logging y auditoría

### C++
- Type safety: enums garantizan que solo valores válidos existen
- map para tablas de transiciones
- Compilación detecta errores antes de ejecutar
- Mejor para sistemas embebidos reales (Arduino, ESP32)

---

## ✨ Consejos Prácticos

1. **Siempre dibuja la tabla de transiciones primero**
2. **Usa enums/constantes, no números mágicos**
3. **En C++/Python, considera clases**
4. **Registra (logging) las transiciones para debugging**
5. **Prueba los casos límite** (ej. moneda en desbloqueado)
6. **Comienza en PSeInt, migra a Python, luego a C++**

---

**Última actualización**: 18/07/2026
