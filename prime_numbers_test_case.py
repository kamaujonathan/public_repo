import unittest
from prime_numbers import check_prime_numbers

class primeNumberTestcase(unittest.TestCase):

	def test_is_prime_a_string(self):
		if self.Is(str)
		self.raises(TypeError)

	def test_if_prime_is_five(self):
		self.assertTrue(check_prime_numbers(5))

	def test_if_prime_is_ten(self):
		self.assertFalse(check_prime_numbers(10), msg = 'Ten is not a prime')

	def test_if_prime_is_zero(self):
		self.assertFalse(check_prime_numbers(0))

	def test_if_prime_is_negative(self):
                self.assertFalse(check_prime_numbers(-6))
