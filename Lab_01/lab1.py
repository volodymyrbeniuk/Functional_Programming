"""ЛР №1: основи функціонального програмування в Python."""

from collections.abc import Callable, Iterable
from decimal import Decimal
from typing import TypeVar


T = TypeVar("T")
R = TypeVar("R")


def apply_discount(prices: Iterable[Decimal], percent: int) -> tuple[Decimal, ...]:
    """Чиста функція: повертає нові ціни, не змінюючи вхідні."""
    if not 0 <= percent <= 100:
        raise ValueError("Знижка має бути від 0 до 100")

    multiplier = Decimal(100 - percent) / Decimal(100)
    return tuple((price * multiplier).quantize(Decimal("0.01")) for price in prices)


def transform_all(values: Iterable[T], function: Callable[[T], R]) -> tuple[R, ...]:
    """Функція вищого порядку: приймає функцію як аргумент."""
    return tuple(map(function, values))


def calculate_total(prices: Iterable[Decimal]) -> Decimal:
    """Чиста функція для обчислення загальної вартості."""
    return sum(prices, start=Decimal("0.00"))


def main() -> None:
    prices = (Decimal("100.00"), Decimal("59.90"), Decimal("40.00"))
    discounted_prices = apply_discount(prices, 15)

    print("Початкові ціни:", prices)
    print("Ціни зі знижкою:", discounted_prices)
    print("Сума зі знижкою:", calculate_total(discounted_prices))
    print("Квадрати чисел:", transform_all((1, 2, 3), lambda number: number**2))

    # Мінімальні перевірки: вхідні дані не змінилися, результат очікуваний.
    assert prices == (Decimal("100.00"), Decimal("59.90"), Decimal("40.00"))
    assert discounted_prices == (Decimal("85.00"), Decimal("50.92"), Decimal("34.00"))


if __name__ == "__main__":
    main()
