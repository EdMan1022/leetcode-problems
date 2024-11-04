from unittest import TestCase

from python_problems.src.string_zigzag import Solution


class TestStringZigZag(TestCase):

    def test_3_rows(self):

        input_string = 'PAYPALISHIRING'
        num_rows = 3
        expected_output = 'PAHNAPLSIIGYIR'

        actual_output = Solution().convert(input_string, num_rows)

        assert actual_output == expected_output

    def test_4_rows(self):

        input_string = 'PAYPALISHIRING'
        num_rows = 4
        expected_output = 'PINALSIGYAHRPI'

        actual_output = Solution().convert(input_string, num_rows)

        assert actual_output == expected_output

    def test_1_row(self):

        input_string = 'P'
        num_rows = 1
        expected_output = 'P'

        actual_output = Solution().convert(input_string, num_rows)

        assert actual_output == expected_output
