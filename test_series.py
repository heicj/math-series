from series import fibonnacci
from series import lucas
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

	
if __name__ == '__main__':
	unittest.main()
	
