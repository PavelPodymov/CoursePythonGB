"""Module for testing"""
import unittest
import main


class TestMain(unittest.TestCase):
    """MainTest"""

    def test_fact(self):
        """test fact"""
        self.assertTrue(main.fact(5))

    def test_fact_1(self):
        """test fact"""
        self.assertEqual(main.fact(5), 120)

    def test_fact_list(self):
        """test fact_list"""
        self.assertIn(120, main.fact_list(6))


if __name__ == '__main__':
    unittest.main()
