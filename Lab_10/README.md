# Лабораторна робота №10

**Варіант 2**

Тема: Функціональні конвеєри CSV/JSON

## Встановлення залежностей

```bash
python -m pip install -r requirements.txt
```

## Запуск

Потрібен Python 3.12+. З кореня репозиторію запустіть:

```bash
python Lab_10/main.py
```

## Перевірки

```bash
python -m pytest Lab_10/tests -q
python -m black --check Lab_10
python -m ruff check Lab_10
python -m mypy Lab_10
```

Детальний звіт: [report.md](report.md).
