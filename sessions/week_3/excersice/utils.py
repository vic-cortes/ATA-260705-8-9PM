import random
import time


def generate_random_sensor_data(quantity: int = 1) -> list[dict]:
    reading_list = []

    # Tiempo inicial (puedes usar el tiempo actual del sistema)
    current_time = time.time()

    for _ in range(quantity):
        # Simulación de valores en rangos automotrices lógicos
        sensor_data = {
            "speed_value": round(random.uniform(0.0, 180.0), 2),  # km/h
            "motor_temp_value": round(random.uniform(70.0, 105.0), 2),  # °C
            "air_flow_value": round(random.uniform(2.0, 40.0), 2),  # g/s
            "rpm_value": round(random.uniform(800.0, 6500.0), 2),  # RPM
            "oil_pressure_value": round(random.uniform(20.0, 60.0), 2),  # PSI
            "oil_temp_value": round(random.uniform(80.0, 110.0), 2),  # °C
            "time_stamp": round(current_time, 4),
        }

        reading_list.append(sensor_data)

        # Incrementa el tiempo en un intervalo (ej. 0.5 segundos por lectura)
        current_time += 0.5

    return reading_list
