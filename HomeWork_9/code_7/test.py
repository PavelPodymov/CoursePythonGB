"""Module for testing"""
import unittest
import main


class TestMain(unittest.TestCase):
    """MainTest"""

    def test_notisinstance(self):
        """используем функцию assertNotIsInstance"""
        self.assertNotIsInstance(main.TownCar, main.Car)

    def test_isinstance(self):
        """используем функцию assertIsInstance"""
        self.assertIsInstance(main.town_1, main.Car)


if __name__ == '__main__':
    unittest.main()
