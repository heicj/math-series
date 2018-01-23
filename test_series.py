from series import fibonacci
""" Importing the object fibonacci, which is a function defined in series.py"""

import unittest

class TestIt(unittest.TestCase):
    def test_1(self):
        self.assertEqual(fibonacci(3), 2)

    def test_2(self):
        self.assertEqual(fibonacci(4), 2)

if __name__ == '__main__':
    unittest.main()
