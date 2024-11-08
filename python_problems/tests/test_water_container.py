from unittest import TestCase

from python_problems.src.water_container import Solution


class TestWaterContainer(TestCase):

    def test_simple_prompt(self):
        input_heights = [1, 1]
        expected_output = 1

        actual_output = Solution().maxArea(input_heights)
        assert actual_output == expected_output

    def test_normal_prompt(self):

        input_heights = [1, 8, 6, 2, 5, 4, 8, 3, 7]
        expected_output = 49

        actual_output = Solution().maxArea(input_heights)
        assert actual_output == expected_output

    def test_height_1(self):
        input_heights = [8,1,4,5,7,2]
        expected_output = 28
        actual_output = Solution().maxArea(input_heights)
        assert actual_output == expected_output

    def test_height_2(self):
        input_heights = [8,1,100,1,100,1]
        expected_output = 200
        actual_output = Solution().maxArea(input_heights)
        assert actual_output == expected_output

    def test_outliers_right(self):
        input_heights = [1, 8, 6, 2, 5, 4, 8, 1000, 1000]
        expected_output = 1000

        actual_output = Solution().maxArea(input_heights)
        assert actual_output == expected_output

    def test_big_left(self):
        input_heights = [1, 8, 1000, 1000, 2, 5, 4, 8, 1, 1, 1, 1]
        expected_output = 1000

        actual_output = Solution().maxArea(input_heights)
        assert actual_output == expected_output
