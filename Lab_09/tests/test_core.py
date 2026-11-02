from lab import Ok,Err,parse_positive
def test_result_short_circuit():
 assert parse_positive("12")==Ok(12)
 assert isinstance(parse_positive("x"),Err) and isinstance(parse_positive("-1"),Err)
