import sys
from calculator.interpreter import Interpreter
from calculator.lexer import Lexer
from calculator.parser_ import Parser

if __name__ == "__main__":
    MIN_PYTHON = (3, 10)

    if sys.version_info < MIN_PYTHON:
        sys.exit("Python {}.{} or later is required".format(*MIN_PYTHON))

    while True:
        try:
            text = input(">> ")
            lexer = Lexer(text)
            tokens = lexer.generate_tokens()
            parser = Parser(tokens)
            tree = parser.parse()
            if not tree:
                continue
            interpreter = Interpreter()
            value = interpreter.visit(tree)
            print(value)
        except Exception as e:
            print(e)
