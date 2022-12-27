from .tokens import Token, TokenType
from string import digits

WHITESPACE = " \r\n\t"


class Lexer:
    def __init__(self, text):
        self.text = iter(text)
        self.advance()

    def advance(self):
        try:
            self.current_char = next(self.text)
        except StopIteration:
            self.current_char = None

    def generate_tokens(self):
        while self.current_char is not None:
            match self.current_char:
                case x if x in WHITESPACE:
                    self.advance()
                case x if x in digits or x == ".":
                    yield self.generate_number()
                case "+":
                    self.advance()
                    yield Token(TokenType.PLUS)
                case "-":
                    self.advance()
                    yield Token(TokenType.MINUS)
                case "*" | "x" | "×":
                    self.advance()
                    yield Token(TokenType.MULTIPLY)
                case "/" | "÷":
                    self.advance()
                    yield Token(TokenType.DIVIDE)
                case "(":
                    self.advance()
                    yield Token(TokenType.LPAREN)
                case ")":
                    self.advance()
                    yield Token(TokenType.RPAREN)
                case "^":
                    self.advance()
                    yield Token(TokenType.POWER)
                case "%":
                    self.advance()
                    yield Token(TokenType.MODULO)
                case _:
                    raise Exception(f"Illegal Character: '{self.current_char}'")

    def generate_number(self):
        decimal_pt_count = 0
        number_str = self.current_char
        self.advance()

        while self.current_char is not None and (self.current_char == "." or self.current_char in digits):
            if self.current_char == ".":
                decimal_pt_count += 1
                if decimal_pt_count > 1:
                    break

            number_str += self.current_char
            self.advance()

        if number_str.startswith("."):
            number_str = "0" + number_str

        if number_str.endswith("."):
            number_str += "0"

        return Token(
            TokenType.NUMBER,
            float(number_str) if "." in number_str else int(number_str),
        )
