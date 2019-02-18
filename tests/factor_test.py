import unittest
from factor import Factor

class FactorTest(unittest.TestCase):

    def test_can_print_number_as_string(self):
        assert Factor(4).numb == "4"

    def test_can_get_factors_of_number(self):
        assert Factor(34).getFactor == [1, 2, 17, 34]
