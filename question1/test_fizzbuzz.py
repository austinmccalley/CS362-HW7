import unittest
from fizz import fizzBuzz


class test_FizzBuzz(unittest.TestCase):
    def testFizz(self):
        for i in [3**1, 3**2, 3**3, 3**4, 3**5, 3**6]:
            self.assertEqual(fizzBuzz(i), 'Fizz')

    def testBuzz(self):
        for i in [5**1, 5**2, 5**3, 5**4, 5**5]:
            self.assertEqual(fizzBuzz(i), 'Buzz')

    def testFizzBuzz(self):
        for i in [5*3 * 1, 5 * 3 * 2, 5 * 3 * 3, 5 * 3 * 4]:
            self.assertEqual(fizzBuzz(i), 'FizzBuzz')