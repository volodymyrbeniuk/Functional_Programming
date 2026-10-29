"""Useful functional tools from functools and operator."""
from functools import partial, reduce, singledispatch
from operator import add, itemgetter, mul
from typing import Any

def product(values: list[int]) -> int: return reduce(mul,values,1)
add_tax=partial(add, 5)
get_name=itemgetter("name")

@singledispatch
def describe(value: Any) -> str: return f"object: {value!r}"
@describe.register
def _(value: int) -> str: return f"integer: {value}"
@describe.register
def _(value: str) -> str: return f"text: {value}"

def main() -> None: print(product([2,3,4])); print(add_tax(10)); print(describe(42))
if __name__=="__main__": main()
