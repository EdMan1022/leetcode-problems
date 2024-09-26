from unittest import TestCase
from python_problems.src.two_sum import Solution, FasterSolution


class TestTwoSum(TestCase):

    def test_simple_input(self):
        test_nums = [2, 7, 11, 15]
        test_target = 9
        solution = Solution().twoSum(test_nums, test_target)
        assert [0, 1] == solution

    def test_input_answer_not_first_2(self):
        test_nums = [3, 2, 4]
        test_target = 6
        solution = Solution().twoSum(test_nums, test_target)
        assert [1, 2] == solution


class TestFasterTwoSum(TestCase):

    def test_fast_simple(self):
        test_nums = [2, 7, 11, 15]
        test_target = 9
        solution = FasterSolution().twoSum(test_nums, test_target)
        assert [0, 1] == solution

    def test_fast_simple_not_first_2(self):
        test_nums = [3, 2, 4]
        test_target = 6
        solution = FasterSolution().twoSum(test_nums, test_target)
        assert [1, 2] == solution

    def test_odd_length_input_non_sequential(self):
        test_nums = [16, 2, 4, 9, 18]
        test_target = 34
        solution = FasterSolution().twoSum(test_nums, test_target)
        assert [0, 4] == solution
