"""Higher-order functions and composition over immutable student records."""

from collections.abc import Callable, Iterable
from functools import reduce
from typing import Any, TypedDict, TypeVar

T = TypeVar("T")
U = TypeVar("U")


class StudentRecord(TypedDict):
    """A student row used by the transformation pipeline."""

    name: str
    score: int | float


UnaryFunction = Callable[[Any], Any]


def compose(*functions: UnaryFunction) -> UnaryFunction:
    """Compose functions right-to-left: compose(f, g)(x) == f(g(x))."""

    def composed(value: Any) -> Any:
        return reduce(
            lambda result, function: function(result), reversed(functions), value
        )

    return composed


def pipe(value: T, *functions: Callable[[Any], Any]) -> Any:
    """Apply functions left-to-right to a value."""
    return reduce(lambda result, function: function(result), functions, value)


def juxt(*functions: Callable[[T], Any]) -> Callable[[T], tuple[Any, ...]]:
    """Return a function that applies every function to the same input."""

    def apply_all(value: T) -> tuple[Any, ...]:
        return tuple(function(value) for function in functions)

    return apply_all


def transform(values: Iterable[T], function: Callable[[T], U]) -> list[U]:
    """Map a transformation over values and return a concrete list."""
    return list(map(function, values))


def select(values: Iterable[T], predicate: Callable[[T], bool]) -> list[T]:
    """Keep values that satisfy a predicate."""
    return list(filter(predicate, values))


def normalize_record(record: StudentRecord) -> StudentRecord:
    """Return a normalized copy without changing the input mapping."""
    return {**record, "name": record["name"].strip(), "score": float(record["score"])}


def average_score(records: Iterable[StudentRecord]) -> float:
    """Calculate the mean score; an empty collection has mean 0.0."""
    scores = map(lambda record: float(record["score"]), records)  # noqa: C417
    total, count = reduce(
        lambda state, score: (state[0] + score, state[1] + 1),
        scores,
        (0.0, 0),
    )
    return total / count if count else 0.0


def honor_roll(
    records: Iterable[StudentRecord], threshold: float = 90.0
) -> list[StudentRecord]:
    """Normalize records and return new rows meeting the score threshold."""
    if not 0 <= threshold <= 100:
        raise ValueError("threshold must be between 0 and 100")

    normalized = map(normalize_record, records)
    return list(filter(lambda record: record["score"] >= threshold, normalized))


def minimum(values: list[float]) -> float:
    """Return the smallest score."""
    return min(values)


def maximum(values: list[float]) -> float:
    """Return the largest score."""
    return max(values)


def total(values: list[float]) -> float:
    """Return the sum of scores."""
    return sum(values)


def main() -> None:
    students: list[StudentRecord] = [
        {"name": "Ada", "score": 96},
        {"name": "Grace", "score": 87},
        {"name": " Alan ", "score": 91},
    ]
    print("Honor roll:", honor_roll(students))
    print("Average:", average_score(students))
    scores = [float(record["score"]) for record in students]
    score_summary = juxt(minimum, maximum, total)(scores)
    print("Score summary (min, max, total):", score_summary)
    double_then_increment = compose(lambda value: value + 1, lambda value: value * 2)
    print("compose(f, g)(10):", double_then_increment(10))
    print("pipe(10, g, f):", pipe(10, lambda value: value * 2, lambda value: value + 1))


if __name__ == "__main__":
    main()
