"""Точка входу лабораторної роботи №11, варіант 2."""

import asyncio

from lab import main as run


def main() -> None:
    """Запускає асинхронну демонстрацію."""
    asyncio.run(run())


if __name__ == "__main__":
    main()
