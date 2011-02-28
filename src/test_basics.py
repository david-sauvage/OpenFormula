import unittest

from objects import CellReference, Number
from basics import add, sub, mul, div
from basics import concatenate, eq, ne, gt
from basics import lt, ge, le

class TestOpenFormulaBasicsOp(unittest.TestCase):
    
#Basics operations
    def test_of_add(self):
        self.assertEqual(add(CellReference("[.A1]")), "[.A1]")
        self.assertEqual(add(Number("2"), CellReference("[.D4]")), "2+[.D4]")
        self.assertRaises(TypeError, add, 2)

    def test_of_substract(self):
        self.assertEqual(sub(CellReference("[.A1]")), "[.A1]")
	self.assertEqual(sub(Number("2"), CellReference("[.D4]")),
                                                                      "2-[.D4]")

        self.assertRaises(TypeError, sub, 2)
   
    def test_of_multiply(self):
        self.assertEqual(mul(CellReference("[.A1]")), "[.A1]")
	self.assertEqual(mul(Number("2"), CellReference("[.D4]")),
                                                                      "2*[.D4]")

        self.assertRaises(TypeError, mul, 2)

    def test_of_divide(self):
        self.assertEqual(div(CellReference("[.A1]")), "[.A1]")
	self.assertEqual(div(Number("2"), CellReference("[.D4]")),
                                                                      "2/[.D4]")

        self.assertRaises(TypeError, div, 2)

    def test_of_concatenate(self):
        self.assertEqual(concatenate("abc"), "abc")
        self.assertEqual(concatenate("abc","def","ghi"),"abc&def&ghi")
        self.assertRaises(TypeError, concatenate, 2)

    def test_of_equal(self):
        self.assertEqual(eq("abc").str, "abc")
        self.assertEqual(eq("abc","def","ghi").str,"abc=def=ghi")
        self.assertEqual(eq(Number("2"), Number("3")).str,"2=3")
        self.assertRaises(TypeError, eq, 2) 

    def test_of_different(self):
        self.assertEqual(ne("abc").str, "abc")
        self.assertEqual(ne("abc","def","ghi").str,"abc<>def<>ghi")
        self.assertEqual(ne(Number("2"), Number("3")).str,"2<>3")
        self.assertRaises(TypeError, ne, 2) 

    def test_of_upper(self):
        self.assertEqual(gt("abc").str, "abc")
        self.assertEqual(gt("abc","def","ghi").str,"abc>def>ghi")
        self.assertEqual(gt(Number("2"), Number("3")).str,"2>3")
        self.assertRaises(TypeError, gt, 2) 

    def test_of_lower(self):
        self.assertEqual(lt("abc").str, "abc")
        self.assertEqual(lt("abc","def","ghi").str,"abc<def<ghi")
        self.assertEqual(lt(Number("2"), Number("3")).str,"2<3")
        self.assertRaises(TypeError, lt, 2) 

    def test_of_upper_equal(self):
        self.assertEqual(ge("abc").str, "abc")
        self.assertEqual(ge("abc","def","ghi").str,"abc>=def>=ghi")
        self.assertEqual(ge(Number("2"), Number("3")).str,"2>=3")
        self.assertRaises(TypeError, ge, 2) 

    def test_of_lower_equal(self):
        self.assertEqual(le("abc").str, "abc")
        self.assertEqual(le("abc","def","ghi").str,"abc<=def<=ghi")
        self.assertEqual(le(Number("2"), Number("3")).str,"2<=3")
        self.assertRaises(TypeError, le, 2) 

if __name__ == '__main__':
    unittest.main()
