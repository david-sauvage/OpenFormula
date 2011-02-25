import unittest

from of_class import RangeReference
from of_stats import of_max, of_min, of_average, of_sumproduct


class TestOpenFormulaFunctions(unittest.TestCase):

#Statistics functions
    def test_of_max(self):
        self.assertEqual(of_max(RangeReference("[.A1:.B2]")), "MAX([.A1:.B2])")
	self.assertEqual(of_max(RangeReference("[.A1:.B2]"),
                    RangeReference("[.C3:.D4]")), "MAX([.A1:.B2] ; [.C3:.D4])")

        self.assertRaises(TypeError, of_max, 2)

    def test_of_min(self):
        self.assertEqual(of_min(RangeReference("[.A1:.B2]")), "MIN([.A1:.B2])")
	self.assertEqual(of_min(RangeReference("[.A1:.B2]"),
                    RangeReference("[.C3:.D4]")), "MIN([.A1:.B2] ; [.C3:.D4])")

        self.assertRaises(TypeError, of_min, 2)

    def test_of_average(self):
	self.assertEqual(of_average(RangeReference("[.A1:.B2]")),
                                                          "AVERAGE([.A1:.B2])")

	self.assertEqual(of_average(RangeReference("[.A1:.B2]"),
                RangeReference("[.C3:.D4]")), "AVERAGE([.A1:.B2] ; [.C3:.D4])")

        self.assertRaises(TypeError, of_average, 2)

    def test_of_sumproduct(self):
	self.assertEqual(of_sumproduct(RangeReference("[.A1:.B2]")),
                                                       "SUMPRODUCT([.A1:.B2])")

	self.assertEqual(of_sumproduct(RangeReference("[.A1:.B2]"),
             RangeReference("[.C3:.D4]")), "SUMPRODUCT([.A1:.B2] ; [.C3:.D4])")

        self.assertRaises(TypeError, of_sumproduct, 2)

if __name__ == '__main__':
    unittest.main()


                          


                          
