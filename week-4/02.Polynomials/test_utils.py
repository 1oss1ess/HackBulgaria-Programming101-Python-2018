import unittest

from utils import (
    extract_term,
    extract_variable_and_power
)

class ExtractVariableAndPower(unittest.TestCase):
    def test_different_cases(self):
        with self.subTest('extract x'):
            self.assertEqual(
                ('x', 1),
                extract_variable_and_power('x')
            )

        with self.subTest('extract x^1'):
            self.assertEqual(
                ('x', 1),
                extract_variable_and_power('x^1')
            )

class ExtractTerm(unittest.TestCase):
    def test_different_cases(self):
        with self.subTest('extract 2'):
            self.assertEqual((2, None, None), extract_term('2'))

        with self.subTest('extract 2*x'):
            self.assertEqual((2, 'x', 1), extract_term('2*x'))

        with self.subTest('extract 2*x^3'):
            self.assertEqual((2, 'x', 3), extract_term('2*x^3'))

        with self.subTest('extract x'):
            self.assertEqual((1, 'x', 1), extract_term('x'))

        with self.subTest('extract x^2'):
            self.assertEqual((1, 'x', 2), extract_term('x^2'))

        with self.subTest('extract 1*x^2'):
            self.assertEqual((1, 'x', 2), extract_term('1*x^2'))

        with self.subTest('extract 1*x'):
            self.assertEqual((1, 'x', 1), extract_term('1*x'))

if __name__ == '__main__':
    unittest.main()
