"""Тести для чистого функціонального ядра розрахунку заробітної плати."""

from copy import deepcopy

from core import (
    Employee,
    calculate_base_pay,
    default_bonus_policy,
    default_tax_policy,
    is_active_employee,
    make_payroll_processor,
)


def sample_employees() -> list[Employee]:
    """Фікстура тестових даних."""
    return [
        {
            "id": 1,
            "name": "Олександр",
            "hours": 160.0,
            "rate": 200.0,
            "bonus": 2000.0,
            "is_active": True,
        },
        {
            "id": 2,
            "name": "Ірина",
            "hours": 80.0,
            "rate": 250.0,
            "bonus": 0.0,
            "is_active": False,
        },
    ]


def test_referential_transparency() -> None:
    """Перевірка референтної прозорості: однаковий вхід дає однаковий вихід."""
    processor = make_payroll_processor(
        is_active_employee, default_bonus_policy, default_tax_policy
    )
    emps = sample_employees()

    res1 = processor(emps)
    res2 = processor(emps)

    assert res1 == res2


def test_no_mutation() -> None:
    """Перевірка відсутності мутації вхідних даних."""
    emps = sample_employees()
    original = deepcopy(emps)

    processor = make_payroll_processor(
        is_active_employee, default_bonus_policy, default_tax_policy
    )
    processor(emps)

    assert emps == original


def test_empty_input() -> None:
    """Перевірка обробки порожнього списку працівників."""
    processor = make_payroll_processor(
        is_active_employee, default_bonus_policy, default_tax_policy
    )
    res = processor([])
    assert res["count"] == 0
    assert res["total_payout"] == 0.0
    assert res["employees"] == []


def test_calculation_correctness() -> None:
    """Перевірка базових обчислень."""
    assert calculate_base_pay(10.0, 100.0) == 1000.0
    assert default_bonus_policy(1000.0, 200.0) == 1200.0
    assert default_tax_policy(1000.0) == 805.0
