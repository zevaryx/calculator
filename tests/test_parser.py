import unittest
from calculator.tokens import Token, TokenType
from calculator.parser_ import Parser
from calculator.nodes import (
    NumberNode,
    AddNode,
    SubtractNode,
    MultiplyNode,
    DivideNode,
    PowerNode,
    ModuloNode,
)


class TestParser(unittest.TestCase):
    def test_empty(self):
        tokens = []
        node = Parser(tokens).parse()
        self.assertEqual(node, None)

    def test_numbers(self):
        tokens = [Token(TokenType.NUMBER, 100)]
        node = Parser(tokens).parse()
        self.assertEqual(node, NumberNode(100))

    def test_individual_operations(self):
        tokens = [
            Token(TokenType.NUMBER, 21),
            Token(TokenType.PLUS),
            Token(TokenType.NUMBER, 23),
        ]
        node = Parser(tokens).parse()
        self.assertEqual(node, AddNode(NumberNode(21), NumberNode(23)))

        tokens = [
            Token(TokenType.NUMBER, 21),
            Token(TokenType.MINUS),
            Token(TokenType.NUMBER, 23),
        ]
        node = Parser(tokens).parse()
        self.assertEqual(node, SubtractNode(NumberNode(21), NumberNode(23)))

        tokens = [
            Token(TokenType.NUMBER, 21),
            Token(TokenType.MULTIPLY),
            Token(TokenType.NUMBER, 23),
        ]
        node = Parser(tokens).parse()
        self.assertEqual(node, MultiplyNode(NumberNode(21), NumberNode(23)))

        tokens = [
            Token(TokenType.NUMBER, 21),
            Token(TokenType.DIVIDE),
            Token(TokenType.NUMBER, 23),
        ]
        node = Parser(tokens).parse()
        self.assertEqual(node, DivideNode(NumberNode(21), NumberNode(23)))

        tokens = [
            Token(TokenType.NUMBER, 21),
            Token(TokenType.POWER),
            Token(TokenType.NUMBER, 23),
        ]
        node = Parser(tokens).parse()
        self.assertEqual(node, PowerNode(NumberNode(21), NumberNode(23)))

        tokens = [
            Token(TokenType.NUMBER, 21),
            Token(TokenType.MODULO),
            Token(TokenType.NUMBER, 23),
        ]
        node = Parser(tokens).parse()
        self.assertEqual(node, ModuloNode(NumberNode(21), NumberNode(23)))

    def test_full_expression(self):
        tokens = [
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
        ]

        node = Parser(tokens).parse()
        self.assertEqual(
            node,
            ModuloNode(
                SubtractNode(
                    AddNode(
                        PowerNode(NumberNode(10), NumberNode(2)),
                        AddNode(
                            DivideNode(NumberNode(21), NumberNode(7)),
                            NumberNode(7),
                        ),
                    ),
                    MultiplyNode(NumberNode(5), NumberNode(2)),
                ),
                NumberNode(100),
            ),
        )
