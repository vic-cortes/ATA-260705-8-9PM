# Tarea

Realice un Pseudocódigo que para emular la máquina de estados de un torniquete. El cual puede tener los estados Bloqueado y Desbloqueado y los eventos que los disparan son Insertar Moneda y Empujar. 

Anexo una tabla en imagen (para ejemplificar el flujo). 

Anexo tambien el código que se hizo para la máquina de estados de la lampara, como apoyo. 

Deben adjuntar su pseudocodigo, saludos!


| Estado actual | Evento | Siguiente estado | Acción |
| :--- | :--- | :--- | :--- |
| Bloqueado | Moneda | Desbloqueado | Permitir paso |
| Bloqueado | Empujar | Bloqueado | Denegar paso |
| Desbloqueado | Empujar | Bloqueado | Registrar paso |
| Desbloqueado | Moneda | Desbloqueado | Mantener desbloqueado |
