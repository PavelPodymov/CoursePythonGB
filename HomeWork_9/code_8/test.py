"""Module for testing"""
import unittest
import main


class TestMain(unittest.TestCase):
    """MainTest"""

    def test_check_predicate(self):
        """test check_predicate"""
        self.assertTrue(main.check_predicate([0, 0, 0]), True)


if __name__ == '__main__':
    unittest.main()
