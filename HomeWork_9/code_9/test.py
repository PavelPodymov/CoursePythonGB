"""Module for testing"""
import unittest
import main


class TestMain(unittest.TestCase):
    """MainTest"""

    def test_raises(self):
        """используем функцию assertRaises"""
        with self.assertRaises(main.ZeroDivisionException):
            main.my_function()

    def test_raises_2(self):
        """используем функцию assertRaises"""
        with self.assertRaises(Exception):
            main.my_function_2()


if __name__ == '__main__':
    unittest.main()
