import unittest

from decimal import Decimal
from objects import Number, Cell, Range
from syntax import of_formula, of_intro, of_number, of_string
from syntax import of_parameter_list, of_reference, of_column, of_row
from syntax import of_range_address, of_reference_list, of_array
from syntax import of_function_name, of_source, of_matrix_row
class TestOpenFormulaSyntax(unittest.TestCase):
    
#Syntax test
    def test_of_formula(self):
        expected = "of:= SUM([.A1:.A2])"
        self.assertEqual(of_formula(of_intro(False), "SUM([.A1:.A2])"), expected)
        expected = "of:== SUM([.A1:.A2])"
        self.assertEqual(of_formula(of_intro(True), "SUM([.A1:.A2])"), expected)
        
    def test_of_intro(self):
        expected = "="
        self.assertEqual(of_intro(), expected)
        expected = "=="
        self.assertEqual(of_intro(True), expected)

    def test_of_number(self):
        self.assertEqual(of_number(5).str, "5")
        self.assertEqual(of_number(5.5).str, "5.5")
        d = Decimal("5.5e55")
        self.assertEqual(of_number(d).str, "5.5E+55")
        self.assertRaises(TypeError, of_number, "a")

    def test_of_string(self):
        self.assertEqual(of_string("abc"), "abc")
        self.assertRaises(TypeError, of_string, 5)

    def test_of_function_name(self):
        self.assertEqual(of_function_name("Product"), "Product")
        self.assertEqual(of_function_name("Abc._12A"), "Abc._12A")
        self.assertRaises(ValueError, of_function_name, "5Sum")
        self.assertRaises(TypeError, of_function_name, 5)

    def test_of_parameter_list(self):
	self.assertEqual(of_parameter_list("abc", "def", "ghi"), 
                                                           "abc ; def ; ghi")

        self.assertEqual(of_parameter_list("abc", "", "ghi"), "abc ;  ; ghi")
        self.assertEqual(of_parameter_list("abc"), "abc")
        self.assertRaises(TypeError, of_parameter_list, "abc", 2, "def")

    def test_of_reference(self):
        expected="['src'# address]"
	self.assertEqual(of_reference(Cell("address"), of_source("src")).str,
                                                                      expected)

	self.assertEqual(of_reference(Range("address"), of_source("src")).str,
                                                                      expected)

        self.assertRaises(TypeError, of_reference, Number("address"))

    def test_of_column(self):
        self.assertEqual(of_column("AB").str, "AB")
        self.assertEqual(of_column("AB", True).str, "$AB")
        self.assertRaises(ValueError, of_column, "A1B")
        self.assertRaises(TypeError, of_column, 8)

    def test_of_row(self):
        self.assertEqual(of_row(55).str, "55")
        self.assertEqual(of_row("55", True).str, "$55")
        self.assertEqual(of_row(55, True).str, "$55")
        self.assertRaises(ValueError, of_row, "5A5")
        self.assertRaises(TypeError, of_row, 8.5)

    def test_of_source(self):
        self.assertEqual(of_source("test"), "'test'#")
        self.assertRaises(TypeError, of_source, 8)

    def test_of_range_address(self):
        expected=".AA11"
	self.assertEqual(of_range_address(of_column("AA"), of_row(11)).str,
                                                                      expected)
        
        expected="sheet.AA11"
	self.assertEqual(of_range_address("sheet", of_column("AA"),
                                                     of_row(11)).str, expected)
        
        expected=".AA11:.BB22"
	self.assertEqual(of_range_address(of_column("AA"), of_row(11),
                                    of_column("BB"), of_row(22)).str, expected)
        
        expected="sheet.AA11:sheet2.BB22"
	self.assertEqual(of_range_address("sheet", of_column("AA"),
               of_row(11),"sheet2", of_column("BB"), of_row(22)).str, expected)
        
        expected=".AA11:.BB22"
	self.assertEqual(of_range_address(of_column("AA"), of_row(11),
                                    of_column("BB"), of_row(22)).str, expected)

        self.assertRaises(TypeError, of_range_address,"A", 1)

    def test_of_reference_list(self):
	self.assertEqual(of_reference_list("abc", "def", "ghi"), 
                                                             "abc ~ def ~ ghi")

        self.assertEqual(of_reference_list("abc"), "abc")
        self.assertRaises(TypeError, of_reference_list, "abc", 2, "def")

    def test_of_array(self):
        self.assertEqual(of_array("abc", "def", "ghi"), "{abc|def|ghi}")
        self.assertEqual(of_array("abc"), "{abc}")
        self.assertRaises(TypeError, of_array, "abc", 2, "def")

    def test_of_matrix_row(self):
        self.assertEqual(of_matrix_row("abc", "def", "ghi"), "abc;def;ghi")
        self.assertEqual(of_matrix_row("abc"), "abc")
        self.assertRaises(TypeError, of_matrix_row, "abc", 2, "def")

if __name__ == '__main__':
    unittest.main()
