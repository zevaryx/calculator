from .interpreter import Interpreter
from .lexer import Lexer
from .parser_ import Parser

def calculate(expression: str) -> int | None:
    """
    Calculate the given expression
    """
    lexer = Lexer(expression)
    tokens = lexer.generate_tokens()
    parser = Parser(tokens)
    tree = parser.parse()
    if not tree:
        return None
    interpreter = Interpreter()
    value = interpreter.visit(tree)
    return value