"""Чисте функціональне ядро для розрахунку заробітної плати.

Варіант 2: Розрахунок заробітної плати активних працівників.
"""

from collections.abc import Callable, Iterable
from typing import TypeVar, TypedDict

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


BonusPolicy = Callable[[float, float], float]
TaxPolicy = Callable[[float], float]
FilterPolicy = Callable[[Employee], bool]


def calculate_base_pay(hours: float, rate: float) -> float:
    """Обчислює базову оплату за відпрацьовані години."""
    return round(hours * rate, 2)


def is_active_employee(emp: Employee) -> bool:
    """Чистий предикат для фільтрації активних працівників."""
    return bool(emp.get("is_active", False))


def with_salary(emp: Employee, salary: float) -> Employee:
    """Створює новий запис працівника з обчисленою зарплатою без мутації оригіналу."""
    new_emp: Employee = dict(emp)  # type: ignore[assignment]
    new_emp["salary"] = round(salary, 2)
    return new_emp


def default_bonus_policy(base_pay: float, bonus: float) -> float:
    """Стандартне нарахування бонусу до базової оплати."""
    return round(base_pay + bonus, 2)


def default_tax_policy(gross_pay: float) -> float:
    """Стандартне утримання податку (19.5% ПДФО + військовий збір)."""
    return round(gross_pay * (1.0 - 0.195), 2)


def make_payroll_processor(
    filter_fn: FilterPolicy,
    bonus_fn: BonusPolicy,
    tax_fn: TaxPolicy,
) -> Callable[[Iterable[Employee]], dict[str, object]]:
    """Фабрика функцій вищого порядку для обробки відомості зарплат."""

    def process(employees: Iterable[Employee]) -> dict[str, object]:
        active_emps = [emp for emp in employees if filter_fn(emp)]
        processed_emps: list[Employee] = []
        total_payout = 0.0

        for emp in active_emps:
            base_pay = calculate_base_pay(emp["hours"], emp["rate"])
            gross_pay = bonus_fn(base_pay, emp.get("bonus", 0.0))
            net_pay = tax_fn(gross_pay)

            updated = with_salary(emp, net_pay)
            processed_emps.append(updated)
            total_payout += net_pay

        return {
            "count": len(processed_emps),
            "total_payout": round(total_payout, 2),
            "employees": processed_emps,
        }

    return process


def compose(f: Callable[[B], C], g: Callable[[A], B]) -> Callable[[A], C]:
    """Функціональна композиція двох функцій: f(g(x))."""
    return lambda x: f(g(x))


apply_bonus = default_bonus_policy
apply_tax = default_tax_policy
calculate_salary = calculate_base_pay
