import unittest
import secondday


class TestSecondday(unittest.TestCase):
    def test_count_substrings(self):
        self.assertEqual(secondday.count_substrings("This is a test string", "is"), 2)
        self.assertEqual(secondday.count_substrings("babababa", "baba"), 2)
        self.assertEqual(secondday.count_substrings("Python is an awesome language to program in!", "o"), 4)
        self.assertEqual(secondday.count_substrings("We have nothing in common!", "really?"), 0)
        self.assertEqual(secondday.count_substrings("This is this and that is this", "this"), 2)

    def test_sum_matrix(self):
        self.assertEqual(secondday.sum_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), 45)
        self.assertEqual(secondday.sum_matrix([[0, 0, 0], [0, 0, 0], [0, 0, 0]]), 0)
        self.assertEqual(secondday.sum_matrix([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]), 55)

    def test_nan_expand(self):
        self.assertEqual(secondday.nan_expand(0), "")
        self.assertEqual(secondday.nan_expand(1), "Not a NaN")
        self.assertEqual(secondday.nan_expand(2), "Not a Not a NaN")
        self.assertEqual(secondday.nan_expand(3), "Not a Not a Not a NaN")

    def test_prime_factorization(self):
        self.assertEqual(secondday.prime_factorization(10), [(2, 1), (5, 1)])
        self.assertEqual(secondday.prime_factorization(14), [(2, 1), (7, 1)])
        self.assertEqual(secondday.prime_factorization(356), [(2, 2), (89, 1)])
        self.assertEqual(secondday.prime_factorization(89), [(89, 1)])
        self.assertEqual(secondday.prime_factorization(1000), [(2, 3), (5, 3)])

    def test_group(self):
        self.assertEqual(secondday.group([1, 1, 1, 2, 3, 1, 1]), [[1, 1, 1], [2], [3], [1, 1]])
        self.assertEqual(secondday.group([1, 2, 1, 2, 3, 3]), [[1], [2], [1], [2], [3, 3]])

    def test_max_consective(self):
        self.assertEqual(secondday.max_consective([1, 2, 3, 3, 3, 3, 4, 3, 3]), 4)
        self.assertEqual(secondday.max_consective([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 5]), 3)

    def test_gas_stations(self):
        self.assertEqual(secondday.gas_stations(320, 90, [50, 80, 140, 180, 220, 290]), [80, 140, 220, 290])
        self.assertEqual(secondday.gas_stations(390, 80, [70, 90, 140, 210, 240, 280, 350]), [70, 140, 210, 280, 350])


if __name__ == '__main__':
    unittest.main()
