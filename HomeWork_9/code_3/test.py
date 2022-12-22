"""Module for testing"""
import unittest
import main


class TestMain(unittest.TestCase):
    """MainTest"""

    def test_rnd(self):
        """random number"""
        self.assertTrue(main.rnd())

    def test_create_fun(self):
        """test create_fun"""
        self.assertTrue(main.create_fun(3))

    def test_create_str(self):
        """test create_str"""
        self.assertEqual(main.create_str([81, 48, 64, 27]), "27x^3 + 64x^2 + 48x + 81 = 0")

    def test_sq_mn(self):
        """test sq_mn"""
        self.assertEqual(main.sq_mn("27x^3"), 3)

    def test_k_mn(self):
        """test k_mn"""
        self.assertEqual(main.k_mn("27x^3"), 27)


if __name__ == '__main__':
    unittest.main()
