import unittest
from calculator.nodes import (
    NumberNode,
    AddNode,
    SubtractNode,
    MultiplyNode,
    DivideNode,
    PowerNode,
    ModuloNode,
)
from calculator.interpreter import Interpreter
from calculator.values import Number


class TestInterpreter(unittest.TestCase):
    def test_numbers(self):
        val = Interpreter().visit(NumberNode(42))
        self.assertEqual(val, Number(42))

    def test_individual_operations(self):
        val = Interpreter().visit(AddNode(NumberNode(21), NumberNode(21)))
        self.assertEqual(val, Number(42))

        val = Interpreter().visit(SubtractNode(NumberNode(21), NumberNode(21)))
        self.assertEqual(val, Number(0))

        val = Interpreter().visit(MultiplyNode(NumberNode(21), NumberNode(21)))
        self.assertEqual(val, Number(441))

        val = Interpreter().visit(DivideNode(NumberNode(21), NumberNode(21)))
        self.assertEqual(val, Number(1))

        val = Interpreter().visit(PowerNode(NumberNode(21), NumberNode(21)))
        self.assertEqual(val, Number(5842587018385982521381124421))

        val = Interpreter().visit(ModuloNode(NumberNode(21), NumberNode(21)))
        self.assertEqual(val, Number(0))

        with self.assertRaises(Exception):
            Interpreter().visit(DivideNode(NumberNode(42), NumberNode(0)))

    def test_full_expression(self):
        tree = ModuloNode(
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
        )

        result = Interpreter().visit(tree)

        self.assertEqual(result, Number(0.0))
