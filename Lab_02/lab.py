"""Higher-order transformations over immutable student records."""
from functools import reduce
from typing import Callable, Iterable, TypeVar

T=TypeVar("T"); U=TypeVar("U")
Record=dict[str, object]

def compose(*functions: Callable[[object], object]) -> Callable[[object], object]:
    """Compose functions left-to-right (f, g)(x) == g(f(x))."""
    def composed(value: object) -> object:
        for function in functions: value=function(value)
        return value
    return composed

def transform(values: Iterable[T], function: Callable[[T], U]) -> list[U]:
    return list(map(function, values))

def select(values: Iterable[T], predicate: Callable[[T], bool]) -> list[T]:
    return list(filter(predicate, values))

def average_score(records: Iterable[Record]) -> float:
    scores=[float(record["score"]) for record in records]
    return reduce(lambda total, score: total+score, scores, 0.0)/len(scores) if scores else 0.0

def honor_roll(records: Iterable[Record], threshold: float=90) -> list[Record]:
    """Return new normalized records for students meeting the threshold."""
    pipeline=lambda row: {**row, "name": str(row["name"]).strip(), "score": float(row["score"])}
    normalized=map(pipeline, records)
    return list(filter(lambda row: row["score"] >= threshold, normalized))

def main() -> None:
    students=[{"name":"Ada", "score":96}, {"name":"Grace", "score":87}, {"name":" Alan ", "score":91}]
    print("Honor roll:", honor_roll(students))
    print("Average:", average_score(students))
if __name__=="__main__": main()
