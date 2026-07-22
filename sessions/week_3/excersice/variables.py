from abc import ABC
from dataclasses import dataclass


class Variable(ABC):
    """
    Base class for representing a variable in the ECU system.
    """

    def __init__(self, name: str, value: float, unit: str) -> None:
        self.name = name
        self.value = value
        self.unit = unit

    def validate_type(self):
        """
        Validates the type of the variable's value.
        """
        try:
            self._validate_type()
            return True
        except Exception as e:
            print(f"Validation error for {self.name}: {e}")
            return False

    def validate(self) -> bool:
        """
        Abstract method to validate the variable's value.
        Should be implemented by subclasses.
        """
        try:
            self._validate()
            return True
        except Exception as e:
            print(f"Validation error for {self.name}: {e}")
            return False


@dataclass
class SpeedVariable(Variable):
    name: str = "Speed"
    value: float = 0.0
    unit: str = "km/h"

    def _validate_type(self):
        """
        Validates the type of the speed value.
        """
        if not isinstance(self.value, (int, float)):
            raise TypeError(
                f"Speed value must be a number, got {type(self.value).__name__}."
            )

    def _validate_range(self):
        """
        Validates the range of the speed value.
        """
        MAX_SPEED = 300.0  # km/h

        if not (0 <= self.value <= MAX_SPEED):
            raise ValueError(
                f"Speed value {self.value} is out of range (0-{MAX_SPEED} km/h)."
            )

    def _validate(self) -> None:
        self._validate_range()


@dataclass
class TemperatureVariable(Variable):
    name: str = "Temperature"
    value: float = 0.0
    unit: str = "°C"

    def _validate_type(self):
        """
        Validates the type of the temperature value.
        """
        if not isinstance(self.value, float):
            raise TypeError(
                f"Temperature value must be a float, got {type(self.value).__name__}."
            )

    def _validate_range(self):
        """
        Validates the range of the temperature value.
        """
        MIN_TEMP = -40.0  # °C
        MAX_TEMP = 150.0  # °C

        if not (MIN_TEMP <= self.value <= MAX_TEMP):
            raise ValueError(
                f"Temperature value {self.value} is out of range ({MIN_TEMP}-{MAX_TEMP} °C)."
            )

    def _validate(self) -> None:
        self._validate_range()


class AirFlowVariable(Variable):
    name: str = "Air Flow"
    value: float = 0.0
    unit: str = "m³/s"

    def _validate_type(self):
        """
        Validates the type of the air flow value.
        """
        if not isinstance(self.value, float):
            raise TypeError(
                f"Air flow value must be a float, got {type(self.value).__name__}."
            )

    def _validate_range(self):
        """
        Validates the range of the air flow value.
        """
        MIN_FLOW = 0.0  # m³/s
        MAX_FLOW = 100.0  # m³/s

        if not (MIN_FLOW <= self.value <= MAX_FLOW):
            raise ValueError(
                f"Air flow value {self.value} is out of range ({MIN_FLOW}-{MAX_FLOW} m³/s)."
            )

    def _validate(self) -> None:
        self._validate_range()


class RpmVariable(Variable):
    name: str = "RPM"
    value: float = 0.0
    unit: str = "rev/min"

    def _validate_type(self):
        """
        Validates the type of the RPM value.
        """
        if not isinstance(self.value, float):
            raise TypeError(
                f"RPM value must be a float, got {type(self.value).__name__}."
            )

    def _validate_range(self):
        """
        Validates the range of the RPM value.
        """
        MIN_RPM = 0.0  # rev/min
        MAX_RPM = 10000.0  # rev/min

        if not (MIN_RPM <= self.value <= MAX_RPM):
            raise ValueError(
                f"RPM value {self.value} is out of range ({MIN_RPM}-{MAX_RPM} rev/min)."
            )

    def _validate(self) -> None:
        self._validate_range()


class OilPressureVariable(Variable):
    name: str = "Oil Pressure"
    value: float = 0.0
    unit: str = "Pa"

    def _validate_type(self):
        """
        Validates the type of the oil pressure value.
        """
        if not isinstance(self.value, float):
            raise TypeError(
                f"Oil pressure value must be a float, got {type(self.value).__name__}."
            )

    def _validate_range(self):
        """
        Validates the range of the oil pressure value.
        """
        MIN_PRESSURE = 0.0  # Pa
        MAX_PRESSURE = 100000.0  # Pa

        if not (MIN_PRESSURE <= self.value <= MAX_PRESSURE):
            raise ValueError(
                f"Oil pressure value {self.value} is out of range ({MIN_PRESSURE}-{MAX_PRESSURE} Pa)."
            )

    def _validate(self) -> None:
        self._validate_range()


class OilTemperatureVariable(Variable):
    name: str = "Oil Temperature"
    value: float = 0.0
    unit: str = "°C"

    def _validate_type(self):
        """
        Validates the type of the oil temperature value.
        """
        if not isinstance(self.value, float):
            raise TypeError(
                f"Oil temperature value must be a float, got {type(self.value).__name__}."
            )

    def _validate_range(self):
        """
        Validates the range of the oil temperature value.
        """
        MIN_TEMP = -40.0  # °C
        MAX_TEMP = 150.0  # °C

        if not (MIN_TEMP <= self.value <= MAX_TEMP):
            raise ValueError(
                f"Oil temperature value {self.value} is out of range ({MIN_TEMP}-{MAX_TEMP} °C)."
            )

    def _validate(self) -> None:
        self._validate_range()
