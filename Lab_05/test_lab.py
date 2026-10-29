import pytest
from lab import take, drop, fibonacci_stream, sliding_windows
def test_lazy_tools():
 assert take(7,fibonacci_stream())==[0,1,1,2,3,5,8]
 assert list(drop(2,[1,2,3]))==[3]
 assert list(sliding_windows([1,2,3],2))==[(1,2),(2,3)]
 with pytest.raises(ValueError): list(sliding_windows([],0))
