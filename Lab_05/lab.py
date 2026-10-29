"""Lazy sequences and sliding windows."""
from itertools import accumulate, islice
from collections.abc import Iterable, Iterator
from typing import TypeVar
T=TypeVar("T")

def fibonacci_stream() -> Iterator[int]:
    a,b=0,1
    while True: yield a; a,b=b,a+b

def take(count: int, values: Iterable[T]) -> list[T]:
    if count<0: raise ValueError("count must be non-negative")
    return list(islice(values,count))

def drop(count: int, values: Iterable[T]) -> Iterator[T]:
    if count<0: raise ValueError("count must be non-negative")
    return islice(values,count,None)

def sliding_windows(values: Iterable[T], width: int) -> Iterator[tuple[T,...]]:
    if width<=0: raise ValueError("width must be positive")
    window=[]
    for item in values:
        window.append(item)
        if len(window)==width: yield tuple(window); window.pop(0)

def running_totals(values: Iterable[int]) -> Iterator[int]: return accumulate(values)

def main() -> None:
    print("First 10 Fibonacci values:", take(10,fibonacci_stream()))
    print("Windows:", list(sliding_windows([1,2,3,4],3)))
if __name__=="__main__": main()
