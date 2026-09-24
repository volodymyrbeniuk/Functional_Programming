from decimal import Decimal

import pytest

from lab1.lab1 import apply_discount, calculate_total, transform_all


def test_discount_returns_expected_prices() -> None:
    prices = (Decimal("100.00"), Decimal("59.90"))

    assert apply_discount(prices, 10) == (Decimal("90.00"), Decimal("53.91"))


def test_discount_does_not_change_input() -> None:
    prices = [Decimal("100.00"), Decimal("59.90")]

    apply_discount(prices, 10)

    assert prices == [Decimal("100.00"), Decimal("59.90")]


@pytest.mark.parametrize("percent", [-1, 101])
def test_invalid_discount_raises_error(percent: int) -> None:
    with pytest.raises(ValueError):
        apply_discount((Decimal("10.00"),), percent)


def test_higher_order_function() -> None:
    assert transform_all((1, 2, 3), lambda number: number**2) == (1, 4, 9)


def test_total() -> None:
    assert calculate_total((Decimal("10.00"), Decimal("20.00"))) == Decimal("30.00")
