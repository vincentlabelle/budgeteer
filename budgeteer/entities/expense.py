from typing import Any

from .money import Money


class Expense:
    """Representation of an expense.

    Parameters
    ----------
    money: Money
        monetary value of the expense

    Raises
    ------
    ValueError
        if money is strictly positive
    """

    def __init__(self, money: Money) -> None:
        self._money = money
        self._raise_if_money_is_strictly_positive()

    def _raise_if_money_is_strictly_positive(self) -> None:
        if self._money > Money(0):
            message = (
                f"cannot instantiate {self.__class__.__name__};"
                f"money must be negative"
            )
            raise ValueError(message)

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, self.__class__):
            return NotImplemented
        return self._money == other._money

    def __hash__(self) -> int:
        return hash(self._money)

    def __str__(self) -> str:
        return str(self._money)

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__}({self})>"
