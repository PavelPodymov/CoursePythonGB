"""Module for testing"""
import unittest
import main


class TestMain(unittest.TestCase):
    """MainTest"""

    def test_notisinstance(self):
        """используем функцию assertNotIsInstance"""
        self.assertNotIsInstance(main.TrafficLight, main.TrafficLight)

    def test_isinstance(self):
        """используем функцию assertIsInstance"""
        self.assertIsInstance(main.t, main.TrafficLight)

    def test_assertIsNone(self):
        """test isinstance_2"""
        self.assertIsNotNone(main.TrafficLight.jogging)


if __name__ == '__main__':
    unittest.main()
