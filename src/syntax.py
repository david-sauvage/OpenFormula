"""
Module that permits to get a string compatible
with the syntax of open formula
"""
#Import from the Standard Library
from re import compile, match
from decimal import Decimal

#Import from
from objects import Number, Cell, Range, CellReference, RangeReference
from objects import Column, Row

function_name_pattern = compile("^[A-Za-z_.1-9]*$")

def Formula(expression, forcerecalc=False):
    """
    Return the syntax for a formula
    An open formula must begin with "of:"
    """
    intro = "==" if forcerecalc else "="
    return "of:" + intro + " " + expression

def number(num):
    """Verify that the argument is a  number and returns it in a string"""
    if type(num) in (int, long, float, Decimal):
        return Number(num)
    else:
        raise TypeError, 'Unknown type "%s"' % type(num)

def string(string):
    """Verify the argument is a string"""
    if type(string)==str:
        return string
    else:
        raise TypeError, "Not a string"

def function_name(name):
    """Verify if name is valid for the openformula syntax"""
    if type(name) == str:
        if name[0].isalpha() and match(function_name_pattern, name) is not None:
            return name
        else:
            raise ValueError, "Does not match the pattern"
    else:
        raise TypeError, "Not a string"

def parameter_list(*parameters):
    """Return the syntax for a parameter list"""
    return ' ; '.join(parameters)

def reference(range_address, source=None):
    """Return the syntax for a reference"""
    reference = str(range_address)
    if source is not None:
        reference = source + " " +  reference
    reference = "[" + reference + "]"
    if type(range_address) is Cell:
        return CellReference(reference)
    elif type(range_address) is Range:
        return RangeReference(reference)
    else:
        raise TypeError, "Not a Cell or Range"

def column(col, blocked=False):
    """Verify that col is an alphanumeric character and returns it"""
    if type(col) is str:
        if col.isalpha():
            if blocked:
                return Column("$"+col.upper())
            else:
                return Column(col)
        else:
            raise ValueError, "A column is an alphanumeric character"
    else:
        raise TypeError, "Not a string"

def row(row, blocked=False):
    """
    Verify that row is a number and returns it
    in a string
    """
    if type(row) is int:
        row = str(row)

    if type(row) is str:
        if row.isdigit():
            if blocked:
                return Row("$"+row)
            else:
                return Row(row)
        else:
            raise ValueError, "A row is a number"
    else:
        raise TypeError, "Not a string"

def source(iri):
    """Return the syntax for a source"""
    if type(iri) is str:
        return "'"+iri+"'#"
    else:
        raise TypeError, "Not a string"

def range_address(*args):
    """
    Return the syntax for a range address. Examples:

    >>> range_address(col1, row1)
    >>> range_address(sheet1, col1, row1)
    >>> range_address(col1, row1, col2, row2)
    >>> range_address(sheet1, col1, row1, col2, row2)
    >>> range_address(sheet1, col1, row1, sheet2, col2, row2)
    """

    if len(args) == 2:
        if type(args[0]) is Column and type(args[1]) is Row:
            return Range(".%s%s" % args)
        else:
            raise TypeError, "Arguments must be a Column and a Row"

    elif len(args) == 3:
        if type(args[1]) is Column and type(args[2]) is Row:
            return Range("%s.%s%s" % args)
        else:
            raise TypeError, "Arguments must be a sheet a Column and a Row"

    elif len(args) == 4:
	if (type(args[0]) is Column and type(args[1]) is Row and type(args[2])
                                           is Column and type(args[3]) is Row):
            return Range(".%s%s:.%s%s" % args)
        else:
            raise TypeError, "Arguments must be : Column, Row, Column, Row"

    elif len(args) == 5:
	if (type(args[1]) is Column and type(args[2]) is Row and type(args[3])
                                           is Column and type(args[4]) is Row):
            return Range("%s.%s%s:.%s%s" % args)
        else:
            return TypeError, """Arguments must be : 
                                 Sheet, Column, Row, Column, Row"""

    elif len(args) == 6:
	if (type(args[1]) is Column and type(args[2]) is Row and type(args[4])
                                            is Column and type(args[5]) is Row):
            return Range("%s.%s%s:%s.%s%s" % args)
        else:
            return TypeError, """Arguments must be : 
                                 Sheet, Column, Row, Sheet, Column, Row"""

    raise ValueError, "Incorrect number of arguments"


def reference_list(*references):
    """Return the syntax for a reference list"""
    return ' ~ '.join(references)

def array(*matrix_rows):
    """Return the syntax for an array"""
    return "{" + "|".join(matrix_rows) + "}"

def matrix_row(*expressions):
    """Return the syntax for a matrix row"""
    return ";".join(expressions)
