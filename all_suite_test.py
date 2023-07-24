import unittest

from unittest.loader import makeSuite

from test_cases.add_a_player import TestAddAPlayerPage
from test_cases.framework import Test
from test_cases.log_in_to_the_system import TestLoginPage

def full_suite():
   test_suite = unittest.TestSuite()
   test_suite.addTest(makeSuite(TestLoginPage))
   test_suite.addTest(makeSuite(TestAddAPlayerPage))
   test_suite.addTest(makeSuite(Test))
   return test_suite

if __name__ == '__main__':
   runner = unittest.TextTestRunner(verbosity=2)
   runner.run(full_suite())