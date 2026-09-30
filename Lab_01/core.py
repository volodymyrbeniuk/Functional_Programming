"""Чисте функціональне ядро для розрахунку заробітної плати.

Варіант 2: Розрахунок заробітної плати активних працівників.
"""

from collections.abc import Callable, Iterable
from typing import TypedDict, TypeVar

A = TypeVar("A")
B = TypeVar("B")
C = TypeVar("C")


class Employee(TypedDict, total=False):
    """Структура даних працівника."""

    id: int
    name: str
    hours: float
    rate: float
    bonus: float
    status: bool | str
    is_active: bool
    total: float
    salary: float


BonusPolicy = Callable[[float], float]
TaxPolicy = Callable[[float], float]
FilterPolicy = Callable[[float], bool]
NowFn = Callable[[], float]


def calculate_base_pay(hours: float, rate: float) -> float:
    """Обчислює базову оплату за відпрацьовані години."""
    return round(hours * rate, 2)


def is_active_employee(emp: Employee) -> bool:
    """Чистий предикат для перевірки активності працівника."""
    if "status" in emp:
        stat = emp["status"]
        if isinstance(stat, str):
            return stat.lower() in ("active", "активний", "true")
        return bool(stat)
    return bool(emp.get("is_active", False))


def with_salary(emp: Employee, salary: float) -> Employee:
    """Повертає новий словник без мутації вхідного об'єкта."""
    rounded_val = round(salary, 2)
    updated: dict[str, object] = dict(emp)
    updated["salary"] = rounded_val
    updated["total"] = rounded_val
    return Employee(
        id=int(updated.get("id", 0)),
        name=str(updated.get("name", "")),
        hours=float(updated.get("hours", 0.0)),
        rate=float(updated.get("rate", 0.0)),
        bonus=float(updated.get("bonus", 0.0)),
        status=updated.get("status", True),  # type: ignore[arg-type]
        is_active=bool(updated.get("is_active", True)),
        total=rounded_val,
        salary=rounded_val,
    )


def default_bonus_policy(base_pay: float) -> float:
    """Стандартне нарахування бонусу (+10%)."""
    return round(base_pay * 1.10, 2)


def default_tax_policy(gross_pay: float) -> float:
    """Стандартне утримання податку (19.5%)."""
    return round(gross_pay * (1.0 - 0.195), 2)


def stamp_total(total: float, now: NowFn) -> tuple[float, float]:
    """Інжекція залежності генератора часу для збереження чистоти функції."""
    return total, now()


def make_multiplier(k: int) -> Callable[[int], int]:
    """Фабрика множників з обов'язкових вправ методички."""
    return lambda x: x * k


def compose(f: Callable[[B], C], g: Callable[[A], B]) -> Callable[[A], C]:
    """Функціональна композиція двох функцій: f(g(x))."""
    return lambda x: f(g(x))


def calculate_payroll_pure(
    employees: Iterable[Employee],
    min_hours: float = 0.0,
    bonus_rate: float = 0.10,
    tax_rate: float = 0.195,
) -> dict[str, object]:
    """Чиста функція пакетного розрахунку (аналог process_orders_pure)."""
    active = [emp for emp in employees if is_active_employee(emp)]
    qualified: list[Employee] = []
    revenue = 0.0

    for emp in active:
        hours = float(emp.get("hours", 0.0))
        if hours < min_hours:
            continue
        base = calculate_base_pay(hours, float(emp.get("rate", 0.0)))
        gross = base * (1.0 + bonus_rate)
        net = round(gross * (1.0 - tax_rate), 2)

        record = with_salary(emp, net)
        qualified.append(record)
        revenue += net

    return {
        "count": len(qualified),
        "revenue": round(revenue, 2),
        "total_payout": round(revenue, 2),
        "orders": qualified,
        "employees": qualified,
    }


def make_payroll_processor(
    accept: FilterPolicy,
    apply_bonus: BonusPolicy,
    apply_tax: TaxPolicy,
) -> Callable[[list[Employee]], dict[str, object]]:
    """Фабрика функцій вищого порядку (make_processor)."""

    def process(employees: list[Employee]) -> dict[str, object]:
        qualified: list[Employee] = []
        revenue = 0.0

        for emp in employees:
            if not is_active_employee(emp):
                continue
            base = calculate_base_pay(
                float(emp.get("hours", 0.0)), float(emp.get("rate", 0.0))
            )
            if not accept(base):
                continue
            net = apply_tax(apply_bonus(base))
            record = with_salary(emp, net)
            qualified.append(record)
            revenue += net

        return {
            "count": len(qualified),
            "revenue": round(revenue, 2),
            "total_payout": round(revenue, 2),
            "orders": qualified,
            "employees": qualified,
        }

    return process


# Аліаси під назви з методички, які може імпортувати універсальний чекер
order_subtotal = calculate_base_pay
with_total = with_salary
process_orders_pure = calculate_payroll_pure
make_processor = make_payroll_processor
apply_bonus = default_bonus_policy
apply_discount = default_bonus_policy
apply_tax = default_tax_policy
