import unittest
import firstday


class TestFirstday(unittest.TestCase):

    def test_sum_of_digits(self):
        self.assertEqual(firstday.sum_of_digits(1325132435356), 43)
        self.assertEqual(firstday.sum_of_digits(123), 6)
        self.assertEqual(firstday.sum_of_digits(-10), 1)

    def test_to_digits(self):
        self.assertEqual(firstday.to_digits(123), [1, 2, 3])
        self.assertEqual(firstday.to_digits(99999), [9, 9, 9, 9, 9])
        self.assertEqual(firstday.to_digits(123023), [1, 2, 3, 0, 2, 3])

    def test_to_number(self):
        self.assertEqual(firstday.to_number([1, 2, 3]), 123)
        self.assertEqual(firstday.to_number([1, 2, 3, 0, 2, 3]), 123023)
        self.assertEqual(firstday.to_number([9, 9, 9, 9, 9]), 99999)
        self.assertEqual(firstday.to_number([21, 2, 33]), 21233)

    def test_fact_digits(self):
        self.assertEqual(firstday.fact_digits(111), 3)
        self.assertEqual(firstday.fact_digits(145), 145)
        self.assertEqual(firstday.fact_digits(999), 1088640)

    def test_fibonacci(self):
        self.assertEqual(firstday.fibonacci(1), [1])
        self.assertEqual(firstday.fibonacci(2), [1, 1])
        self.assertEqual(firstday.fibonacci(3), [1, 1, 2])
        self.assertEqual(firstday.fibonacci(10), [1, 1, 2, 3, 5, 8, 13, 21, 34, 55])

    def test_fib_number(self):
        self.assertEqual(firstday.fib_number(3), 112)
        self.assertEqual(firstday.fib_number(10), 11235813213455)

    def test_palindrome(self):
        self.assertTrue(firstday.palindrome(121), True)
        self.assertTrue(firstday.palindrome("kapak"), True)
        self.assertFalse(firstday.palindrome("baba"), False)

    def test_count_vowels(self):
        self.assertEqual(firstday.count_vowels("Python"), 2)
        self.assertEqual(firstday.count_vowels("Theistareykjarbunga"), 8)
        self.assertEqual(firstday.count_vowels("grrrrgh!"), 0)
        self.assertEqual(firstday.count_vowels("Github is the second best thing that happend to programmers, after the keyboard!"), 22)
        self.assertEqual(firstday.count_vowels("A nice day to code!"), 8)

    def test_count_consonants(self):
        self.assertEqual(firstday.count_consonants("Python"), 4)
        self.assertEqual(firstday.count_consonants("Theistareykjarbunga"), 11)
        self.assertEqual(firstday.count_consonants("grrrrgh!"), 7)
        self.assertEqual(firstday.count_consonants("Github is the second best thing that happend to programmers, after the keyboard!"), 44)
        self.assertEqual(firstday.count_consonants("A nice day to code!"), 6)

    def test_char_histogram(self):
        self.assertEqual(firstday.char_histogram("Python!"), {'P': 1, 'y': 1, 't': 1, 'h': 1, 'o': 1, 'n': 1, '!': 1})
        self.assertEqual(firstday.char_histogram("AAAAaaa!!!"), {'A': 4, 'a': 3, '!': 3})


if __name__ == '__main__':
    unittest.main()
