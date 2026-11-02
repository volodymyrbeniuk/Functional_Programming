import pytest
from lab import Event,parse_line,summarize
def test_log_pipeline():
 assert parse_line("error | disk full | 18")==Event("ERROR","disk full",18)
 assert summarize([Event("INFO","ready",3),Event("ERROR","disk full",18)])=={"count":2,"errors":1,"total_duration_ms":21,"messages":["disk full"]}
 with pytest.raises(ValueError): parse_line("ERROR|bad|x")
