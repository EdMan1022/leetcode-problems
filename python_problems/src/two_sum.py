class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        sorted_nums = nums

        for potential_first_n, potential_first in enumerate(sorted_nums):
            target_minus_first = target - potential_first
            for potential_second_n, potential_second in enumerate(sorted_nums[potential_first_n + 1:]):
                if potential_second == target_minus_first:
                    adjusted_second_n = potential_second_n + potential_first_n + 1
                    return [potential_first_n, adjusted_second_n]


class NumItem:

    def __init__(self, original_index, value):
        self.original_index = original_index
        self.value = value


class FasterSolution:

    def twoSum(self, nums, target):
        """
        Use the fact that we can figure out the required number and order the set to search more efficiently

        First, need to make a data structure retaining the original location of each input number,
        since the answer requires their location, not their value.

        Then, sort this list by the value of the
        :param nums:
        :param target:
        :return:
        """

        indexed_nums = [
            NumItem(index, value)
            for index, value in enumerate(nums)
        ]
        original_length = len(indexed_nums)

        sorted_indexed_nums = sorted(indexed_nums, key=lambda x: x.value)

        for first_index, first_item in enumerate(sorted_indexed_nums):
            required_value = target - first_item.value
            subset_sorted_nums = sorted_indexed_nums[first_index + 1:]
            continue_current_loop = True

            while continue_current_loop:

                midpoint = int(len(subset_sorted_nums) / 2)
                midpoint_item = subset_sorted_nums[midpoint]

                if midpoint_item.value == required_value:
                    return [first_item.original_index, midpoint_item.original_index]
                elif midpoint == 0 or midpoint == original_length:
                    continue_current_loop = False
                elif midpoint_item.value > required_value:
                    subset_sorted_nums = subset_sorted_nums[:midpoint]
                elif midpoint_item.value < required_value:
                    subset_sorted_nums = subset_sorted_nums[midpoint:]
