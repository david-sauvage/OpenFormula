"""Module with some useful functions used by Open Formula"""

# Import from Open Formula
from objects import Number, CellReference, RangeReference, LogicalExpression

#
# Internal helpers
#
def __num_list_function(function, *number_list):
   """
   Generic implementation the syntax for simple function with many arguments 
   like FUNCTION(num1, num2, num3, etc...)

   Arguments :
       function -- str
       number -- Number or CellReference or RangeReference
   """
   if type(function) is str and is_num_range_list(number_list):
      parameter = ""
      for i in number_list:
         parameter = parameter+str(i)+" ; "
      return function.upper()+"("+parameter[0:-3]+")"
   else:
      raise TypeError, "Arguments must be Numbers or CellReferences"

#
# Functions that verify types
#
def is_number_list(arg):
    """
    Verify if all classes present in the list are Numbers or CellReferences
    """
    for i in arg:
        if not isinstance(i, (Number, CellReference)):
            return False
    return True

def is_string_list(arg):
    """
    Verify if all classes present in the list are Strings or CellReferences
    """
    for i in arg:
        if not isinstance(i, (str, CellReference)):
            return False
    return True

def is_str_num_list(arg):
    """
    Verify if all classes present in the list are 
    Strings, Numbers or CellReferences
    """
    for i in arg:
        if not isinstance(i, (str, Number, CellReference)):
            return False
    return True

def is_num_range_list(arg):
    """
    Verify if all classes present in the list are 
    Numbers, CellReferences or RangeReferences
    """
    for i in arg:
        if not isinstance(i, (Number, CellReference, RangeReference)):
            return False
    return True

def is_logical_list(arg):
    """Verify if all classes present in the list are LogicalExpressions"""
    for i in arg:
        if not isinstance(i, LogicalExpression):
            return False
    return True
