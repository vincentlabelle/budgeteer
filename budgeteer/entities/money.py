from decimal import Decimal
from typing import Any, Tuple


class Money:
    """Representation of a monetary value.

    Parameters
    ----------
    cents: int
        monetary value in cents
    """

    _EXPONENT = -2

    def __init__(self, cents: int) -> None:
        self._value = self._convert(cents)

    def _convert(self, cents: int) -> Decimal:
        return Decimal(
            (
                self._get_sign(cents),
                self._get_digits(cents),
                self._EXPONENT,
            )
        )

    def _get_sign(self, cents: int) -> int:
        return 1 if cents < 0 else 0

    def _get_digits(self, cents: int) -> Tuple[int, ...]:
        return tuple(int(d) for d in str(abs(cents)))

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, self.__class__):
            return NotImplemented
        return self._value == other._value

    def __lt__(self, other: Any) -> bool:
        if not isinstance(other, self.__class__):
            return NotImplemented
        return self._value < other._value

    def __le__(self, other: Any) -> bool:
        if not isinstance(other, self.__class__):
            return NotImplemented
        return self._value <= other._value

    def __gt__(self, other: Any) -> bool:
        if not isinstance(other, self.__class__):
            return NotImplemented
        return self._value > other._value

    def __ge__(self, other: Any) -> bool:
        if not isinstance(other, self.__class__):
            return NotImplemented
        return self._value >= other._value

    def __hash__(self) -> int:
        return hash(self._value)

    def __str__(self) -> str:
        return str(self._value)

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__}({self})>"
