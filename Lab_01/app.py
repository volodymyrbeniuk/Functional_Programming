"""Оболонка введення/виведення (I/O)."""

from core import (
    Employee,
    default_bonus_policy,
    default_tax_policy,
    make_payroll_processor,
)


def render_report(result: dict[str, object]) -> None:
    """Виведення звіту без домішування до чистих обчислень."""
    print("=== Відомість нарахування заробітної плати ===")
    print(f"Оброблено працівників: {result['count']}")
    print(f"Загальний фонд виплат: {result['total_payout']} грн\n")

    employees = result.get("employees", [])
    if isinstance(employees, list):
        for emp in employees:
            print(f"ID {emp['id']}: {emp['name']} -> До виплати: {emp['salary']} грн")


def main() -> None:
    """Точка входу програми."""
    employees: list[Employee] = [
        {"id": 1, "name": "Володимир", "hours": 160.0, "rate": 300.0, "is_active": True},
        {"id": 2, "name": "Тарас", "hours": 120.0, "rate": 200.0, "is_active": False},
        {"id": 3, "name": "Оксана", "hours": 150.0, "rate": 280.0, "is_active": True},
    ]

    payroll_processor = make_payroll_processor(
        accept=lambda base: base >= 20000.0,
        apply_bonus=default_bonus_policy,
        apply_tax=default_tax_policy,
    )

    report_data = payroll_processor(employees)
    render_report(report_data)


if __name__ == "__main__":
    main()
