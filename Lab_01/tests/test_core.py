"""Тести для чистого функціонального ядра розрахунку зарплати."""

from copy import deepcopy

from core import (
    Employee,
    calculate_payroll_pure,
    compose,
    default_bonus_policy,
    default_tax_policy,
    make_payroll_processor,
    stamp_total,
)


def sample_employees() -> list[Employee]:
    return [
        {"id": 1, "name": "Олександр", "hours": 160.0, "rate": 200.0, "is_active": True},
        {"id": 2, "name": "Ірина", "hours": 80.0, "rate": 250.0, "is_active": False},
        {"id": 3, "name": "Дмитро", "hours": 170.0, "rate": 180.0, "is_active": True},
    ]


def test_referential_transparency() -> None:
    emps = sample_employees()
    r1 = calculate_payroll_pure(emps, min_hours=100.0, bonus_rate=0.1, tax_rate=0.2)
    r2 = calculate_payroll_pure(emps, min_hours=100.0, bonus_rate=0.1, tax_rate=0.2)
    assert r1 == r2


def test_no_mutation() -> None:
    emps = sample_employees()
    original = deepcopy(emps)
    calculate_payroll_pure(emps, min_hours=0.0, bonus_rate=0.0, tax_rate=0.0)
    assert emps == original


def test_callable_policies() -> None:
    emps = sample_employees()
    accept = lambda s: s >= 30000.0
    apply_bonus = lambda s: s * 1.1
    apply_tax = lambda s: s * 0.8

    processor = make_payroll_processor(
        accept=accept,
        apply_bonus=apply_bonus,
        apply_tax=apply_tax,
    )
    result = processor(emps)
    assert result["count"] == 2
    assert result["total_payout"] > 0


def test_stamp_total() -> None:
    fixed_time = lambda: 1700000000.0
    total, timestamp = stamp_total(5000.0, fixed_time)
    assert total == 5000.0
    assert timestamp == 1700000000.0


def test_compose() -> None:
    f = lambda x: x * 2
    g = lambda x: x + 10
    h = compose(f, g)
    assert h(5) == 30
