from lab import Parsed,ParseError,integer,literal,map_parser
def test_parser_combinators():
 assert integer("-42x")==Parsed(-42,3)
 assert isinstance(integer("x"),ParseError)
 assert literal("ab")("abc",0)==Parsed("ab",2)
 assert map_parser(integer,lambda n:n*2)("21",0)==Parsed(42,2)
