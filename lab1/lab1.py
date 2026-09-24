from collections.abc import Callable, Iterable
from decimal import Decimal
from typing import TypeVar


T = TypeVar("T")
R = TypeVar("R")


def apply_discount(prices: Iterable[Decimal], percent: int) -> tuple[Decimal, ...]:
    """Повертає нові ціни зі знижкою, не змінюючи вхідну колекцію."""
    if not 0 <= percent <= 100:
        raise ValueError("Знижка має бути від 0 до 100")

    multiplier = Decimal(100 - percent) / Decimal(100)
    return tuple((price * multiplier).quantize(Decimal("0.01")) for price in prices)


def transform_all(values: Iterable[T], function: Callable[[T], R]) -> tuple[R, ...]:
    """Функція вищого порядку, яка застосовує function до кожного значення."""
    return tuple(map(function, values))


def calculate_total(prices: Iterable[Decimal]) -> Decimal:
    """Обчислює суму цін без побічних ефектів."""
    return sum(prices, start=Decimal("0.00"))


def main() -> None:
    prices = (Decimal("100.00"), Decimal("59.90"), Decimal("40.00"))
    discounted_prices = apply_discount(prices, 15)

    print(discounted_prices)
    print(calculate_total(discounted_prices))
    print(transform_all((1, 2, 3), lambda number: number**2))


if __name__ == "__main__":
    main()
