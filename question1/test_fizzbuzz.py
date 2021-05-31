import unittest
from fizz import fizzBuzz


class test_FizzBuzz(unittest.TestCase):
    def testFizz(self):
        for i in [3**1, 3**2, 3**3, 3**4, 3**5, 3**6]:
          self.assertEqual(fizzBuzz(i), 'Fizz')
