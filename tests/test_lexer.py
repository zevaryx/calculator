import unittest
from calculator.lexer import Lexer
from calculator.tokens import Token, TokenType


class TestLexer(unittest.TestCase):
    def test_empty(self):
        tokens = list(Lexer("").generate_tokens())
        self.assertEqual(tokens, [])

    def test_whitespace(self):
        tokens = list(Lexer("\t\n \t\t\n\n\r\r").generate_tokens())
        self.assertEqual(tokens, [])

    def test_numbers(self):
        tokens = list(Lexer("123 123.456 123. .456 .").generate_tokens())
        self.assertEqual(
            tokens,
            [
                Token(TokenType.NUMBER, 123),
                Token(TokenType.NUMBER, 123.456),
                Token(TokenType.NUMBER, 123.0),
                Token(TokenType.NUMBER, 0.456),
                Token(TokenType.NUMBER, 0.0),
            ],
        )

    def test_operators(self):
        tokens = list(Lexer("+-*/^%").generate_tokens())
        self.assertEqual(
            tokens,
            [
                Token(TokenType.PLUS),
                Token(TokenType.MINUS),
                Token(TokenType.MULTIPLY),
                Token(TokenType.DIVIDE),
                Token(TokenType.POWER),
                Token(TokenType.MODULO),
            ],
        )

    def test_parens(self):
        tokens = list(Lexer("()").generate_tokens())
        self.assertEqual(
            tokens, [Token(TokenType.LPAREN), Token(TokenType.RPAREN)]
        )

    def test_all(self):
        tokens = list(
            Lexer("(10 ^ 2 + (21 / 7 + 7) - 5 * 2) % 100").generate_tokens()
        )
        self.assertEqual(
            tokens,
            [
                Token(TokenType.LPAREN),
                Token(TokenType.NUMBER, 10),
                Token(TokenType.POWER),
                Token(TokenType.NUMBER, 2),
                Token(TokenType.PLUS),
                Token(TokenType.LPAREN),
                Token(TokenType.NUMBER, 21),
                Token(TokenType.DIVIDE),
                Token(TokenType.NUMBER, 7),
                Token(TokenType.PLUS),
                Token(TokenType.NUMBER, 7),
                Token(TokenType.RPAREN),
                Token(TokenType.MINUS),
                Token(TokenType.NUMBER, 5),
                Token(TokenType.MULTIPLY),
                Token(TokenType.NUMBER, 2),
                Token(TokenType.RPAREN),
                Token(TokenType.MODULO),
                Token(TokenType.NUMBER, 100),
            ],
        )
