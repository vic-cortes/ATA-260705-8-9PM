from dataclasses import dataclass
from enum import Enum, auto

from variables import (
    AirFlowVariable,
    OilPressureVariable,
    OilTemperatureVariable,
    RpmVariable,
    SpeedVariable,
    TemperatureVariable,
    Variable,
)

MIN_TIME_DIFFERENCE_BETWEEN_MESSAGES = 0.1  # seconds


@dataclass
class CarSensors:
    speed: SpeedVariable = SpeedVariable()
    motor_temperature: TemperatureVariable = TemperatureVariable()
    air_flow: AirFlowVariable = AirFlowVariable()
    rpm: RpmVariable = RpmVariable()
    oil_pressure: OilPressureVariable = OilPressureVariable()
    oil_temperature: OilTemperatureVariable = OilTemperatureVariable()
    time_stamp: float = 0.0  # seconds since epoch


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

    def __init__(self):
        self.state: State = State.INIT

    @property
    def is_init_state(self) -> bool:
        return self.state == State.INIT

    def run_init_state(self):
        """
        Run the ECU gateway in the INIT state.
        This state is responsible for initializing the system and performing self-tests.
        """
        car_sensors: CarSensors = CarSensors()

        VALID_SENSOR_VARIABLES = [
            car_sensors.speed,
            car_sensors.motor_temperature,
            car_sensors.air_flow,
            car_sensors.rpm,
            car_sensors.oil_pressure,
            car_sensors.oil_temperature,
        ]

        # Run validation for each sensor variable
        for variable in VALID_SENSOR_VARIABLES:
            variable.validate_type()

        self.state = State.SELF_TEST

    def run(self):
        if self.is_init_state:
            self.run_init_state()


@dataclass
class EcuControl:
    pass
