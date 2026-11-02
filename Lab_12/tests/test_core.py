import pytest
from lab import sort_values,is_sorted,stable_unique,parse_csv_ints
def test_invariants_examples():
 values=[3,1,2,1]; result=sort_values(values)
 assert result==[1,1,2,3] and is_sorted(result) and values==[3,1,2,1]
 assert stable_unique(values)==[3,1,2] and parse_csv_ints("1, 2")==[1,2]
 with pytest.raises(ValueError): parse_csv_ints("1,x")
