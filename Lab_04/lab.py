"""Recursion, quicksort, order statistics, and memoization."""
from functools import lru_cache
from random import Random
from typing import Sequence, TypeVar
T=TypeVar("T")

def quicksort(values: Sequence[T]) -> list[T]:
    if len(values)<2: return list(values)
    pivot=values[len(values)//2]
    lower=[x for x in values if x<pivot]; equal=[x for x in values if x==pivot]; upper=[x for x in values if x>pivot]
    return quicksort(lower)+equal+quicksort(upper)

def randomized_select(values: Sequence[T], rank: int, seed: int=0) -> T:
    """Return 1-based rank without modifying input."""
    if not 1 <= rank <= len(values): raise ValueError("rank is outside the sequence")
    rng=Random(seed); work=list(values); target=rank-1; lo=0; hi=len(work)-1
    while lo<=hi:
        pivot=work[rng.randint(lo,hi)]; left=lo; right=hi; i=lo
        while i<=right:
            if work[i]<pivot: work[left],work[i]=work[i],work[left]; left+=1; i+=1
            elif work[i]>pivot: work[right],work[i]=work[i],work[right]; right-=1
            else: i+=1
        if target<left: hi=left-1
        elif target>right: lo=right+1
        else: return pivot
    raise RuntimeError("unreachable")

@lru_cache(maxsize=None)
def fibonacci(n: int) -> int:
    if n<0: raise ValueError("n must be non-negative")
    return n if n<2 else fibonacci(n-1)+fibonacci(n-2)

def main() -> None: print("Sorted:", quicksort([7,2,9,2,1])); print("F(30):", fibonacci(30))
if __name__=="__main__": main()
