"""Module for testing"""
import unittest
import main


class TestMain(unittest.TestCase):
    """MainTest"""

    def test_add(self):
        """Add"""
        self.assertEqual(main.add(1, 2), 3)

    def test_sub(self):
        """Sub"""
        self.assertEqual(main.sub(4, 2), 2)

    def test_mul(self):
        """Mult"""
        self.assertNotEqual(main.mul(2, 5), 11)

    def test_div(self):
        """Div"""
        self.assertEqual(main.div(8, 4), 2)


if __name__ == '__main__':
    unittest.main()
