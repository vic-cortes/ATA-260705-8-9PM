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
    speed: SpeedVariable = SpeedVariable()
    motor_temperature: TemperatureVariable = TemperatureVariable()
    air_flow: AirFlowVariable = AirFlowVariable()
    rpm: RpmVariable = RpmVariable()
    oil_pressure: OilPressureVariable = OilPressureVariable()
    oil_temperature: OilTemperatureVariable = OilTemperatureVariable()


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

    pass


@dataclass
class EcuControl:
    pass
