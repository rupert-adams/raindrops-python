import unittest
from factor import Factor

class FactorTest(unittest.TestCase):

    def test_can_print_number_as_string(self):
        assert Factor(4).numb == 4
