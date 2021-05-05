from .tokens import TokenType
from .nodes import *


class Parser:
    def __init__(self, tokens):
        self.tokens = iter(tokens)
        self.advance()

    def raise_error(self, e = None):
        if e:
            raise Exception(f"Error: {e}")
        raise Exception("Invalid syntax")

    def advance(self):
        try:
            self.current_token = next(self.tokens)
        except StopIteration:
            self.current_token = None

    def parse(self):
        if self.current_token is None:
            return

        result = self.expr()

        if self.current_token is not None:
            self.raise_error("Current token is not None")

        return result

    def expr(self):
        result = self.term()
        while self.current_token is not None and self.current_token.type in (
            TokenType.PLUS,
            TokenType.MINUS,
        ):
            match self.current_token.type:
                case TokenType.PLUS:
                    self.advance()
                    result = AddNode(result, self.term())
                case TokenType.MINUS:
                    self.advance()
                    result = SubtractNode(result, self.term())

        return result

    def term(self):
        result = self.factor()

        while self.current_token is not None and self.current_token.type in (
            TokenType.MULTIPLY,
            TokenType.DIVIDE,
            TokenType.POWER,
            TokenType.MODULO,
        ):
            match self.current_token.type:
                case TokenType.MULTIPLY:
                    self.advance()
                    result = MultiplyNode(result, self.factor())
                case TokenType.DIVIDE:
                    self.advance()
                    result = DivideNode(result, self.factor())
                case TokenType.POWER:
                    self.advance()
                    result = PowerNode(result, self.factor())
                case TokenType.MODULO:
                    self.advance()
                    result = ModuloNode(result, self.factor())

        return result

    def factor(self):
        token = self.current_token

        match token.type:
            case TokenType.LPAREN:
                self.advance()
                result = self.expr()
                if self.current_token.type != TokenType.RPAREN:
                    self.raise_error()
                self.advance()
                return result
            case TokenType.NUMBER:
                self.advance()
                return NumberNode(token.value)
            case TokenType.PLUS:
                self.advance()
                return PlusNode(self.factor())
            case TokenType.MINUS:
                self.advance()
                return MinusNode(self.factor())

        self.raise_error("Invalid factor token")
