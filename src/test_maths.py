import unittest

from objects import Number, CellReference, RangeReference
from maths import ABS, ACOS, ACOSH, ACOT, ACOTH, ASIN
from maths import ASINH, ATAN, ATAN2, ATANH, CEILING
from maths import COMBIN, COMBINA, COS, COSH, COT, COTH
from maths import COUNTBLANK, COUNTIF, DEGREES, EVEN, EXP
from maths import FACT, FLOOR, GCD, GCD_ADD, INT, ISEVEN
from maths import ISODD, LCM, LCM_ADD, LN, LOG, LOG10, MOD
from maths import MROUND, MULTINOMIAL, ODD, PI, POWER, PRODUCT
from maths import QUOTIENT, RADIANS, RAND, RANDBETWEEN, ROUND
from maths import ROUNDDOWN, ROUNDUP, SERIESSUM, SIGN, SIN, SINH
from maths import SQRT, SQRTPI, SUM, SUMIF, SUMSQ, TAN
from maths import TANH, TRUNC


class TestOpenFormulaMaths(unittest.TestCase):

#Mathematicals functions
    def test_of_abs(self):
        self.assertEqual(ABS(Number("2")), "ABS(2)")
        self.assertEqual(ABS(CellReference("[.A1]")), "ABS([.A1])")
        self.assertRaises(TypeError, ABS, 2)

    def test_of_acos(self):
        self.assertEqual(ACOS(Number("2")), "ACOS(2)")
        self.assertEqual(ACOS(CellReference("[.A1]")), "ACOS([.A1])")
        self.assertRaises(TypeError, ACOS, 2)

    def test_of_acosh(self):
        self.assertEqual(ACOSH(Number("2")), "ACOSH(2)")
        self.assertEqual(ACOSH(CellReference("[.A1]")), "ACOSH([.A1])")
        self.assertRaises(TypeError, ACOSH, 2)

    def test_of_acot(self):
        self.assertEqual(ACOT(Number("2")), "ACOT(2)")
        self.assertEqual(ACOT(CellReference("[.A1]")), "ACOT([.A1])")
        self.assertRaises(TypeError, ACOT, 2) 

    def test_of_acoth(self):
        self.assertEqual(ACOTH(Number("2")), "ACOTH(2)")
        self.assertEqual(ACOTH(CellReference("[.A1]")), "ACOTH([.A1])")
        self.assertRaises(TypeError, ACOTH, 2)    

    def test_of_asin(self):
        self.assertEqual(ASIN(Number("2")), "ASIN(2)")
        self.assertEqual(ASIN(CellReference("[.A1]")), "ASIN([.A1])")
        self.assertRaises(TypeError, ASIN, 2)  

    def test_of_asinh(self):
        self.assertEqual(ASINH(Number("2")), "ASINH(2)")
        self.assertEqual(ASINH(CellReference("[.A1]")), "ASINH([.A1])")
        self.assertRaises(TypeError, ASINH, 2)  

    def test_of_atan(self):
        self.assertEqual(ATAN(Number("2")), "ATAN(2)")
        self.assertEqual(ATAN(CellReference("[.A1]")), "ATAN([.A1])")
        self.assertRaises(TypeError, ATAN, 2)  

    def test_of_atan2(self):
        self.assertEqual(ATAN2(Number("1"), CellReference("[.A1]")), "ATAN2(1 ; [.A1])")
        self.assertRaises(TypeError, ATAN2, 2, 2)

    def test_of_atanh(self):
        self.assertEqual(ATANH(Number("2")), "ATANH(2)")
        self.assertEqual(ATANH(CellReference("[.A1]")), "ATANH([.A1])")
        self.assertRaises(TypeError, ATANH, 2) 

    def test_of_ceiling(self):
        self.assertEqual(CEILING(Number(2), Number(4)), "CEILING(2 ; 4)")
        self.assertEqual(CEILING(Number(1), Number(2), Number(3)), "CEILING(1 ; 2 ; 3)")
        self.assertRaises(TypeError, CEILING, 2, 3)

    def test_of_combin(self):
        self.assertEqual(COMBIN(Number("1"), CellReference("[.A1]")), "COMBIN(1 ; [.A1])")
        self.assertRaises(TypeError, COMBIN, 2, 3)

    def test_of_combina(self):
        self.assertEqual(COMBINA(Number("1"), CellReference("[.A1]")), "COMBINA(1 ; [.A1])")
        self.assertRaises(TypeError, COMBINA, 2, 3)

    def test_of_cos(self):
        self.assertEqual(COS(Number("2")), "COS(2)")
        self.assertEqual(COS(CellReference("[.A1]")), "COS([.A1])")
        self.assertRaises(TypeError, COS, 2)

    def test_of_cosh(self):
        self.assertEqual(COSH(Number("2")), "COSH(2)")
        self.assertEqual(COSH(CellReference("[.A1]")), "COSH([.A1])")
        self.assertRaises(TypeError, COSH, 2)

    def test_of_cot(self):
        self.assertEqual(COT(Number("2")), "COT(2)")
        self.assertEqual(COT(CellReference("[.A1]")), "COT([.A1])")
        self.assertRaises(TypeError, COT, 2)

    def test_of_coth(self):
        self.assertEqual(COTH(Number("2")), "COTH(2)")
        self.assertEqual(COTH(CellReference("[.A1]")), "COTH([.A1])")
        self.assertRaises(TypeError, COTH, 2)

    def test_of_countblank(self):
        self.assertEqual(COUNTBLANK(RangeReference("[.A1:.B2]")), "COUNTBLANK([.A1:.B2])")
        self.assertRaises(TypeError, COUNTBLANK, 2)

    def test_of_countif(self):
        self.assertEqual(COUNTIF(RangeReference("[.A1:.B2]"), Number("3")), "COUNTIF([.A1:.B2];3)")
        self.assertRaises(TypeError, COUNTIF, 2)

    def test_of_degrees(self):
        self.assertEqual(DEGREES(Number("2")), "DEGREES(2)")
        self.assertEqual(DEGREES(CellReference("[.A1]")), "DEGREES([.A1])")
        self.assertRaises(TypeError, DEGREES, 2)

    def test_of_even(self):
        self.assertEqual(EVEN(Number("2")), "EVEN(2)")
        self.assertEqual(EVEN(CellReference("[.A1]")), "EVEN([.A1])")
        self.assertRaises(TypeError, EVEN, 2)

    def test_of_exp(self):
        self.assertEqual(EXP(Number("2")), "EXP(2)")
        self.assertEqual(EXP(CellReference("[.A1]")), "EXP([.A1])")
        self.assertRaises(TypeError, EXP, 2)

    def test_of_fact(self):
        self.assertEqual(FACT(Number("2")), "FACT(2)")
        self.assertEqual(FACT(CellReference("[.A1]")), "FACT([.A1])")
        self.assertRaises(TypeError, FACT, 2)

    def test_of_floor(self):
        self.assertEqual(FLOOR(Number(2), Number(4)), "FLOOR(2 ; 4)")
        self.assertEqual(FLOOR(Number(1), Number(2), Number(3)), "FLOOR(1 ; 2 ; 3)")
        self.assertRaises(TypeError, FLOOR, 2, 3)

    def test_of_gcd(self):
        self.assertEqual(GCD(RangeReference("[.A1:.B2]")), "GCD([.A1:.B2])")
        self.assertEqual(GCD(RangeReference("[.A1:.B2]"), RangeReference("[.C3:.D4]")), "GCD([.A1:.B2] ; [.C3:.D4])")
        self.assertRaises(TypeError, GCD, 2)

    def test_of_gcd_add(self):
        self.assertEqual(GCD_ADD(RangeReference("[.A1:.B2]")), "GCD_ADD([.A1:.B2])")
        self.assertEqual(GCD_ADD(RangeReference("[.A1:.B2]"), RangeReference("[.C3:.D4]")), "GCD_ADD([.A1:.B2] ; [.C3:.D4])")
        self.assertRaises(TypeError, GCD_ADD, 2)

    def test_of_int(self):
        self.assertEqual(INT(Number("2")), "INT(2)")
        self.assertEqual(INT(CellReference("[.A1]")), "INT([.A1])")
        self.assertRaises(TypeError, INT, 2)

    def test_of_iseven(self):
        self.assertEqual(ISEVEN(Number("2")), "ISEVEN(2)")
        self.assertEqual(ISEVEN(CellReference("[.A1]")), "ISEVEN([.A1])")
        self.assertRaises(TypeError, ISEVEN, 2)

    def test_of_isodd(self):
        self.assertEqual(ISODD(Number("2")), "ISODD(2)")
        self.assertEqual(ISODD(CellReference("[.A1]")), "ISODD([.A1])")
        self.assertRaises(TypeError, ISODD, 2)

    def test_of_lcm(self):
        self.assertEqual(LCM(RangeReference("[.A1:.B2]")), "LCM([.A1:.B2])")
        self.assertEqual(LCM(RangeReference("[.A1:.B2]"), RangeReference("[.C3:.D4]")), "LCM([.A1:.B2] ; [.C3:.D4])")
        self.assertRaises(TypeError, LCM, 2)

    def test_of_lcm_add(self):
        self.assertEqual(LCM_ADD(RangeReference("[.A1:.B2]")), "LCM_ADD([.A1:.B2])")
        self.assertEqual(LCM_ADD(RangeReference("[.A1:.B2]"), RangeReference("[.C3:.D4]")), "LCM_ADD([.A1:.B2] ; [.C3:.D4])")
        self.assertRaises(TypeError, LCM_ADD, 2)

    def test_of_ln(self):
        self.assertEqual(LN(Number("2")), "LN(2)")
        self.assertEqual(LN(CellReference("[.A1]")), "LN([.A1])")
        self.assertRaises(TypeError, LN, 2)

    def test_of_log(self):
        self.assertEqual(LOG(CellReference("[.B2]"),Number("3")), "LOG([.B2] ; 3)")
        self.assertRaises(TypeError, LOG, 2)

    def test_of_log10(self):
        self.assertEqual(LOG10(Number("2")), "LOG10(2)")
        self.assertEqual(LOG10(CellReference("[.A1]")), "LOG10([.A1])")
        self.assertRaises(TypeError, LOG10, 2)

    def test_of_mod(self):
        self.assertEqual(MOD(CellReference("[.B2]"),Number("3")), "MOD([.B2] ; 3)")
        self.assertRaises(TypeError, MOD, 2, 3)

    def test_of_mround(self):
        self.assertEqual(MROUND(CellReference("[.B2]"),Number("3")), "MROUND([.B2] ; 3)")
        self.assertRaises(TypeError, MROUND, 2, 3)

    def test_of_multinomial(self):
        self.assertEqual(MULTINOMIAL(RangeReference("[.A1:.B2]")), "MULTINOMIAL([.A1:.B2])")
        self.assertEqual(MULTINOMIAL(RangeReference("[.A1:.B2]"), RangeReference("[.C3:.D4]")), "MULTINOMIAL([.A1:.B2] ; [.C3:.D4])")
        self.assertRaises(TypeError, MULTINOMIAL, 2)

    def test_of_odd(self):
        self.assertEqual(ODD(Number("2")), "ODD(2)")
        self.assertEqual(ODD(CellReference("[.A1]")), "ODD([.A1])")
        self.assertRaises(TypeError, ODD, 2)
        
    def test_of_pi(self):
        self.assertEqual(PI(), "PI()")

    def test_of_power(self):
        self.assertEqual(POWER(CellReference("[.B2]"),Number("3")), "POWER([.B2] ; 3)")
        self.assertRaises(TypeError, POWER, 2, 3)

    def test_of_product(self):
        self.assertEqual(PRODUCT(RangeReference("[.A1:.B2]")), "PRODUCT([.A1:.B2])")
        self.assertEqual(PRODUCT(RangeReference("[.A1:.B2]"), RangeReference("[.C3:.D4]")), "PRODUCT([.A1:.B2] ; [.C3:.D4])")
        self.assertRaises(TypeError, PRODUCT, 2)

    def test_of_quotient(self):
        self.assertEqual(QUOTIENT(CellReference("[.B2]"),Number("3")), "QUOTIENT([.B2] ; 3)")
        self.assertRaises(TypeError, QUOTIENT, 2, 3)

    def test_of_radians(self):
        self.assertEqual(RADIANS(Number("2")), "RADIANS(2)")
        self.assertEqual(RADIANS(CellReference("[.A1]")), "RADIANS([.A1])")
        self.assertRaises(TypeError, RADIANS, 2)
        
    def test_of_rand(self):
        self.assertEqual(RAND(), "RAND()")
        
    def test_of_randbetween(self):
        self.assertEqual(RANDBETWEEN(CellReference("[.B2]"),Number("3")), "RANDBETWEEN([.B2] ; 3)")
        self.assertRaises(TypeError, RANDBETWEEN, 2, 3)

    def test_of_round(self):
        self.assertEqual(ROUND(Number("1")), "ROUND(1)")
        self.assertEqual(ROUND(Number("1"), CellReference("[.A1]")), "ROUND(1 ; [.A1])")
        self.assertRaises(TypeError, ROUND, 2)

    def test_of_rounddown(self):
        self.assertEqual(ROUNDDOWN(Number("1")), "ROUNDDOWN(1)")
        self.assertEqual(ROUNDDOWN(Number("1"), CellReference("[.A1]")), "ROUNDDOWN(1 ; [.A1])")
        self.assertRaises(TypeError, ROUNDDOWN, 2)

    def test_of_roundup(self):
        self.assertEqual(ROUNDUP(Number("1")), "ROUNDUP(1)")
        self.assertEqual(ROUNDUP(Number("1"), CellReference("[.A1]")), "ROUNDUP(1 ; [.A1])")
        self.assertRaises(TypeError, ROUNDUP, 2)

    def test_of_seriessum(self):
        self.assertEqual(SERIESSUM(Number("1"),CellReference("[.A1]"), Number("3"), RangeReference("[.A1:.B2]") ), "SERIESSUM(1 ; [.A1] ; 3 ; [.A1:.B2])")
        self.assertRaises(TypeError, SERIESSUM, 2, 3, 4, 5)

    def test_of_sign(self):
        self.assertEqual(SIGN(Number("2")), "SIGN(2)")
        self.assertEqual(SIGN(CellReference("[.A1]")), "SIGN([.A1])")
        self.assertRaises(TypeError, SIGN, 2)

    def test_of_sin(self):
        self.assertEqual(SIN(Number("2")), "SIN(2)")
        self.assertEqual(SIN(CellReference("[.A1]")), "SIN([.A1])")
        self.assertRaises(TypeError, SIN, 2)

    def test_of_sinh(self):
        self.assertEqual(SINH(Number("2")), "SINH(2)")
        self.assertEqual(SINH(CellReference("[.A1]")), "SINH([.A1])")
        self.assertRaises(TypeError, SINH, 2)

    def test_of_sqrt(self):
        self.assertEqual(SQRT(Number("2")), "SQRT(2)")
        self.assertEqual(SQRT(CellReference("[.A1]")), "SQRT([.A1])")
        self.assertRaises(TypeError, SQRT, 2)

    def test_of_sqrtpi(self):
        self.assertEqual(SQRTPI(Number("2")), "SQRTPI(2)")
        self.assertEqual(SQRTPI(CellReference("[.A1]")), "SQRTPI([.A1])")
        self.assertRaises(TypeError, SQRTPI, 2)

    def test_of_sum(self):
        self.assertEqual(SUM(RangeReference("[.A1:.B2]")), "SUM([.A1:.B2])")
        self.assertEqual(SUM(RangeReference("[.A1:.B2]"), RangeReference("[.C3:.D4]")), "SUM([.A1:.B2] ; [.C3:.D4])")
        self.assertRaises(TypeError, SUM, 2)

    def test_of_sumif(self):
        self.assertEqual(SUMIF(RangeReference("[.A1:.B2]"), Number("3")), "SUMIF([.A1:.B2];3)")
        self.assertEqual(SUMIF(RangeReference("[.A1:.B2]"),Number("3") ,RangeReference("[.C3:.D4]")), "SUMIF([.A1:.B2];3;[.C3:.D4])")
        self.assertRaises(TypeError, SUMIF, 2, 3)

    def test_of_sumsq(self):
        self.assertEqual(SUMSQ(RangeReference("[.A1:.B2]")), "SUMSQ([.A1:.B2])")
        self.assertEqual(SUMSQ(RangeReference("[.A1:.B2]"), RangeReference("[.C3:.D4]")), "SUMSQ([.A1:.B2] ; [.C3:.D4])")
        self.assertRaises(TypeError, SUMSQ, 2)

    def test_of_tan(self):
        self.assertEqual(TAN(Number("2")), "TAN(2)")
        self.assertEqual(TAN(CellReference("[.A1]")), "TAN([.A1])")
        self.assertRaises(TypeError, TAN, 2)

    def test_of_tanh(self):
        self.assertEqual(TANH(Number("2")), "TANH(2)")
        self.assertEqual(TANH(CellReference("[.A1]")), "TANH([.A1])")
        self.assertRaises(TypeError, TANH, 2)

    def test_of_trunc(self):
        self.assertEqual(TRUNC(CellReference("[.B2]"),Number("3")), "TRUNC([.B2] ; 3)")
        self.assertRaises(TypeError, TRUNC, 2, 3)





if __name__ == '__main__':
    unittest.main()


                          


                          
