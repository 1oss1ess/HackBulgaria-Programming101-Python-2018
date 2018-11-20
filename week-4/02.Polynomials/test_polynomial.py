import unittest

from polynomial import Term, Polynomial


class TermTests(unittest.TestCase):
    def test_is_constant(self):
        with self.subTest('Term with coeff, variable and power is not'):
            t = Term(coeff=2, variable='x', power=3)

            self.assertFalse(t.is_constant)

        with self.subTest('Constant term is constant'):
            value = 2
            t = Term.constant(value)

            self.assertTrue(t.is_constant)

            self.assertEqual(value, t.coeff)
            self.assertIsNone(t.variable)
            self.assertEqual(0, t.power)

    def test_str_representation_of_term_is_correct(self):
        with self.subTest('Coefficient is bigger than 1'):
            t = Term(coeff=2, variable='x', power=3)

            expected = '2*x^3'
            self.assertEqual(expected, str(t))

        with self.subTest('Coefficient is 1'):
            t = Term(coeff=1, variable='x', power=3)

            expected = 'x^3'
            self.assertEqual(expected, str(t))

        with self.subTest('Power is 1'):
            t = Term(coeff=1, variable='x', power=1)

            expected = 'x'
            self.assertEqual(expected, str(t))

        with self.subTest('Coeff is bigger than 1, power is 1'):
            t = Term(coeff=2, variable='x', power=1)

            expected = '2*x'
            self.assertEqual(expected, str(t))

        with self.subTest('Term is constant'):
            t = Term.constant(2)

            expected = '2'
            self.assertEqual(expected, str(t))

    def test_derivative(self):
        with self.subTest('Derivative of constant is 0'):
            t = Term.constant(2)
            expected = Term.constant(0)

            self.assertEqual(expected, t.derivative())

        with self.subTest('Derivative of 2*x^1'):
            t = Term(coeff=2, variable='x', power=1)
            expected = Term.constant(2)

            self.assertEqual(expected, t.derivative())

        with self.subTest('Derivative of x^1'):
            t = Term(coeff=1, variable='x', power=1)
            expected = Term.constant(1)

            self.assertEqual(expected, t.derivative())

        with self.subTest('Derivative of 2*x^2'):
            t = Term(coeff=2, variable='x', power=2)
            expected = Term(coeff=4, variable='x', power=1)

            self.assertEqual(expected, t.derivative())


class PolynomialTests(unittest.TestCase):
    def test_terms_are_sorted_by_power(self):
        with self.subTest('Case 1'):
            terms = [
                Term(coeff=1, variable='x', power=2),
                Term(coeff=1, variable='x', power=5)
            ]

            p = Polynomial(terms)

            expected_terms = [
                Term(coeff=1, variable='x', power=5),
                Term(coeff=1, variable='x', power=2)
            ]

            self.assertEqual(expected_terms, p.terms)

if __name__ == '__main__':
    unittest.main()
