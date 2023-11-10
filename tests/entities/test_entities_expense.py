import pytest

from budgeteer.entities.expense import Expense
from budgeteer.entities.money import Money


class TestExpenseInstantiation:
    @pytest.mark.parametrize("money", [Money(0), Money(-1)])
    def test_when_succeeds(self, money: Money) -> None:
        Expense(money)

    @pytest.mark.parametrize("money", [Money(1)])
    def test_when_fails(self, money: Money) -> None:
        with pytest.raises(ValueError):
            Expense(money)


@pytest.fixture(scope="module")
def money() -> Money:
    return Money(-1234)


@pytest.fixture(scope="module")
def expense(money: Money) -> Expense:
    return Expense(money)


class TestExpenseCast:
    def test_str(self, expense: Expense, money: Money) -> None:
        assert str(expense) == str(money)


class TestExpenseRepresentation:
    def test(self, expense: Expense) -> None:
        assert repr(expense) == f"<{expense.__class__.__name__}({expense})>"


class TestExpenseEqual:
    def test_when_equal(self, expense: Expense, money: Money) -> None:
        other = Expense(money)
        assert expense == other

    def test_when_different_value(self, expense: Expense, money: Money) -> None:
        other = Expense(money + Money(1))
        assert expense != other

    def test_when_different_type(self, expense: Expense) -> None:
        assert expense != "a"


class TestExpenseHash:
    def test_when_equal(self, expense: Expense, money: Money) -> None:
        other = Expense(money)
        assert hash(expense) == hash(other)

    def test_when_different_value(self, expense: Expense, money: Money) -> None:
        other = Expense(money + Money(1))
        assert hash(expense) != hash(other)
