import pytest
from lab import normalize
def test_pure_etl_transform():
 row={"category":" Food ","amount":"12.345"}
 assert normalize([row])==[{"category":"food","amount":12.35}] and row["category"]==" Food "
 with pytest.raises(ValueError): normalize([{"amount":"-1"}])
