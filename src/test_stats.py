import unittest

from objects import RangeReference
from stats import MAX, MIN, AVERAGE, SUMPRODUCT


class TestOpenFormulaFunctions(unittest.TestCase):

#Statistics functions
    def test_of_max(self):
        self.assertEqual(MAX(RangeReference("[.A1:.B2]")), "MAX([.A1:.B2])")
	self.assertEqual(MAX(RangeReference("[.A1:.B2]"),
                    RangeReference("[.C3:.D4]")), "MAX([.A1:.B2] ; [.C3:.D4])")

        self.assertRaises(TypeError, MAX, 2)

    def test_of_min(self):
        self.assertEqual(MIN(RangeReference("[.A1:.B2]")), "MIN([.A1:.B2])")
	self.assertEqual(MIN(RangeReference("[.A1:.B2]"),
                    RangeReference("[.C3:.D4]")), "MIN([.A1:.B2] ; [.C3:.D4])")

        self.assertRaises(TypeError, MIN, 2)

    def test_of_average(self):
	self.assertEqual(AVERAGE(RangeReference("[.A1:.B2]")),
                                                          "AVERAGE([.A1:.B2])")

	self.assertEqual(AVERAGE(RangeReference("[.A1:.B2]"),
                RangeReference("[.C3:.D4]")), "AVERAGE([.A1:.B2] ; [.C3:.D4])")

        self.assertRaises(TypeError, AVERAGE, 2)

    def test_of_sumproduct(self):
	self.assertEqual(SUMPRODUCT(RangeReference("[.A1:.B2]")),
                                                       "SUMPRODUCT([.A1:.B2])")

	self.assertEqual(SUMPRODUCT(RangeReference("[.A1:.B2]"),
             RangeReference("[.C3:.D4]")), "SUMPRODUCT([.A1:.B2] ; [.C3:.D4])")

        self.assertRaises(TypeError, SUMPRODUCT, 2)

if __name__ == '__main__':
    unittest.main()


                          


                          
