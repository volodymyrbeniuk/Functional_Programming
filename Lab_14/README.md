# Лабораторна робота №14

**Варіант 2**

Тема: Підсумковий проєкт — DSL для аналізу логів

## Встановлення залежностей

```bash
python -m pip install -r requirements.txt
```

## Запуск

Потрібен Python 3.12+. З кореня репозиторію запустіть:

```bash
python Lab_14/main.py
```

## Перевірки

```bash
python -m pytest Lab_14/tests -q
python -m black --check Lab_14
python -m ruff check Lab_14
python -m mypy Lab_14
```

Детальний звіт: [report.md](report.md).
