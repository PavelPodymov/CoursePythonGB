"""Module for testing"""
import unittest
import main


class TestMain(unittest.TestCase):
    """MainTest"""

    def test_fibo(self):
        """test fibo"""
        self.assertEqual(main.fibo(5), 5)

    def test_fibo_neg(self):
        """test fact"""
        self.assertEqual(main.fibo_neg(-1), 1)


if __name__ == '__main__':
    unittest.main()
