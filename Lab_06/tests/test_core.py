import pytest
from lab import make_multiplier, retry
def test_closure_and_retry():
 assert make_multiplier(4)(3)==12
 calls=[]
 @retry(3)
 def flaky():
  calls.append(1)
  if len(calls)<2: raise RuntimeError()
  return "ok"
 assert flaky()=="ok" and len(calls)==2
