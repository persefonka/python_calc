import unittest
from main import calc

class Testconvert_calc(unittest.TestCase):
    def test_area(self):
        self.assertEquals(calc(1.0,2.0,"+"),(3.0))
        self.assertEquals(calc(-1.0, -2.0, "+"), (-3.0))
        self.assertEquals(calc(1.0, 2.0, "*"), (2.0))
        self.assertEquals(calc(-1.0, -2.0, "*"), (2.0))
        self.assertEquals(calc(-1.0, 0, "/"), ("На ноль делить нельзя"))


    def test_values(self):
        self.assertRaises(ValueError,calc( 1.0,0,"/"))
       # self.assertRaises(ValueError, convert_string_to_array, "--1")
        #self.assertRaises(ValueError, convert_string_to_array, " ")
       # self.assertRaises(ValueError, convert_string_to_array, "")
        #дает значение из ковычек на вход функции и проверяет что выдает именно valueerror(их может быть много разных типов)



