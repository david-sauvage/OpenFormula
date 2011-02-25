# Import from the Standard Library
from unittest import TestLoader, TestSuite, TextTestRunner

# Import tests
import test_of_basics_op
import test_of_logical
import test_of_maths
import test_of_stats
import test_of_syntax


test_modules = [test_of_basics_op,
		test_of_logical,
		test_of_maths,
		test_of_stats,
		test_of_syntax]


loader = TestLoader()

if __name__ == '__main__':
    suite = TestSuite()
    for module in test_modules:
        suite.addTest(loader.loadTestsFromModule(module))

    TextTestRunner(verbosity=1).run(suite)
