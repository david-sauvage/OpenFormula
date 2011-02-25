import unittest

from of_class import LogicalExpression, Number
from of_logicals_op import of_and, of_or, of_true, of_false, of_not, of_if

class TestOpenFormulaFunctions(unittest.TestCase):
    
#Logicals operations
    def test_of_and(self):
        self.assertEqual(of_and(LogicalExpression("1>2")).str, "AND(1>2)")
	self.assertEqual(of_and(LogicalExpression("2=2"),
                                LogicalExpression("3>2")).str, "AND(2=2 ; 3>2)")

        self.assertRaises(TypeError, of_and, 2, 3)

    def test_of_or(self):
        self.assertEqual(of_or(LogicalExpression("1>2")).str, "OR(1>2)")
	self.assertEqual(of_or(LogicalExpression("2=2"),
                                 LogicalExpression("3>2")).str, "OR(2=2 ; 3>2)")

        self.assertRaises(TypeError, of_or, 2, 3)

    def test_of_true(self):
        self.assertEqual(of_true().str, "TRUE()")

    def test_of_false(self):
        self.assertEqual(of_false().str, "FALSE()")

    def test_of_not(self):
        self.assertEqual(of_not(LogicalExpression("1>2")).str, "NOT(1>2)")
        self.assertRaises(TypeError, of_or, 2)

    def test_of_if(self):
	self.assertEqual(of_if(LogicalExpression("1>2"), Number("3"),
                                                    Number("4")), "IF(1>2;3;4)")

        self.assertRaises(TypeError, of_if, "1>2", 1, 2)

if __name__ == '__main__':
    unittest.main()


                          


                          
