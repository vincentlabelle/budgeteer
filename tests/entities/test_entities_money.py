import pytest

from budgeteer.entities.money import Money


class TestMoneyCast:
    @pytest.mark.parametrize(
        "money, expected",
        [
            (Money(-1234), "-12.34"),
            (Money(-100), "-1.00"),
            (Money(-10), "-0.10"),
            (Money(-1), "-0.01"),
            (Money(0), "0.00"),
            (Money(1), "0.01"),
            (Money(10), "0.10"),
            (Money(100), "1.00"),
            (Money(1234), "12.34"),
        ],
    )
    def test_str(self, money: Money, expected: str) -> None:
        assert str(money) == expected


@pytest.fixture(scope="module")
def cents() -> int:
    return 100


@pytest.fixture(scope="module")
def money(cents: int) -> Money:
    return Money(cents)


class TestMoneyRepresentation:
    def test(self, money: Money) -> None:
        assert repr(money) == f"<{money.__class__.__name__}({money})>"


class TestMoneyEqual:
    def test_when_equal(self, money: Money, cents: int) -> None:
        other = Money(cents)
        assert money == other

    def test_when_different_value(self, money: Money, cents: int) -> None:
        other = Money(cents + 1)
        assert money != other

    def test_when_different_type(self, money: Money) -> None:
        assert money != "a"


class TestMoneyHash:
    def test_when_equal(self, money: Money, cents: int) -> None:
        other = Money(cents)
        assert hash(money) == hash(other)

    def test_when_unequal(self, money: Money, cents: int) -> None:
        other = Money(cents + 1)
        assert hash(money) != hash(other)


class TestMoneyInequalities:
    def test_lt_when_less_than(self, money: Money, cents: int) -> None:
        other = Money(cents + 1)
        assert money < other

    def test_lt_when_equal(self, money: Money, cents: int) -> None:
        other = Money(cents)
        assert not money < other

    def test_lt_when_greater_than(self, money: Money, cents: int) -> None:
        other = Money(cents - 1)
        assert not money < other

    def test_lt_when_different_type(self, money: Money) -> None:
        with pytest.raises(TypeError):
            money < "a"

    def test_le_when_less_than(self, money: Money, cents: int) -> None:
        other = Money(cents + 1)
        assert money <= other

    def test_le_when_equal(self, money: Money, cents: int) -> None:
        other = Money(cents)
        assert money <= other

    def test_le_when_greater_than(self, money: Money, cents: int) -> None:
        other = Money(cents - 1)
        assert not money <= other

    def test_le_when_different_type(self, money: Money) -> None:
        with pytest.raises(TypeError):
            money <= "a"

    def test_gt_when_less_than(self, money: Money, cents: int) -> None:
        other = Money(cents + 1)
        assert not money > other

    def test_gt_when_equal(self, money: Money, cents: int) -> None:
        other = Money(cents)
        assert not money > other

    def test_gt_when_greater_than(self, money: Money, cents: int) -> None:
        other = Money(cents - 1)
        assert money > other

    def test_gt_when_different_type(self, money: Money) -> None:
        with pytest.raises(TypeError):
            money > "a"

    def test_ge_when_less_than(self, money: Money, cents: int) -> None:
        other = Money(cents + 1)
        assert not money >= other

    def test_ge_when_equal(self, money: Money, cents: int) -> None:
        other = Money(cents)
        assert money >= other

    def test_ge_when_greater_than(self, money: Money, cents: int) -> None:
        other = Money(cents - 1)
        assert money >= other

    def test_ge_when_different_type(self, money: Money) -> None:
        with pytest.raises(TypeError):
            money >= "a"


class TestMoneyArithmetic:
    def test_add(self, money: Money, cents: int) -> None:
        other = Money(cents + 1)
        assert money + other == Money(2 * cents + 1)

    def test_add_when_different_type(self, money: Money) -> None:
        with pytest.raises(TypeError):
            money + "a"

    def test_sub(self, money: Money, cents: int) -> None:
        other = Money(cents + 1)
        assert money - other == Money(-1)

    def test_sub_when_different_type(self, money: Money) -> None:
        with pytest.raises(TypeError):
            money - "a"
