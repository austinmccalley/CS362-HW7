import unittest
from lp import leapYear

class test_leapYear(unittest.TestCase):
  def testDiv4(self):
    self.assertTrue(leapYear('1640'))
  