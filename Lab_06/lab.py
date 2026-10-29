"""Closures and parameterized decorators."""
from functools import wraps
from time import perf_counter, sleep
from typing import Callable, TypeVar, ParamSpec
P=ParamSpec("P"); R=TypeVar("R")

def make_multiplier(factor: int) -> Callable[[int],int]: return lambda value: value*factor

def timed(function: Callable[P,R]) -> Callable[P,R]:
    @wraps(function)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
        start=perf_counter(); result=function(*args,**kwargs); elapsed=perf_counter()-start
        print(f"{function.__name__}: {elapsed:.6f}s"); return result
    return wrapper

def retry(attempts: int, delay: float=0) -> Callable[[Callable[P,R]],Callable[P,R]]:
    if attempts<1 or delay<0: raise ValueError("attempts must be positive and delay non-negative")
    def decorate(function: Callable[P,R]) -> Callable[P,R]:
        @wraps(function)
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
            for attempt in range(attempts):
                try: return function(*args,**kwargs)
                except Exception:
                    if attempt==attempts-1: raise
                    if delay: sleep(delay)
            raise RuntimeError("unreachable")
        return wrapper
    return decorate

def main() -> None: print("Triple:",make_multiplier(3)(7))
if __name__=="__main__": main()
