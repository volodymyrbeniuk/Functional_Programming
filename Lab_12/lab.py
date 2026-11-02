"""Property-testable pure functions (Hypothesis is an optional dev dependency)."""
from collections.abc import Sequence
from typing import TypeVar
T=TypeVar("T")
def sort_values(values: Sequence[T]) -> list[T]: return sorted(values)
def is_sorted(values: Sequence[T]) -> bool: return all(a<=b for a,b in zip(values,values[1:]))
def stable_unique(values: Sequence[T]) -> list[T]:
    seen=set(); result=[]
    for value in values:
        if value not in seen: seen.add(value); result.append(value)
    return result
def parse_csv_ints(text: str) -> list[int]:
    if not text.strip(): return []
    try: return [int(part.strip()) for part in text.split(",")]
    except ValueError as exc: raise ValueError("expected comma-separated integers") from exc
def main() -> None: print(sort_values([3,1,2,1])); print(stable_unique([3,1,3,2]))
if __name__=="__main__": main()
