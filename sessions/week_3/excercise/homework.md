# Pseudocódigo: flujo general de funcionamiento del sistema.

# Máquina de estados: estados, transiciones y condiciones de cambio.

## Diagram ageneral de estados

INIT -> SELF_TEST

```mermaid
```

# Requerimientos funcionales: funciones que el sistema deberá cumplir.

## Sensores

- Flujo de Aire
- Presion de Aceite
- Temperatura de Aeite
- Temperatura de motor
- Humedad
- RPM
- Velocidad
- Temperatura ambiente

## Funciones del sistema

El sistema debe:

- iniciar en el estado `INIT`
- monitorear que la velocidad no sobrepase los 170 km/hr
- cambiar al estado de `DEGRADED` en caso de de que la temperatura de aceite sobrepase los 120 C
- monitorear que la temperatura ambiente este en el rango operacional de -10 y 45. En caso de estar fuera del rango operacional cambiar al estado `DEGRADED`
- monitorear el flujo de aire que sea el adecuado para el motor entre 0 y 0.5 m3/s
- Si el las RPM estan en condiciones normales, pero no existe flujo de aire entonces inmediatamente cambiar `SAFE_STATE`
- Si la temperatura del motor sobrepasa los 500 Grados automaticamente cambiar a estado `SHUTDOWN`

# Presentación del proyecto: explicación clara y coherente de la propuesta.