import unittest
from lp import leapYear

class test_leapYear(unittest.TestCase):
  def testDiv4(self):
    self.assertTrue(leapYear('1640'))

  def testDiv4Except(self):
    self.assertFalse(leapYear('2100'))

  def testDiv100(self):
    self.assertTrue(leapYear('2000'))