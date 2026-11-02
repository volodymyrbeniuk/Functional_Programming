# Лабораторна робота №12

**Варіант 2**

Тема: Властивісне тестування

## Встановлення залежностей

```bash
python -m pip install -r requirements.txt
```

## Запуск

Потрібен Python 3.12+. З кореня репозиторію запустіть:

```bash
python Lab_12/main.py
```

## Перевірки

```bash
python -m pytest Lab_12/tests -q
python -m black --check Lab_12
python -m ruff check Lab_12
python -m mypy Lab_12
```

Детальний звіт: [report.md](report.md).
