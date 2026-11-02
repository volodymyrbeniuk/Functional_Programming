from lab import Num,Add,Mul,evaluate
def test_expression_evaluation():
 assert evaluate(Mul(Add(Num(2),Num(3)),Num(4)))==20
