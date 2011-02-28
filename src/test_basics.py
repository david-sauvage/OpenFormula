import unittest

from objects import CellReference, Number
from basics import of_add, of_substract, of_multiply, of_divide
from basics import of_concatenate, of_equal, of_different, of_upper
from basics import of_lower, of_upper_equal, of_lower_equal

class TestOpenFormulaBasicsOp(unittest.TestCase):
    
#Basics operations
    def test_of_add(self):
        self.assertEqual(of_add(CellReference("[.A1]")), "[.A1]")
        self.assertEqual(of_add(Number("2"), CellReference("[.D4]")), "2+[.D4]")
        self.assertRaises(TypeError, of_add, 2)

    def test_of_substract(self):
        self.assertEqual(of_substract(CellReference("[.A1]")), "[.A1]")
	self.assertEqual(of_substract(Number("2"), CellReference("[.D4]")),
                                                                      "2-[.D4]")

        self.assertRaises(TypeError, of_substract, 2)
   
    def test_of_multiply(self):
        self.assertEqual(of_multiply(CellReference("[.A1]")), "[.A1]")
	self.assertEqual(of_multiply(Number("2"), CellReference("[.D4]")),
                                                                      "2*[.D4]")

        self.assertRaises(TypeError, of_multiply, 2)

    def test_of_divide(self):
        self.assertEqual(of_divide(CellReference("[.A1]")), "[.A1]")
	self.assertEqual(of_divide(Number("2"), CellReference("[.D4]")),
                                                                      "2/[.D4]")

        self.assertRaises(TypeError, of_divide, 2)

    def test_of_concatenate(self):
        self.assertEqual(of_concatenate("abc"), "abc")
        self.assertEqual(of_concatenate("abc","def","ghi"),"abc&def&ghi")
        self.assertRaises(TypeError, of_concatenate, 2)

    def test_of_equal(self):
        self.assertEqual(of_equal("abc").str, "abc")
        self.assertEqual(of_equal("abc","def","ghi").str,"abc=def=ghi")
        self.assertEqual(of_equal(Number("2"), Number("3")).str,"2=3")
        self.assertRaises(TypeError, of_equal, 2) 

    def test_of_different(self):
        self.assertEqual(of_different("abc").str, "abc")
        self.assertEqual(of_different("abc","def","ghi").str,"abc<>def<>ghi")
        self.assertEqual(of_different(Number("2"), Number("3")).str,"2<>3")
        self.assertRaises(TypeError, of_different, 2) 

    def test_of_upper(self):
        self.assertEqual(of_upper("abc").str, "abc")
        self.assertEqual(of_upper("abc","def","ghi").str,"abc>def>ghi")
        self.assertEqual(of_upper(Number("2"), Number("3")).str,"2>3")
        self.assertRaises(TypeError, of_different, 2) 

    def test_of_lower(self):
        self.assertEqual(of_lower("abc").str, "abc")
        self.assertEqual(of_lower("abc","def","ghi").str,"abc<def<ghi")
        self.assertEqual(of_lower(Number("2"), Number("3")).str,"2<3")
        self.assertRaises(TypeError, of_lower, 2) 

    def test_of_upper_equal(self):
        self.assertEqual(of_upper_equal("abc").str, "abc")
        self.assertEqual(of_upper_equal("abc","def","ghi").str,"abc>=def>=ghi")
        self.assertEqual(of_upper_equal(Number("2"), Number("3")).str,"2>=3")
        self.assertRaises(TypeError, of_different, 2) 

    def test_of_lower_equal(self):
        self.assertEqual(of_lower_equal("abc").str, "abc")
        self.assertEqual(of_lower_equal("abc","def","ghi").str,"abc<=def<=ghi")
        self.assertEqual(of_lower_equal(Number("2"), Number("3")).str,"2<=3")
        self.assertRaises(TypeError, of_lower_equal, 2) 

if __name__ == '__main__':
    unittest.main()
