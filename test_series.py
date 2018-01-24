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
	
