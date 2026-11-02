from lab import product, add_tax, describe
def test_functional_tools():
 assert product([2,3,4])==24 and product([])==1
 assert add_tax(10)==15
 assert describe(2)=="integer: 2" and describe("a")=="text: a"
