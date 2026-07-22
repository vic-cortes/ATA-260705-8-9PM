from abc import ABC, abstractmethod
from dataclasses import dataclass


class Variable(ABC):
    """
    Base class for representing a variable in the ECU system.
    """

    def __init__(self, name: str, value: float, unit: str) -> None:
        self.name = name
        self.value = value
        self.unit = unit

    @abstractmethod
    def validate(self):
        """
        Abstract method to validate the variable's value.
        Should be implemented by subclasses.
        """
        pass


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

    def validate(self) -> bool:
        try:
            self._validate_type()
            self._validate_range()
            return True
        except (TypeError, ValueError) as e:
            print(f"Validation error for {self.name}: {e}")
            return False
