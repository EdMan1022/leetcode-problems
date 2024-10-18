from unittest import TestCase

from python_problems.src.median_of_two_sorted_arrays import Solution


class TestUtil(TestCase):

    def test_simple_case(self):
        test_input = [
            [1, 3],
            [2,]
        ]
        expected_output = 2.
        actual_ouput = Solution().findMedianSortedArrays(test_input[0], test_input[1])

        assert actual_ouput == expected_output

    def test_5s_case(self):
        test_input = [
            [1, 3, 5, 6],
            [4,]
        ]

        expected_output = 4.
        actual_ouput = Solution().findMedianSortedArrays(test_input[0], test_input[1])

        assert actual_ouput == expected_output

    def test_evens_case(self):
        test_input = [
            [1, 2],
            [3, 4]
        ]
        expected_output = 2.5
        actual_ouput = Solution().findMedianSortedArrays(test_input[0], test_input[1])

        assert actual_ouput == expected_output

    def test_big_outlier(self):
        test_input = [
            [2, 3, 4],
            [1, 76, 77]
        ]
        expected_output = 3.5
        actual_ouput = Solution().findMedianSortedArrays(test_input[0], test_input[1])

        assert actual_ouput == expected_output

    def test_large_input(self):
        test_input_1 = [i for i in range(1000000)]
        test_input_2 = [i * 2 for i in range(1000000)]
        actual_output = Solution().findMedianSortedArrays(test_input_1, test_input_2)

        print(actual_output)
