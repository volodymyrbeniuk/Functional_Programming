import pytest
from lab import quicksort, randomized_select, fibonacci
def test_algorithms():
 a=[4,2,4,1]; assert quicksort(a)==[1,2,4,4]; assert a==[4,2,4,1]
 assert randomized_select(a,3)==4; assert fibonacci(10)==55
 with pytest.raises(ValueError): randomized_select(a,0)
