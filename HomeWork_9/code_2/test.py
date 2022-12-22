"""Module for testing"""
import unittest
import main


class TestMain(unittest.TestCase):
    """MainTest"""

    def test_get_list(self):
        """get_list"""
        self.assertEqual(main.get_list(3), [1, 2, 3])

    def test_unsorted_list(self):
        """get_list"""
        self.assertEqual(main.get_unsorted_list([3, 2, 1]), [3, 2, 1])


if __name__ == '__main__':
    unittest.main()
