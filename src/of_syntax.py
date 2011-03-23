"""
Module that permits to get a string compatible
with the syntax of open formula
"""
#Import from the Standard Library
from re import compile, match
from decimal import Decimal

#Import from
from of_class import Number, Cell, Range, CellReference, RangeReference
from of_class import Column, Row

function_name_pattern = compile("^[A-Za-z_.1-9]*$")

#
#Private API
#

def __get_an_address(arg):
    """
    arg - str
    Verify the format of the cell
    and add a '.' when it is necessary
    """
    if arg.count('.') == 1: #if it's like "sheet.A1"
        split = arg.split('.')
        return split[0]+'.'+__verify_cell(split[1])
    elif arg.count('.') == 0:  #if it's just like "A1"
        return '.'+__verify_cell(arg)
    else:
        raise ValueError, "Not a valid range address"

def __verify_cell(arg):
    """
    arg - str
    Verify that arg correspond to a cell
    """
    col = ''
    for c in arg:
        if c.isalpha():
            col += c
        else:
            break
    row = int(arg[len(col):])
    return str(of_column(col))+str(of_row(row))

#
#Public API
#

def of_formula(intro, expression):
    """
    Return the syntax for a formula
    An open formula must begin with "of:"
    """
    return "of:"+intro+" "+expression

def of_intro(forcerecalc=False):
    """Return the syntax for an intro"""
    if forcerecalc:
        return "=="
    else:
        return "="

def of_number(num):
    """Verify that the argument is a  number and returns it in a string"""
    if type(num) in (int, long, float, Decimal):
        return Number(num)
    else:
        raise TypeError, 'Unknown type "%s"' % type(num)

def of_string(string):
    """Verify the argument is a string"""
    if type(string)==str:
        return string
    else:
        raise TypeError, "Not a string"

def of_function_name(name):
    """Verify if name is valid for the openformula syntax"""
    if type(name) == str:
        if name[0].isalpha() and match(function_name_pattern, name) is not None:
            return name
        else:
            raise ValueError, "Does not match the pattern"
    else:
        raise TypeError, "Not a string"

def of_parameter_list(*parameters):
    """Return the syntax for a parameter list"""
    return ' ; '.join(parameters)

def of_reference(range_address, source=None):
    """Return the syntax for a reference"""
    reference = range_address.str
    if source is not None:
        reference = source + " " +  reference
    reference = "[" + reference + "]"
    if type(range_address) is Cell:
        return CellReference(reference)
    elif type(range_address) is Range:
        return RangeReference(reference)
    else:
        raise TypeError, "Not a Cell or Range"

def of_column(col, blocked=False):
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

def of_row(row, blocked=False):
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

def of_source(iri):
    """Return the syntax for a source"""
    if type(iri) is str:
        return "'"+iri+"'#"
    else:
        raise TypeError, "Not a string"

def of_range_address(*args):
    """
    Return the syntax for a range address. Examples:

    >>> of_range_address(col1, row1)
    >>> of_range_address(sheet1, col1, row1)
    >>> of_range_address(col1, row1, col2, row2)
    >>> of_range_address(sheet1, col1, row1, col2, row2)
    >>> of_range_address(sheet1, col1, row1, sheet2, col2, row2)
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

def of_range_address2(arg):
    """
    Return the syntax for a range address
    arg - string like 'A1', 'A1:B2', 'Sheet.A1:B2 etc...
    """
    
    if type(arg) is str:
        if arg.count(':') == 1: #if it's a table
            split = arg.split(':')
            part1 = __get_an_address(split[0])
            part2 = __get_an_address(split[1])
            return RangeReference('['+part1+':'+part2+"]")
        elif arg.count(':') == 0: #if it's a cell
            return CellReference("["+__get_an_address(arg)+"]")
        else:
            raise ValueError, "Not a valid range address"
    else:
        raise TypeError, "Not a string"

def of_reference_list(*references):
    """Return the syntax for a reference list"""
    return ' ~ '.join(references)

def of_array(*matrix_rows):
    """Return the syntax for an array"""
    return "{" + "|".join(matrix_rows) + "}"

def of_matrix_row(*expressions):
    """Return the syntax for a matrix row"""
    return ";".join(expressions)
