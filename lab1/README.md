# Lab 1 Основи ФП у Python

Варіант: 2

## Мета

Ознайомитися з чистими функціями, референтною прозорістю, побічними ефектами та функціями вищого порядку в Python.

## Реалізація

- `lab1.py` містить чисті функції `apply_discount` і `calculate_total`;
- `transform_all` приймає функцію як аргумент через `typing.Callable`;
- `test_lab1.py` перевіряє результат, відсутність мутації та помилкові значення знижки.

## Запуск

```powershell
python lab1/lab1.py
```

## Тести, стиль і типи

```powershell
python -m pip install -r lab1/requirements-dev.txt
python -m pytest lab1 -q
python -m black --check lab1
python -m ruff check lab1
python -m mypy lab1
```
