import unittest

from objects import LogicalExpression, Number
from logic import AND, OR, TRUE, FALSE, NOT, IF

class TestOpenFormulaFunctions(unittest.TestCase):
    
#Logicals operations
    def test_of_and(self):
        self.assertEqual(AND(LogicalExpression("1>2")).str, "AND(1>2)")
	self.assertEqual(AND(LogicalExpression("2=2"),
                                LogicalExpression("3>2")).str, "AND(2=2 ; 3>2)")

        self.assertRaises(TypeError, AND, 2, 3)

    def test_of_or(self):
        self.assertEqual(OR(LogicalExpression("1>2")).str, "OR(1>2)")
	self.assertEqual(OR(LogicalExpression("2=2"),
                                 LogicalExpression("3>2")).str, "OR(2=2 ; 3>2)")

        self.assertRaises(TypeError, OR, 2, 3)

    def test_of_true(self):
        self.assertEqual(TRUE().str, "TRUE()")

    def test_of_false(self):
        self.assertEqual(FALSE().str, "FALSE()")

    def test_of_not(self):
        self.assertEqual(NOT(LogicalExpression("1>2")).str, "NOT(1>2)")
        self.assertRaises(TypeError, NOT, 2)

    def test_of_if(self):
	self.assertEqual(IF(LogicalExpression("1>2"), Number("3"),
                                                    Number("4")), "IF(1>2;3;4)")

        self.assertRaises(TypeError, IF, "1>2", 1, 2)

if __name__ == '__main__':
    unittest.main()


                          


                          
