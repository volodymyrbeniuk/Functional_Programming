"""Тести для перевірки чистоти функцій та правильності розрахунків."""

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
        {
            "id": 3,
            "name": "Дмитро",
            "hours": 170.0,
            "rate": 180.0,
            "bonus": 1500.0,
            "is_active": True,
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


def test_calculation_correctness() -> None:
    """Перевірка точності обчислень базової ставки, бонусу та податку."""
    base = calculate_base_pay(100.0, 150.0)
    assert base == 15000.0

    gross = default_bonus_policy(base, 1000.0)
    assert gross == 16000.0

    net = default_tax_policy(gross)
    assert net == round(16000.0 * 0.805, 2)
