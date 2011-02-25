"""
Module that gives mathematicals functions of open formula
except for convert, euroconvert and subtotal
"""

#Import from Open Formula
from of_class import Number, CellReference, RangeReference, LogicalExpression
from of_utils import is_num_range_list
from of_syntax import of_parameter_list

#
#Private API
#

def __simple_function(function, number):
   """
   Generic implementation the syntax for simple function like
   FUNCTION(number)
   
   Arguments :
       function -- str
       number -- Number or CellReference
   """
   if type(function) is str and isinstance(number, (Number, CellReference)):
      return function.upper()+"("+number.str+")"
   else:
      raise TypeError, "Argument must be a Number or a CellReference"


def __simple_function2(function, number1, number2):
   """
   Generic implementation the syntax for simple function with two arguments 
   like FUNCTION(number1, number2)
   
   Arguments :
       function -- str
       number -- Number or CellReference
   """
   if (type(function) is str and type(number1) in (Number, CellReference) and 
                                      type(number2) in (Number, CellReference)):
      return function.upper()+"("+of_parameter_list(number1.str,
                                                                number2.str)+")"

   else:
      raise TypeError, "Arguments must be Numbers or CellReferences"

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
         parameter = parameter+i.str+" ; "
      return function.upper()+"("+parameter[0:-3]+")"
   else:
      raise TypeError, "Arguments must be Numbers or CellReferences"

def __round(function, number, count):
   """
   Generic function used by all the round function in open formula

   Arguments :
       function -- str
       number -- Number or CellReference
       count -- None or Number or CellReference
   """
   if count is None:
      if type(function) is str and type(number) in (Number, CellReference):
         return function.upper()+"("+of_parameter_list(number.str)+")"
      else:
         raise TypeError, "Argument must be a Number or a CellReference"
   else:
      if (type(function) is str and type(number) in (Number, CellReference) and 
                                        type(count) in (Number, CellReference)):

	 return function.upper()+"("+of_parameter_list(number.str,
                                                                 count.str)+")"

      else:
         raise TypeError, "Arguments must be Numbers or CellReferences"

def __floor_ceil(function, number, significance, mode):
   """
   Generic function used by ceil & floor function included in open formula

   Arguments
       function -- str 
       number -- Number or CellReference
       significance -- Number or CellRefenrece
       mode -- None or Number or CellReference
   """
   if mode is None:
      if (type(function) is str and type(number) in (Number, CellReference) and 
                                type(significance) in (Number, CellReference)):

	 return function.upper()+"("+of_parameter_list(number.str,
                                                           significance.str)+")"

      else:
         raise TypeError, "Arguments must be Numbers or CellReferences"
   else:
      if (type(function) is str and type(number) in (Number, CellReference) and 
			     type(significance) in (Number, CellReference) and 
                                        type(mode) in (Number, CellReference)):

	 return function.upper()+"("+of_parameter_list(number.str,
                                                 significance.str, mode.str)+")"

      else:
         raise TypeError, "Arguments must be Numbers or CellReferences"

#
#Public API
#

def of_abs(number):
    """Return the syntax for an absolute value """
    return __simple_function("ABS", number)

def of_acos(number):
    """Return the syntax for arccosine """
    return __simple_function("ACOS", number)

def of_acosh(number):
    """Return the syntax for an inverse hyperbolic cosine """
    return __simple_function("ACOSH", number)

def of_acot(number):
    """Return the syntax for an inverse cotangent """
    return __simple_function("ACOT", number)

def of_acoth(number):
    """Return the syntax for an inverse hyperbolic cotangent """
    return __simple_function("ACOTH", number)

def of_asin(number):
    """Return the syntax for an arcsine """
    return __simple_function("ASIN", number)

def of_asinh(number):
    """Return the syntax for an inverse hyperbolic sine """
    return __simple_function("ASINH", number)

def of_atan(number):
    """Return the syntax for a tangent """
    return __simple_function("ATAN", number)

def of_atan2(number1, number2):
    """Return the syntax for a tangent with specified coordonates """
    return __simple_function2("ATAN2", number1, number2)

def of_atanh(number):
    """Return the syntax for an inverse hyperbolic tangent """
    return __simple_function("ATANH", number)

def of_ceiling(number, significance, mode=None):
    """
    Return the syntax for a ceiling
    Rounds a number to the nearest multiple of significance
    """
    return __floor_ceil("CEILING", number, significance, mode)
    
def of_combin(number1, number2):
    """
    Return the syntax for a combination (without repetitions)
    Calculates the number of combinations for elements without repetition
    """
    return __simple_function2("COMBIN", number1, number2)

def of_combina(number1, number2):
    """
    Return the syntax for a combination (with repetitions)
    Calculates the number of combinations for elements including repetition
    """ 
    return __simple_function2("COMBINA", number1, number2)
   
def of_cos(number):
    """Return the syntax for a cosine """
    return __simple_function("COS", number)

def of_cosh(number):
    """Return the syntax for an hyperbolic cosine """
    return __simple_function("COSH", number)

def of_cot(number):
    """Return the syntax for a cotagent """
    return __simple_function("COT", number)

def of_coth(number):
    """Return the syntax for an hyperbolic cotangent """
    return __simple_function("COTH", number)

def of_countblank(cell_range):
    """Return the syntax for a countblank """
    if type(cell_range) in (CellReference, RangeReference):
            return "COUNTBLANK("+cell_range.str+")"
    else:
        raise TypeError, "Argument must be a RangeReference or a CellReference"

def of_countif(cells, criteria):
   """Return the syntax for a countif """
   if (type(cells) in (CellReference, RangeReference) and type(criteria) in 
               (Number, CellReference, RangeReference, LogicalExpression, str)):

      return "COUNTIF("+cells.str+";"+criteria.str+")"
   else:
      raise TypeError, """First argument has to be CellReference or  
			RangeReference, second argument must be Number,  
                        CellReference, RangeReference"""

def of_degrees(number):
    """
    Return the syntax for a degrees
    Convert Radians to Degrees
    """
    return __simple_function("DEGREES", number)

def of_even(number):
    """
    Return the syntax for an even
    Rounds a positive number up and a negative number down
    to the nearest even integer
    """
    return __simple_function("EVEN", number)

def of_exp(number):
    """
    Return the syntax for an exponential
    Calculates the exponent for basis e
    """
    return __simple_function("EXP", number)

def of_fact(number):
    """Return the syntax for an factorial """
    return __simple_function("FACT", number)

def of_floor(number, significance, mode=None):
    """
    Return the syntax for a floor
    Round number down to the nearest multiple of significance
    """
    return  __floor_ceil("FLOOR", number, significance, mode)

def of_gcd(*number_list):
    """Return the syntax for a Greatest Common Divisor """
    return __num_list_function("GCD", *number_list)
 

def of_gcd_add(*number_list):
    """Return the syntax for a Greatest Common Divisor """
    return __num_list_function("GCD_ADD", *number_list)

def of_int(number):
    """
    Return the syntax for an integer function
    Round a number to the nearest integer
    """
    return __simple_function("INT", number)
 
def of_iseven(number):
    """
    Return the syntax for an "iseven"
    Return true if the value is an even integer
    """
    return __simple_function("ISEVEN", number)

def of_isodd(number):
    """Return the syntax for an "isodd"
    Return true if the value is an odd integer
    """
    return __simple_function("ISODD", number)

def of_lcm(*number_list):
    """Return the syntax for a lowest common multiple """
    return __num_list_function("LCM", *number_list)

def of_lcm_add(*number_list):
    """Return the syntax for a lowest common multiple """
    return __num_list_function("LCM_ADD", *number_list)

def of_ln(number):
    """
    Return the syntax for a "ln"
    Calculates the natural logarithm
    """
    return __simple_function("LN", number)

def of_log(number, base):
    """
    Return the syntax for a "log" with the base you want
    Calculates the logarithm to any specified base
    """
    return __simple_function2("LOG", number, base)

def of_log10(number):
    """
    Return the syntax for a "log" in base 10
    Calculates the base 10 logarithm of a number
    """
    return __simple_function("LOG10", number)

def of_mod(dividend, divisor):
    """Return the syntax for a "modulo" """
    return __simple_function2("MOD", dividend, divisor)

def of_mround(number, multiple):
    """
    Return the syntax for a "mround"
    returns the number rounded to a specified multiple
    """
    return __simple_function2("MROUND", number, multiple)

def of_multinomial(*number_list):
    """
    Return the syntax for a "multinomial"
    Return the multinomial coefficient of a set of number
    """
    return __num_list_function("MULTINOMIAL", *number_list)

def of_odd(number):
    """
    Return the syntax for an "odd" 
    Rounds a positive number up and a negative number down
    to the nearest odd integer
    """
    return __simple_function("ODD", number)

def of_pi():
    """Return the syntax in order to get Pi """
    return "PI()"

def of_power(base, exponent):
    """Return the syntax for a power (base^exponent)"""
    return __simple_function2("POWER", base, exponent)

def of_product(*number_list):
    """Return the syntax for a product """
    return __num_list_function("PRODUCT", *number_list)
  
def of_quotient(numerator, denominator):
    """Return the syntax for a quotient """
    return __simple_function2("QUOTIENT", numerator, denominator)

def of_radians(number):
    """
    Return the syntax for a "radians"
    Convert degrees to radians
    """
    return __simple_function("RADIANS", number)

def of_rand():
    """Return the syntax in order to get a random number """
    return "RAND()"

def of_randbetween(bottom, top):
    """
    Return the syntax for a randbetween
    in order to get a random number between bottom and top
    """
    return __simple_function2("RANDBETWEEN", bottom, top)

def of_round(number, count=None):
    """
    Return the syntax for a round
    Rounds a number to a predefined accuracy
    """
    return __round("ROUND", number, count)
  
def of_rounddown(number, count=None):
    """
    Return the syntax for a rounddown
    Rounds down a number to a predefined accuracy
    """
    return __round("ROUNDDOWN", number, count)

def of_roundup(number, count=None):
    """
    Return the syntax for a roundup
    Rounds up a number to a predefined accuracy
    """
    return __round("ROUNDUP", number, count)

def of_seriessum(x, n, m, coeff):
    """
    Return the syntax for a seriessum
    Gives the sum of a power series
    """
    if (type(x) in (Number, CellReference) and  
       type(n) in (Number, CellReference) and 
       type(m) in (Number, CellReference) and 
       type(coeff) in (Number, CellReference, RangeReference)):

	return "SERIESSUM("+of_parameter_list(x.str, n.str, m.str,
                                                                 coeff.str)+")"

    else:
        raise TypeError, "Wrong type of arguments"

def of_sign(number):
    """
    Return the syntax for a "sign" 
    Give the algebraic sign of the number
    """
    return __simple_function("SIGN", number)
  
def of_sin(number):
    """Return the syntax for a sine"""
    return __simple_function("SIN", number)

def of_sinh(number):
    """Return the syntax for an hyperbolic sine"""
    return __simple_function("SINH", number)

def of_sqrt(number):
    """Return the syntax for a square root """
    return __simple_function("SQRT", number)

def of_sqrtpi(number):
    """Return the syntax for a square root * pi """
    return __simple_function("SQRTPI", number)

def of_sum(*number_list):
    """Return the syntax for a sum """
    return __num_list_function("SUM", *number_list)

def of_sumif(cells, criteria, sum_range=None):
   """Return the syntax for a sumif """
   if sum_range is None:
      if (type(cells) in (CellReference, RangeReference) and 
	 type(criteria) in (Number, CellReference, RangeReference,
                                                       LogicalExpression, str)):

         return "SUMIF("+cells.str+";"+criteria.str+")"
      else:
         raise TypeError, "Wrong types of arguments"
   else:
      if (type(cells) in (CellReference, RangeReference) and 
	 type(criteria) in (Number, CellReference, RangeReference,
                                                 LogicalExpression, str) and  
         type(sum_range) in (CellReference, RangeReference)):

         return "SUMIF("+cells.str+";"+criteria.str+";"+sum_range.str+")"
      else:
         raise TypeError, "Wrong types of arguments"

def of_sumsq(*number_list):
    """Return the syntax for a sum of the squares """
    return __num_list_function("SUMSQ", *number_list)

def of_tan(number):
    """Return the syntax for a tangent """
    return __simple_function("TAN", number)
 
def of_tanh(number):
    """Return the syntax for an hyperbolic tangent """
    return __simple_function("TANH", number)

def of_trunc(number, count):
    """Return the syntax for a truncate """
    return __simple_function2("TRUNC", number, count)
