"""Composable parser combinators with source positions."""
from dataclasses import dataclass
from typing import Callable, Generic, TypeVar
T=TypeVar("T")
@dataclass(frozen=True)
class ParseError: position:int; message:str
@dataclass(frozen=True)
class Parsed(Generic[T]): value:T; position:int
Parser=Callable[[str,int],Parsed[T]|ParseError]
def literal(expected:str) -> Parser[str]:
    def parse(source:str,position:int):
        if source.startswith(expected,position): return Parsed(expected,position+len(expected))
        return ParseError(position,f"expected {expected!r}")
    return parse
def integer(source:str,position:int=0) -> Parsed[int]|ParseError:
    end=position
    if end<len(source) and source[end] in "+-": end+=1
    start_digits=end
    while end<len(source) and source[end].isdigit(): end+=1
    if end==start_digits: return ParseError(position,"expected integer")
    return Parsed(int(source[position:end]),end)
def map_parser(parser:Parser[T],function:Callable[[T,],object]) -> Parser[object]:
    def parse(source:str,position:int):
        result=parser(source,position)
        return result if isinstance(result,ParseError) else Parsed(function(result.value),result.position)
    return parse
def main() -> None: print(integer("-123x"))
if __name__=="__main__": main()
