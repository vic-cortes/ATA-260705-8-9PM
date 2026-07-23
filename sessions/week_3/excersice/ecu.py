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

from .utils import generate_random_sensor_data

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


@dataclass
class EcuGatewayMiddleware:
    """
    Middleware for handling ECU gateway functionality.
    This is in charge of validating and routing messages between
    the ECU and other components of the system.
    """

    state: State
    car_sensors: CarSensors

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
            self.car_sensors.speed,
            self.car_sensors.motor_temperature,
            self.car_sensors.air_flow,
            self.car_sensors.rpm,
            self.car_sensors.oil_pressure,
            self.car_sensors.oil_temperature,
        ]

        # Run validation for each sensor variable
        for variable in VALID_SENSOR_VARIABLES:
            variable.validate_type()

    def process(self):
        if self.is_init_state:
            self.set_self_state()

        self.validate_sensors_data()


@dataclass
class EcuControl:
    state: State
    car_sensors: CarSensors


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
    last_ecu_state = ecu_gateway.state

    ecu_control = EcuControl(state=last_ecu_state, car_sensors=car_sensors)

    return ecu_control.state


def main():
    ecu_current_state = State.INIT

    while True:
        ecu_current_data = read_car_sensors(state=ecu_current_state)
        ecu_current_state = ecu_process(
            state=ecu_current_state, car_sensors=ecu_current_data
        )

        time.sleep(0.1)


if __name__ == "__main__":
    main()
