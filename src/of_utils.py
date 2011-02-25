"""Module with some useful functions used by Open Formula"""

#Import from Open Formula
from of_class import Number, CellReference, RangeReference, LogicalExpression

#Functions that verify types
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
