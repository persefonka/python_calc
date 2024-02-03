import unittest
from main import calc
class Testcalc(unittest.TestCase):
    def test_area(self):
        self.assertEquals(calc(1,2,'+'), (3))