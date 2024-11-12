from unittest import TestCase
from python_problems.src.triple_sum import Solution


class TestTripleSum(TestCase):

    def test_simplest_input(self):
        input_nums = [0,0,0]
        expected_output = [[0,0,0],]
        actual_output = Solution().threeSum(input_nums)
        assert actual_output == expected_output

    def test_positive_input(self):
        input_nums = [-1,0,1]
        expected_output = [[-1,0,1],]
        actual_output = Solution().threeSum(input_nums)
        assert actual_output == expected_output


    def test_simple_input(self):
        input_nums = [-1,0,1,2,-1,-4]
        expected_output = [[-1,-1,2],[-1,0,1]]
        actual_output = Solution().threeSum(input_nums)
        assert actual_output == expected_output

    def test_4_identical(self):
        input_nums = [0,0,0,0]
        expected_output = [[0, 0, 0],]
        actual_output = Solution().threeSum(input_nums)
        assert actual_output == expected_output


    def test_3_numbers_only(self):
        input_nums = [0,1,1]
        expected_output = []
        actual_output = Solution().threeSum(input_nums)
        assert actual_output == expected_output

    def test_skip_input(self):
        input_nums = [-5, 0, 1, 2, 4]
        expected_output = [[-5,1,4]]
        actual_output = Solution().threeSum(input_nums)
        assert actual_output == expected_output
