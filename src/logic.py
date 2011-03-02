"""
Module that gives logicals operations for syntax formula
Operations like AND, OR, IF etc...
"""

#Import from Open Formula
from utils import is_logical_list
from objects import LogicalExpression, Number, CellReference


#Private API
def __logical_operations(function, *expression_list):
   """
   Generic Implementation that gives the syntax for a logical operation

   Arguments :
       function -- str
       expression_list -- LogicalExpression
   """
   if type(function) is str and is_logical_list(expression_list):
      parameter = " ; ".join(str(i) for i in expression_list)
      return LogicalExpression(function.upper()+"("+parameter+")")
   else:
      raise TypeError, "Arguments must be LogicalExpressions"

#Public API
def AND(*expression_list):
    """Return the syntax for an "and"  """
    return __logical_operations("AND", *expression_list)

def OR(*expression_list):
    """Return the syntax for an "or" """
    return __logical_operations("OR", *expression_list)

def TRUE():
    """Return the value true included in the open formula syntax """
    return LogicalExpression("TRUE()")

def FALSE():
    """Return the value false included in the open formula syntax """
    return LogicalExpression("FALSE()")

def NOT(expression):
    """Return the syntax for a "not" expression  """
    if type(expression) is LogicalExpression:
        return LogicalExpression("NOT("+str(expression)+")")
    else:
        raise TypeError, "Argument must be a LogicalExpression"

def IF(test, then, otherwise):
    """
    Return the syntax for an if

    Arguments :
        test --LogicalExpression
        then --str or Number or CellReference
        otherwise --str or Number or CellReference
    """
    if type(test) is LogicalExpression and type(then) in (Number,
       CellReference, str) and type(otherwise) in (Number, CellReference, str):

        expression = "IF("+str(test)+";"
        if type(then)==str:
            expression = expression+then+";"
        else:
            expression = expression+str(then)+";"
        if type(otherwise)==str:
            expression = expression+otherwise+")"
        else:
            expression = expression+str(otherwise)+")"

        return expression
    else:
        raise TypeError, "Wrong type of argument"
