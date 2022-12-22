"""Module for testing"""
import unittest
import main


class TestMain(unittest.TestCase):
    """MainTest"""

    def test_int_funcs(self):
        """test fibo"""
        self.assertEqual(main.int_funcs("texts"), "Texts")


if __name__ == '__main__':
    unittest.main()
