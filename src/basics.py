"""
Modules that will give basics operations for open formula
(Operations like add substract or comparison like equal, upper etc...)
"""
#Import from Open Formula
from objects import LogicalExpression
from utils import is_number_list, is_str_num_list, is_string_list


#Private API
def __basic_operation(operator, *number_list):
   """
   Generic implementation that gives the syntax for a basic operation

   Arguments :
       operator -- str
       number_list -- Number or CellReference

   """
   if type(operator) is str and is_number_list(number_list):
      return operator.join(str(i) for i in number_list)
   else:
      raise TypeError, "Arguments must be Numbers or CellReferences"

def __basic_comparison(operator, *arguments_list):
   """
   Generic implementation that gives the syntax for a basic comparison
      
   Arguments :
       operator  --str
       arguments_list --str or Number or CellReference 
   """
   if type(operator) is str and is_str_num_list(arguments_list):
      expression = operator.join(str(i) for i in arguments_list)
      return LogicalExpression(expression)
   else:
      raise TypeError, "Arguments must be Numbers, strings or CellReferences"

#Public API
def of_add(*number_list):
    """Verify arguments and return a string for an "add" expression """
    return __basic_operation("+", *number_list)

def of_substract(*number_list):
    """Verify arguments and return a string for a "substract" expression """
    return __basic_operation("-", *number_list)

def of_multiply(*number_list):
    """Verify arguments and return a string for a "multiply" expression """
    return __basic_operation("*", *number_list)

def of_divide(*number_list):
    """Verify arguments and return a string for a "divide" expression """
    return __basic_operation("/", *number_list)

def of_concatenate(*string_list):
    """Verify arguments and return a string for a "concatenate" expression """
    if is_string_list(string_list):
        return "&".join(str(i) for i in string_list)
    else:
        raise TypeError, "Arguments must be strings"

def of_equal(*arguments_list):
    """Verify arguments and return a string for an "equal (=)" expression """
    return __basic_comparison("=", *arguments_list)

def of_different(*arguments_list):
    """Verify arguments and return a string for an "different (<>)" expression """
    return __basic_comparison("<>", *arguments_list)

def of_upper(*arguments_list):
    """Verify arguments and return a string for an "upper (>)" expression """
    return __basic_comparison(">", *arguments_list)

def of_lower(*arguments_list):
    """Verify arguments and return a string for an "lower (<)" expression """
    return __basic_comparison("<", *arguments_list)

def of_upper_equal(*arguments_list):
    """Verify arguments and return a string for an "upper or equal (>=)" expression """
    return __basic_comparison(">=", *arguments_list)

def of_lower_equal(*arguments_list):
    """Verify arguments and return a string for an "lower or equal (<=)" expression """
    return __basic_comparison("<=", *arguments_list)
