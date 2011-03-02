import unittest

from decimal import Decimal
from objects import Number, Cell, Range
from syntax import Formula, number, string
from syntax import parameter_list, reference, column, row
from syntax import range_address, reference_list, array
from syntax import function_name, source, matrix_row

class TestOpenFormulaSyntax(unittest.TestCase):
    
#Syntax test
    def test_of_formula(self):
        expected = "of:= SUM([.A1:.A2])"
        self.assertEqual(Formula("SUM([.A1:.A2])"), expected)
        expected = "of:== SUM([.A1:.A2])"
        self.assertEqual(Formula("SUM([.A1:.A2])", forcerecalc=True), expected)

    def test_of_number(self):
        self.assertEqual(number(5).str, "5")
        self.assertEqual(number(5.5).str, "5.5")
        d = Decimal("5.5e55")
        self.assertEqual(number(d).str, "5.5E+55")
        self.assertRaises(TypeError, number, "a")

    def test_of_string(self):
        self.assertEqual(string("abc"), "abc")
        self.assertRaises(TypeError, string, 5)

    def test_of_function_name(self):
        self.assertEqual(function_name("Product"), "Product")
        self.assertEqual(function_name("Abc._12A"), "Abc._12A")
        self.assertRaises(ValueError, function_name, "5Sum")
        self.assertRaises(TypeError, function_name, 5)

    def test_of_parameter_list(self):
	self.assertEqual(parameter_list("abc", "def", "ghi"),"abc ; def ; ghi")
        self.assertEqual(parameter_list("abc", "", "ghi"), "abc ;  ; ghi")
        self.assertEqual(parameter_list("abc"), "abc")
        self.assertRaises(TypeError, parameter_list, "abc", 2, "def")

    def test_of_reference(self):
        expected="['src'# address]"
	self.assertEqual(reference(Cell("address"), source("src")).str,
                                                                      expected)
	self.assertEqual(reference(Range("address"), source("src")).str,
                                                                      expected)
        self.assertRaises(TypeError, reference, Number("address"))

    def test_of_column(self):
        self.assertEqual(column("AB").str, "AB")
        self.assertEqual(column("AB", True).str, "$AB")
        self.assertRaises(ValueError, column, "A1B")
        self.assertRaises(TypeError, column, 8)

    def test_of_row(self):
        self.assertEqual(row(55).str, "55")
        self.assertEqual(row("55", True).str, "$55")
        self.assertEqual(row(55, True).str, "$55")
        self.assertRaises(ValueError, row, "5A5")
        self.assertRaises(TypeError, row, 8.5)

    def test_of_source(self):
        self.assertEqual(source("test"), "'test'#")
        self.assertRaises(TypeError, source, 8)

    def test_of_range_address(self):
        expected=".AA11"
	self.assertEqual(range_address(column("AA"), row(11)).str, expected)

        expected="sheet.AA11"
	self.assertEqual(range_address("sheet", column("AA"),
                                                     row(11)).str, expected)

        expected=".AA11:.BB22"
	self.assertEqual(range_address(column("AA"), row(11),
                                    column("BB"), row(22)).str, expected)

        expected="sheet.AA11:sheet2.BB22"
	self.assertEqual(range_address("sheet", column("AA"),
               row(11),"sheet2", column("BB"), row(22)).str, expected)
        
        expected=".AA11:.BB22"
	self.assertEqual(range_address(column("AA"), row(11),
                                    column("BB"), row(22)).str, expected)

        self.assertRaises(TypeError, range_address,"A", 1)

    def test_of_reference_list(self):
	self.assertEqual(reference_list("abc", "def", "ghi"), 
                                                             "abc ~ def ~ ghi")

        self.assertEqual(reference_list("abc"), "abc")
        self.assertRaises(TypeError, reference_list, "abc", 2, "def")

    def test_of_array(self):
        self.assertEqual(array("abc", "def", "ghi"), "{abc|def|ghi}")
        self.assertEqual(array("abc"), "{abc}")
        self.assertRaises(TypeError, array, "abc", 2, "def")

    def test_of_matrix_row(self):
        self.assertEqual(matrix_row("abc", "def", "ghi"), "abc;def;ghi")
        self.assertEqual(matrix_row("abc"), "abc")
        self.assertRaises(TypeError, matrix_row, "abc", 2, "def")

if __name__ == '__main__':
    unittest.main()
