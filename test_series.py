from series import fibonacci, lucas
""" Importing the object fibonacci, which is a function defined in series.py"""

import unittest

class TestIt(unittest.TestCase):
    def test_1(self):
        self.assertEqual(fibonacci(3), 2)

    def test_2(self):
        self.assertEqual(fibonacci(4), 2)

class TestIt2(unittest.TestCase):
    def test_1(self):
        self.assertEqual(lucas(3), 4)

    def test_2(self):
        self.assertEqual(lucas(4), 3)

if __name__ == '__main__':
    unittest.main()
