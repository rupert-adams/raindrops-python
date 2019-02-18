import unittest
from factor import Factor

class FactorTest(unittest.TestCase):

    def test_can_print_number_as_string(self):
        assert Factor(4).raindrops == "4"

    def test_can_return_pling_if_number_divisible_by_3(self):
        assert Factor(3).raindrops == "Pling"

    def test_can_return_plong_if_number_divisible_by_7(self):
        assert Factor(28).raindrops == "Plong"

    def test_can_return_plingplang_if_divisible_by_3_and_5(self):
        assert Factor(30).raindrops == "PlingPlang"

    def test_can_print_number_as_string(self):
        assert Factor(34).raindrops == "34"
