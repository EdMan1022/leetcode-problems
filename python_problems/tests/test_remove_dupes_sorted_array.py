from unittest import TestCase

from python_problems.src.remove_duplicates_sorted_array import Solution


class TestRemoveDupes(TestCase):

    def test_3_digits(self):
        input_array = [1, 1, 2]
        expected_output = [1, 2]

        actual_output = Solution().removeDuplicates(input_array)
        # assert expected_output == actual_output

    def test_second_double_digits(self):
        input_array = [1, 2, 2]
        expected_output = [1, 2]

        actual_output = Solution().removeDuplicates(input_array)
        # assert expected_output == actual_output