from unittest import TestCase

from python_problems.src.integer_to_roman import Solution


class TestWaterContainer(TestCase):

    def test_simple_one(self):
        input_int = 1
        expected_output = 'I'

        actual_output = Solution().intToRoman(input_int)
        assert actual_output == expected_output

    def test_one_increment(self):
        input_int = 2
        expected_output = 'II'

        actual_output = Solution().intToRoman(input_int)
        assert actual_output == expected_output

    def test_simple_5(self):
        input_int = 5
        expected_output = 'V'

        actual_output = Solution().intToRoman(input_int)
        assert actual_output == expected_output

    def test_single_decrement(self):
        input_int = 4
        expected_output = 'IV'

        actual_output = Solution().intToRoman(input_int)
        assert actual_output == expected_output

    def test_single_increment(self):
        input_int = 6
        expected_output = 'VI'

        actual_output = Solution().intToRoman(input_int)
        assert actual_output == expected_output

    def test_double_increment(self):
        input_int = 7
        expected_output = 'VII'
        actual_output = Solution().intToRoman(input_int)
        assert actual_output == expected_output

    def test_triple_increment(self):
        input_int = 8
        expected_output = 'VIII'
        actual_output = Solution().intToRoman(input_int)
        assert actual_output == expected_output

    def test_ten_decrement(self):
        input_int = 9
        expected_output = 'IX'
        actual_output = Solution().intToRoman(input_int)
        assert actual_output == expected_output

    def test_increment_combo(self):
        input_int = 16
        expected_output = 'XVI'
        actual_output = Solution().intToRoman(input_int)
        assert actual_output == expected_output

    def test_increment_decrement_combo(self):
        input_int = 14
        expected_output = 'XIV'
        actual_output = Solution().intToRoman(input_int)
        assert actual_output == expected_output

    def test_multiple_combo(self):
        input_int = 99
        expected_output = 'XCIX'
        actual_output = Solution().intToRoman(input_int)
        assert actual_output == expected_output

    def test_multiple_increment_combo(self):
        input_int = 96
        expected_output = 'XCVI'
        actual_output = Solution().intToRoman(input_int)
        assert actual_output == expected_output

    def test_multiple_hundreds(self):
        input_int = 200
        expected_output = 'CC'
        actual_output = Solution().intToRoman(input_int)
        assert actual_output == expected_output

    def test_five_hundreds(self):
        input_int = 600
        expected_output = 'DC'
        actual_output = Solution().intToRoman(input_int)
        assert actual_output == expected_output

    def test_multiple_thousands(self):
        input_int = 3000
        expected_output = 'MMM'
        actual_output = Solution().intToRoman(input_int)
        assert actual_output == expected_output
