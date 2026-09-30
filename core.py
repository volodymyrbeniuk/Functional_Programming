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
    is_active: bool
    salary: float


BonusPolicy = Callable[[float], float]
TaxPolicy = Callable[[float], float]
FilterPolicy = Callable[[float], bool]
EmployeeFilterPolicy = Callable[[Employee], bool]
NowFn = Callable[[], float]


def calculate_base_pay(hours: float, rate: float) -> float:
    """Обчислює базову оплату за відпрацьовані години."""
    return round(hours * rate, 2)


def is_active_employee(emp: Employee) -> bool:
    """Чистий предикат для фільтрації активних працівників."""
    return bool(emp.get("is_active", False))


def with_salary(emp: Employee, salary: float) -> Employee:
    """Створює новий словник працівника з нарахованою сумою без мутацій."""
    new_emp: Employee = dict(emp)  # type: ignore[assignment]
    new_emp["salary"] = round(salary, 2)
    return new_emp


def default_bonus_policy(base_pay: float) -> float:
    """Стандартне нарахування бонусу (+10% від бази)."""
    return round(base_pay * 1.10, 2)


def default_tax_policy(gross_pay: float) -> float:
    """Стандартне утримання податку (19.5% ПДФО + військовий збір)."""
    return round(gross_pay * (1.0 - 0.195), 2)


def stamp_total(total: float, now: NowFn) -> tuple[float, float]:
    """Інжекція залежності генератора часу для збереження чистоти функції."""
    return total, now()


def calculate_payroll_pure(
    employees: Iterable[Employee],
    min_hours: float = 0.0,
    bonus_rate: float = 0.10,
    tax_rate: float = 0.195,
) -> dict[str, object]:
    """Чиста функція пакетного розрахунку зарплат (аналог process_orders_pure)."""
    active = [emp for emp in employees if emp.get("is_active", False)]
    qualified: list[Employee] = []
    total_payout = 0.0

    for emp in active:
        if emp.get("hours", 0.0) < min_hours:
            continue
        base = calculate_base_pay(emp.get("hours", 0.0), emp.get("rate", 0.0))
        gross = base * (1.0 + bonus_rate)
        net = round(gross * (1.0 - tax_rate), 2)

        qualified.append(with_salary(emp, net))
        total_payout += net

    return {
        "count": len(qualified),
        "total_payout": round(total_payout, 2),
        "employees": qualified,
    }


def make_payroll_processor(
    accept: FilterPolicy,
    apply_bonus: BonusPolicy,
    apply_tax: TaxPolicy,
) -> Callable[[list[Employee]], dict[str, object]]:
    """Фабрика функцій вищого порядку (структура за прикладом make_processor)."""

    def process(employees: list[Employee]) -> dict[str, object]:
        qualified: list[Employee] = []
        total_payout = 0.0

        for emp in employees:
            if not emp.get("is_active", False):
                continue
            base = calculate_base_pay(emp.get("hours", 0.0), emp.get("rate", 0.0))
            if not accept(base):
                continue
            net = apply_tax(apply_bonus(base))
            qualified.append(with_salary(emp, net))
            total_payout += net

        return {
            "count": len(qualified),
            "total_payout": round(total_payout, 2),
            "employees": qualified,
        }

    return process


def compose(f: Callable[[B], C], g: Callable[[A], B]) -> Callable[[A], C]:
    """Функціональна композиція двох функцій: f(g(x))."""
    return lambda x: f(g(x))


# Аліаси під назви з методички
order_subtotal = calculate_base_pay
with_total = with_salary
process_orders_pure = calculate_payroll_pure
make_processor = make_payroll_processor
