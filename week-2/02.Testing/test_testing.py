import unittest
import testing


class TestTesting(unittest.TestCase):
    def test_simplify_fraction(self):
        self.assertEqual(testing.simplify_fraction((3, 9)), (1, 3))
        self.assertEqual(testing.simplify_fraction((1, 7)), (1, 7))
        self.assertEqual(testing.simplify_fraction((4, 10)), (2, 5))
        self.assertEqual(testing.simplify_fraction((63, 462)), (3, 22))
        self.assertEqual(testing.simplify_fraction((0, 3)), 0)
        with self.assertRaises(Exception) as context:
            testing.simplify_fraction((6, 0))
        self.assertTrue("Division by zero is undefined", context.exception)

    def test_collect_fractions(self):
        self.assertEqual(testing.collect_fractions([(1, 4), (1, 2)]), (3, 4))
        self.assertEqual(testing.collect_fractions([(1, 7), (2, 6)]), (10, 21))

    def test_sort_fractions(self):
        self.assertEqual(testing.sort_fractions([(2, 3), (1, 2)]), [(1, 2), (2, 3)])
        self.assertEqual(testing.sort_fractions([(2, 3), (1, 2), (1, 3)]), [(1, 3), (1, 2), (2, 3)])
        self.assertEqual(testing.sort_fractions([(5, 6), (22, 78), (22, 7), (7, 8), (9, 6), (15, 32)]), [(22, 78), (15, 32), (5, 6), (7, 8), (9, 6), (22, 7)])


if __name__ == '__main__':
    unittest.main()
