# Import from the Standard Library
from unittest import TestLoader, TestSuite, TextTestRunner

# Import tests
import test_basics
import test_logic
import test_maths
import test_stats
import test_syntax


test_modules = [test_basics,
                test_logic,
                test_maths,
                test_stats,
                test_syntax]

loader = TestLoader()

if __name__ == '__main__':
    suite = TestSuite()
    for module in test_modules:
        suite.addTest(loader.loadTestsFromModule(module))

    TextTestRunner(verbosity=1).run(suite)
