from collections.abc import Callable, Sequence
from typing import TypeVar

T = TypeVar("T")
R = TypeVar("R")


def apply_discount(prices: Sequence[float], percent: int) -> list[float]:
    """Повертає новий список цін зі знижкою."""
    if percent < 0 or percent > 100:
        raise ValueError("Знижка має бути від 0 до 100")

    discounted: list[float] = []
    for price in prices:
        new_price = price * (1 - percent / 100)
        discounted.append(round(new_price, 2))

    return discounted


def transform_all(values: Sequence[T], func: Callable[[T], R]) -> list[R]:
    """Застосовує передану функцію до кожного елемента."""
    result: list[R] = []
    for v in values:
        result.append(func(v))
    return result


def calculate_total(prices: Sequence[float]) -> float:
    """Рахує загальну суму цін."""
    return float(sum(prices))


def main() -> None:
    prices: list[float] = [100.00, 59.90, 40.00]

    discounted_prices = apply_discount(prices, 15)

    print("Ціни зі знижкою:", discounted_prices)
    print("Загальна сума:", calculate_total(discounted_prices))

    print("Квадрати чисел:", transform_all([1, 2, 3], lambda x: x ** 2))


if __name__ == "__main__":
    main()
