# Pseudocódigo: flujo general de funcionamiento del sistema.

# Máquina de estados: estados, transiciones y condiciones de cambio.

## Estados

- INIT: Estado inicial del ECU
- SELF_TEST: Estado en donde revisa funcionalidad basica de componentes
- OPERATIONAL: Estado considerada operacion normal
- DEGRADED: Operación limitada
- SAFE_STATE: Mantener en condiciones seguras
- SHUT_DOWN: Estatus que realiza el el apagado para evitar daños en carro
- MAINTENANCE: Estado donde el ECU funciona como estatus normal. Simplemente muestra el mensaje que el mantenimiento es requerido

## Diagrama general de estados

INIT -> SELF_TEST

```mermaid
```

# Requerimientos funcionales: funciones que el sistema deberá cumplir.

## Sensores

- Flujo de Aire (m³/s)
- Presión de Aceite (PSI)
- Temperatura de Aceite (°C)
- Temperatura de Motor (°C)
- Humedad de Motor (%)
- RPM (revoluciones/minuto)
- Velocidad (km/h)
- Kilometraje (km)
- Temperatura Ambiente (°C)

## Funciones del sistema

El sistema debe:

- Iniciar en el estado `INIT`
- Monitorear que la velocidad no sobrepase los 170 km/h
- Cambiar al estado `DEGRADED` si la temperatura de aceite sobrepasa los 120 °C
- Monitorear que la temperatura ambiente esté en el rango operacional de -10 °C a 45 °C. Si está fuera de rango, cambiar a `DEGRADED`
- Monitorear el flujo de aire sea el adecuado (rango: 0 a 0.5 m³/s)
- Si las RPM están en condiciones normales pero el flujo de aire es insuficiente (< 0.1 m³/s), cambiar inmediatamente a `SAFE_STATE`
- Si la temperatura del motor sobrepasa los 120 °C, cambiar automáticamente a `SHUTDOWN`
- Si la presión de aceite sobrepasa los 50 PSI, cambiar a `SAFE_STATE`
- Después de 14,000 km recorridos, cambiar a `MAINTENANCE`
- Si la humedad del motor es superior al 40%, marcar estado `DEGRADED`
- Si la humedad del motor alcanza el 90% o superior, cambiar a `SHUTDOWN`

# Presentación del proyecto: explicación clara y coherente de la propuesta.