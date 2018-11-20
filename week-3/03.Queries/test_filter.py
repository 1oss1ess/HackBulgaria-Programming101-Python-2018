import unittest
import filter


class TestFilter(unittest.TestCase):

    def test_filter_by_full_name(self):
        list_of_person = [['Michael Harris', 'lime', "Scott, Young and King", 'zacharymcdonald@gmail.com', '114 - 116 - 1124x315', 2151], ['Diana Filipova', 'lime', "Scott, Young and King", 'zacharymcdonald@yahoo.com', '114-116-1124x315,2151'], ['Diana Harris', 'lime', "Scott, Young and King", 'zacharymcdonald@yahoo.com', '114 - 116 - 1124x315', 2151], ['Diana Harris', 'green', "Scott, Young and King", 'kaitlynmalone@gmail.com', '114-116-1124x315,2151']]

        result = [['Diana Harris', 'lime', "Scott, Young and King", 'zacharymcdonald@yahoo.com', '114 - 116 - 1124x315', 2151], ['Diana Harris', 'green', "Scott, Young and King", 'kaitlynmalone@gmail.com', '114-116-1124x315,2151']]

        self.assertEqual(filter.filter_by_full_name(list_of_person), result)
        self.assertEqual(filter.filter_by_full_name([['Michael Olson', 'olive', "Scott, Young and King", 'zacharymcdonald@gmail.com', '114 - 116 - 1124x315', 2151]]), [])
        self.assertEqual(filter.filter_by_full_name([['Diana Harris', 'olive', "Scott, Young and King", 'zacharymcdonald@gmail.com', '114 - 116 - 1124x315', 2151]], 'Diana Harris'), [['Diana Harris', 'olive', "Scott, Young and King", 'zacharymcdonald@gmail.com', '114 - 116 - 1124x315', 2151]])
        self.assertEqual(filter.filter_by_full_name([[]], 'Diana Harris'), [])

    def test_filter_by_fname_and_color(self):
        list_of_person = [['Diana Harris', 'lime', "Scott, Young and King", 'zacharymcdonald@yahoo.com', '114 - 116 - 1124x315', 2151], ['Diana Harris', 'green', "Scott, Young and King", 'kaitlynmalone@gmail.com', '114-116-1124x315,2151']]

        result = [['Diana Harris', 'lime', "Scott, Young and King", 'zacharymcdonald@yahoo.com', '114 - 116 - 1124x315', 2151]]

        self.assertEqual(filter.filter_by_fname_and_color(list_of_person), result)
        self.assertEqual(filter.filter_by_fname_and_color([['Diana Harris', 'green', "Scott, Young and King", 'kaitlynmalone@gmail.com', '114-116-1124x315,2151']]), [])

    def test_startswith_fname(self):
        data = [['Diana Harris', 'lime', "Scott, Young and King", 'zacharymcdonald@yahoo.com', '114 - 116 - 1124x315', 2151], ['Dianas Harris', 'green', "Scott, Young and King", 'kaitlynmalone@gmail.com', '114-116-1124x315,2151']]

        result = [['Diana Harris', 'lime', "Scott, Young and King", 'zacharymcdonald@yahoo.com', '114 - 116 - 1124x315', 2151]]

        self.assertEqual(filter.startswith_fname(data), result)

    def test_contains_email(self):
        data = [['Michael Harris', 'lime', "Scott, Young and King", 'zacharymcdonald@gmail.com', '114 - 116 - 1124x315', 2151], ['Diana Filipova', 'lime', "Scott, Young and King", 'zacharymcdonald@yahoo.com', '114-116-1124x315,2151'], ['Diana Harris', 'lime', "Scott, Young and King", 'zacharymcdonald@yahoo.com', '114 - 116 - 1124x315', 2151], ['Diana Harris', 'green', "Scott, Young and King", 'kaitlynmalone@gmail.com', '114-116-1124x315,2151']]
        expect_data = [['Michael Harris', 'lime', "Scott, Young and King", 'zacharymcdonald@gmail.com', '114 - 116 - 1124x315', 2151], ['Diana Harris', 'green', "Scott, Young and King", 'kaitlynmalone@gmail.com', '114-116-1124x315,2151']]

        self.assertEqual(filter.contains_email(data), expect_data)

    def test_filter_by_salary(self):
        data = [['Amber Ware', 'yellow', 'Townsend Inc', 'lambthomas@gmail.com', '867.131.2353', 435], ['Michael Harris', 'lime', "Scott, Young and King", 'zacharymcdonald@gmail.com', '114 - 116 - 1124x315', 2999], ['Diana Harris', 'lime', "Scott, Young and King", 'zacharymcdonald@yahoo.com', '114 - 116 - 1124x315', 2151]]
        expext_data = [['Michael Harris', 'lime', "Scott, Young and King", 'zacharymcdonald@gmail.com', '114 - 116 - 1124x315', 2999], ['Diana Harris', 'lime', "Scott, Young and King", 'zacharymcdonald@yahoo.com', '114 - 116 - 1124x315', 2151]]

        self.assertEqual(filter.filter_by_salary(data), expext_data)


if __name__ == '__main__':
    unittest.main()
