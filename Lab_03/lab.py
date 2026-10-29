"""Immutable values and copy-on-write transformations."""
from dataclasses import dataclass, replace
from types import MappingProxyType
from typing import Mapping

@dataclass(frozen=True)
class Student:
    name: str
    grades: tuple[int, ...]

def add_grade(student: Student, grade: int) -> Student:
    if not 0 <= grade <= 100: raise ValueError("grade must be between 0 and 100")
    return replace(student, grades=student.grades+(grade,))

def with_entry(data: Mapping[str, int], key: str, value: int) -> Mapping[str, int]:
    return MappingProxyType({**data, key:value})

def unique_tags(tags: list[str]) -> frozenset[str]: return frozenset(tags)

def main() -> None:
    original=Student("Ada", (95,)); updated=add_grade(original, 99)
    print("Original:", original); print("Updated:", updated)
if __name__=="__main__": main()
