from dataclasses import dataclass
from enum import Enum, auto

MIN_TIME_DIFFERENCE_BETWEEN_MESSAGES = 0.1  # seconds


@dataclass
class Sensors:
    speed: float
    temperature: float
    air_flow: float
    rpm: float


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
