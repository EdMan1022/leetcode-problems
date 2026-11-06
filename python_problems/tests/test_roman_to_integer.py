from unittest import TestCase

from python_problems.src.roman_to_integer import Solution


class TestRomanInteger(TestCase):

    def test_single_symbol(self):
        test_input = 'I'
        expected_output = 1

        assert Solution().romanToInt(test_input) == expected_output

    def test_duplicate_symbol(self):
        test_input = 'II'
        expected_output = 2

        assert Solution().romanToInt(test_input) == expected_output

    def test_different_symbols(self):
        test_input = 'VI'
        expected_output = 6

        assert Solution().romanToInt(test_input) == expected_output

    def test_subtraction(self):
        test_input = 'IV'
        expected_output = 4

        assert Solution().romanToInt(test_input) == expected_output

    def test_subtraction_2(self):
        test_input = 'IX'
        expected_output = 9

        assert Solution().romanToInt(test_input) == expected_output

    def test_subtraction_3(self):
        test_input = 'XL'
        expected_output = 40

        assert Solution().romanToInt(test_input) == expected_output

    def test_subtraction_4(self):
        test_input = 'XC'
        expected_output = 90

        assert Solution().romanToInt(test_input) == expected_output

    def test_subtraction_5(self):
        test_input = 'CD'
        expected_output = 400

        assert Solution().romanToInt(test_input) == expected_output

    def test_combined_subtraction(self):
        test_input = 'MCMXCIV'
        expected_output = 1994

        assert Solution().romanToInt(test_input) == expected_output

    def test_combined_subtraction_2(self):
        test_input = 'MCMXCVII'
        expected_output = 1997

        assert Solution().romanToInt(test_input) == expected_output

    def test_combined_subtraction_3(self):
        test_input = 'LVIII'
        expected_output = 58

        assert Solution().romanToInt(test_input) == expected_output