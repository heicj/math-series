fibonacci_test
from series import fibonacci, lucas, sum_series
""" Importing the objects fibonacci, lucas, sum_series which are functions defined in series.py"""

import unittest

class TestIt(unittest.TestCase):
    """ Test fibonacci: test_1 should pass, test_2 should fail """
    def test_1(self):
        self.assertEqual(fibonacci(3), 2)

    def test_2(self):
        self.assertEqual(fibonacci(4), 2)

class TestIt2(unittest.TestCase):
    """ Test lucas: test_1 should pass, test_2 should fail """
    def test_1(self):
        self.assertEqual(lucas(3), 4)

    def test_2(self):
        self.assertEqual(lucas(4), 3)

class TestIt3(unittest.TestCase):
    """ Test sum_series """
    def test_1(self):
        """ Pass Test for fibonacci portion """
        self.assertEqual(sum_series(4), 3)

    def test_2(self):
        """ Fail Test for fibonacci portion """
        self.assertEqual(sum_series(4), 6)
    
    def test_3(self):
        """ Pass Test for lucas portion """
        self.assertEqual(sum_series(4, 2, 1), 7)

    def test_4(self):
        """ Fail Test for lucas portion"""
        self.assertEqual(sum_series(4, 2, 1), 3)

if __name__ == '__main__':
    unittest.main()

from series import fibonnacci
from series import lucas
from series import sum_series
import unittest

class TestIt(unittest.TestCase):
	def test_1(self):
		self.assertEqual(fibonnacci(3), 2)
	def test_2(self):
		self.assertEqual(fibonnacci(4), 2)
	def test_3(self):
		self.assertEqual(lucas(2), 3)
	def test_4(self):
		self.assertEqual(lucas(4), 6)
	def test_5(self):
		self.assertEqual(sum_series(3), 2)
	def test_6(self):
		self.assertEqual(sum_series(2, 2, 1), 3)

	
if __name__ == '__main__':
	unittest.main()
	

