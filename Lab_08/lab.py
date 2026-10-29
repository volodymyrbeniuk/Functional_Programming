"""A tiny expression algebra evaluated with structural pattern matching."""
from dataclasses import dataclass
from typing import TypeAlias
@dataclass(frozen=True)
class Num: value: int
@dataclass(frozen=True)
class Add: left: "Expr"; right: "Expr"
@dataclass(frozen=True)
class Mul: left: "Expr"; right: "Expr"
Expr: TypeAlias=Num|Add|Mul

def evaluate(expr: Expr) -> int:
    match expr:
        case Num(value): return value
        case Add(left,right): return evaluate(left)+evaluate(right)
        case Mul(left,right): return evaluate(left)*evaluate(right)
        case _: raise TypeError(f"unsupported expression: {expr!r}")

def main() -> None: print(evaluate(Mul(Add(Num(2),Num(3)),Num(4))))
if __name__=="__main__": main()
