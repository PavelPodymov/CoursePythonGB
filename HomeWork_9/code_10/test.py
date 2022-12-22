"""Module for testing"""
import unittest
import main


class TestMain(unittest.TestCase):
    """MainTest"""

    def test_max_number(self):
        """test check_predicate"""
        self.assertEqual(main.max_number("1114111"), 4)

    def test_max_number_2(self):
        """test check_predicate"""
        self.assertNotEqual(main.max_number_2("111415"), 4)


if __name__ == '__main__':
    unittest.main()
