# MenuCalificaciones - Notas de Actualización

## ✅ Mejoras implementadas

### 1. **Validación de cantidad > 0**
```pseint
Si cantidad <= 0 Entonces
    Escribir "ERROR: La cantidad debe ser mayor a 0. Intente de nuevo."
    cantidad <- 0
FinSi
```
- Ahora rechaza números ≤ 0
- Si falla, resetea `cantidad` a 0 para permitir reintentar

### 2. **Validación de calificaciones 0-10**
```pseint
Mientras No valido Hacer
    Escribir "Ingrese la calificacion de ", nombres[i], " (0-10): "
    Leer notaTemp
    Si notaTemp >= 0 Y notaTemp <= 10 Entonces
        calificaciones[i] <- notaTemp
        valido <- Verdadero
    SiNo
        Escribir "ERROR: La calificacion debe estar entre 0 y 10."
    FinSi
FinMientras
```
- Usa loop `Mientras` para reintentar si el valor es inválido
- Solo avanza cuando la calificación está entre 0 y 10

### 3. **Menú simplificado**
**Antes (5 opciones):**
1. Registrar alumnos
2. Registrar calificaciones
3. Mostrar todas las calificaciones
4. Calcular el promedio
5. Salir

**Ahora (4 opciones):**
1. Registrar calificaciones (nombres + notas)
2. Mostrar todas las calificaciones
3. Calcular el promedio
4. Salir

- Más intuitivo: todo en una opción
- Menor complejidad

### 4. **Control de entrada única**
```pseint
Si cantidad = 0 Entonces
    ...
    conteo <- cantidad
SiNo
    Escribir "AVISO: Las calificaciones ya fueron registradas."
FinSi
```
- No permite registrar calificaciones dos veces
- Variable `conteo` indica si ya se registraron datos
- Evita sobrescribir datos

### 5. **Mejor presentación**
- Encabezado de bienvenida
- Líneas en blanco para separar secciones
- Mensajes de error claros con "ERROR:"
- Estadísticas expandidas (suma total, promedio)
- Mensajes de confirmación

### 6. **Variables mejoradas**
- `conteo` — controla si ya se registraron calificaciones
- `valido` — flag para validación en loop

---

## 🧪 Casos de prueba

### Caso 1: Flujo normal
```
1. Registrar: 2 alumnos, notas 8.5 y 9
2. Mostrar: Muestra ambas
3. Promedio: 8.75
4. Salir
```

### Caso 2: Cantidad inválida
```
1. Registrar: Ingresa -5
   → Rechaza, reinicia
   → Ingresa 0
   → Rechaza, reinicia
   → Ingresa 1 ✓
```

### Caso 3: Calificación inválida
```
1. Registrar: Ingresa 11 para alumno 1
   → Rechaza, pide reintentar
   → Ingresa 10 ✓
```

### Caso 4: Intentar registrar dos veces
```
1. Registrar: 1 alumno ✓
1. Registrar (intento 2): Aviso "ya registradas"
```

---

## 🎯 Cumple con requisitos

✅ Registrar calificaciones  
✅ Mostrar todas las calificaciones  
✅ Calcular el promedio  
✅ Salir  
✅ Menú repetido hasta elegir salir  
✅ Usuario indica cantidad  
✅ Cantidad debe ser > 0  
✅ Calificaciones entre 0 y 10  
✅ Menú repite hasta elegir salir  

---

## 📝 Notas para estudiantes

- **Validación**: Importante para evitar datos inválidos
- **Loops**: `Mientras` para validación, `Repetir` para menú
- **Arrays**: Se usan índices 1-based (empiezan en 1, no en 0)
- **Variables booleanas**: `Falso`/`Verdadero` para control de flujo
