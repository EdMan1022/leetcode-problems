from unittest import TestCase

from python_problems.src.phone_number import Solution


class TestPhoneNumberStrings(TestCase):

    def test_2_digits(self):
        input_digits = '23'

        expected_output = ["ad","ae","af","bd","be","bf","cd","ce","cf"]

        actual_output = Solution().letterCombinations(input_digits)

        assert actual_output == expected_output

    def test_single_digit(self):
        input_digits = '2'
        expected_output = ['a', 'b', 'c']
        actual_output = Solution().letterCombinations(input_digits)
        assert actual_output == expected_output

    def test_no_digit(self):
        input_digits = ''
        expected_output = []
        actual_output = Solution().letterCombinations(input_digits)
        assert actual_output == expected_output


    def test_triple_digit(self):
        input_digits = '234'
        expected_output = ['adg', 'adh', 'adi', 'aeg', 'aeh', 'aei', 'afg', 'afh', 'afi', 'bdg', 'bdh', 'bdi', 'beg', 'beh', 'bei', 'bfg', 'bfh', 'bfi', 'cdg', 'cdh', 'cdi', 'ceg', 'ceh', 'cei', 'cfg', 'cfh', 'cfi']
        actual_output = Solution().letterCombinations(input_digits)
        print(actual_output)
        assert actual_output == expected_output