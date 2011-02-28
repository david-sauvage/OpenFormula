"""
Module with classes useful for open formula
These classes are used to see what types of string we have
"""
class OFObject(object):
   def __init__(self, value):
       self.str = str(value)

   def __str__(self):
       return self.str

class Number(OFObject):
    pass

class Cell(OFObject):
    pass

class Range(OFObject):
    pass

class CellReference(OFObject):
    pass

class RangeReference(OFObject):
    pass

class Column(OFObject):
    pass

class Row(OFObject):
    pass

class LogicalExpression(OFObject):
    pass
