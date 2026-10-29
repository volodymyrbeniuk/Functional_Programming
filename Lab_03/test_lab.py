import pytest
from lab import Student, add_grade, unique_tags, with_entry
def test_immutable_updates():
 s=Student("A",(90,)); assert add_grade(s,95).grades==(90,95); assert s.grades==(90,)
 assert unique_tags(["x","x"])==frozenset({"x"})
 assert dict(with_entry({"a":1},"b",2))=={"a":1,"b":2}
 with pytest.raises(ValueError): add_grade(s,101)
