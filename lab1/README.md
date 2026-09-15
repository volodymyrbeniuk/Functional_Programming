# Lab 1 — Основи функціонального програмування

Лабораторна робота з курсу «Функціональне програмування на Python».

## Що реалізовано

- чисту функцію `apply_discount`, яка не змінює вхідні ціни;
- функцію вищого порядку `transform_all` з `typing.Callable`;
- чисту функцію `calculate_total`;
- тести `pytest` для коректності та перевірки відсутності мутації.

## Запуск програми

```powershell
python lab1.py
```

## Запуск тестів

```powershell
python -m pip install -r requirements.txt
python -m pytest -q
```
