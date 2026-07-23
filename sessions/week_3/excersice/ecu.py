import random
import time
from dataclasses import dataclass
from enum import Enum, auto

from variables import (
    AirFlowVariable,
    OilPressureVariable,
    OilTemperatureVariable,
    RpmVariable,
    SpeedVariable,
    TemperatureVariable,
)

MIN_TIME_DIFFERENCE_BETWEEN_MESSAGES = 0.1  # seconds


class CarSensors:

    def __init__(
        self,
        speed_value: float = 0.0,
        motor_temp_value: float = 0.0,
        air_flow_value: float = 0.0,
        rpm_value: float = 0.0,
        oil_pressure_value: float = 0.0,
        oil_temp_value: float = 0.0,
    ) -> None:
        self.speed: SpeedVariable = SpeedVariable(value=speed_value)
        self.motor_temperature: TemperatureVariable = TemperatureVariable(
            value=motor_temp_value
        )
        self.air_flow: AirFlowVariable = AirFlowVariable(value=air_flow_value)
        self.rpm: RpmVariable = RpmVariable(value=rpm_value)
        self.oil_pressure: OilPressureVariable = OilPressureVariable(
            value=oil_pressure_value
        )
        self.oil_temperature: OilTemperatureVariable = OilTemperatureVariable(
            value=oil_temp_value
        )
        self.time_stamp: float = 0.0  # seconds since epoch


class State(Enum):
    INIT = auto()
    SELF_TEST = auto()
    SELF_STATE = auto()
    OPERATIONAL = auto()
    DEGRADED = auto()
    SHUTDOWN = auto()


class EcuGatewayMiddleware:
    """
    Middleware for handling ECU gateway functionality.
    This is in charge of validating and routing messages between
    the ECU and other components of the system.
    """

    def __init__(self, state: State, car_sensors: CarSensors) -> None:
        self.state: State = state
        self._car_sensors: CarSensors = car_sensors

    @property
    def is_init_state(self) -> bool:
        return self.state == State.INIT

    def set_self_state(self) -> None:
        self.state = State.SELF_TEST

    def validate_sensors_data(self):
        """
        Run the ECU gateway in the INIT state.
        This state is responsible for initializing the system and performing self-tests.
        """

        VALID_SENSOR_VARIABLES = [
            self._car_sensors.speed,
            self._car_sensors.motor_temperature,
            self._car_sensors.air_flow,
            self._car_sensors.rpm,
            self._car_sensors.oil_pressure,
            self._car_sensors.oil_temperature,
        ]

        # Run validation for each sensor variable
        for variable in VALID_SENSOR_VARIABLES:
            variable.validate_type()

        self.state = State.SELF_TEST

    def run(self):
        if self.is_init_state:
            self.set_self_state()

        self.validate_sensors_data()


@dataclass
class EcuControl:
    pass


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


def read_car_sensors(state: State) -> CarSensors:
    """
    Simulates reading data from sensors
    """
    if state == State.INIT:
        # Create initial values
        return CarSensors()

    # Create random sensor values for testing purposes
    random_values = generate_random_sensor_data()[0]
    return CarSensors(**random_values)


def ecu_process(state: State, car_sensors: CarSensors) -> State:
    """
    Main ECU process
    """

    ecu_gateway = EcuGatewayMiddleware(state=state, car_sensors=car_sensors)
    ecu_gateway.run()

    return ecu_gateway.state


def main():
    init_state = State.INIT

    while True:
        current_car_data = read_car_sensors()
        ecu_process(state=init_state, car_sensors=current_car_data)


if __name__ == "__main__":
    main()
