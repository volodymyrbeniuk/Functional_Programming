"""Domain errors represented as Result values."""
from dataclasses import dataclass
from typing import Callable, Generic, TypeVar
T=TypeVar("T"); U=TypeVar("U")
@dataclass(frozen=True)
class Ok(Generic[T]): value:T
@dataclass(frozen=True)
class Err: error:str
Result=Ok[T]|Err

def map_result(result: Result[T], function: Callable[[T],U]) -> Result[U]:
    return Ok(function(result.value)) if isinstance(result,Ok) else result

def flat_map(result: Result[T], function: Callable[[T],Result[U]]) -> Result[U]:
    return function(result.value) if isinstance(result,Ok) else result

def parse_int(text: str) -> Result[int]:
    try: return Ok(int(text))
    except ValueError: return Err(f"not an integer: {text!r}")

def positive(value: int) -> Result[int]: return Ok(value) if value>0 else Err("value must be positive")
def parse_positive(text: str) -> Result[int]: return flat_map(parse_int(text),positive)

def main() -> None: print(parse_positive("42")); print(parse_positive("bad"))
if __name__=="__main__": main()
