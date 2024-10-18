class Solution(object):

    def findMedianSortedArraysSlow(self, nums1, nums2):
        """
        This approach would probably be faster in a language other than python

        This approach tracks separate indices for each input list,
        iteratively increasing the index for whichever list has the smaller current value.
        When the median index for the combined set is reached,
        return that value (for the odd case),
        or return the average of this index and the previous value (for the even case)

        The problem is that "primitives" in python are all so complicated that the builtin sort command
        is a lot faster than this kind of while loop at a fundamental level.
        So the second solution method below of just combining the arrays, re-sorting them,
        and returning the median is much faster, since the python `sort` command use Cython
        to actually do the bubble sort in C.
        This absolutely would not be the case for a lower level language like C,
        python is just an abomination :)
        :param nums1: List of sorted integers
        :param nums2: List of sorted integers
        :return: the median value of the combined set of nums1 and nums2
        """
        keep_merging = True

        nums_1_index = 0
        nums_2_index = 0
        total_length = len(nums1) + len(nums2)
        max_number = max(nums1[-1], nums2[-1]) + 1

        if total_length % 2 == 0:

            second_median_index = total_length / 2
            first_median_index = second_median_index - 1

            while keep_merging:

                try:
                    current_num_1 = nums1[nums_1_index]
                except IndexError:
                    current_num_1 = max_number
                try:
                    current_num_2 = nums2[nums_2_index]
                except IndexError:
                    current_num_2 = max_number

                if current_num_1 <= current_num_2:
                    current_merged_num = current_num_1
                    bump_num_1 = True
                else:
                    current_merged_num = current_num_2
                    bump_num_1 = False

                if nums_1_index + nums_2_index == first_median_index:
                    first_avg_num = current_merged_num
                elif nums_1_index + nums_2_index == second_median_index:
                    return (first_avg_num + current_merged_num) / 2

                if bump_num_1:
                    nums_1_index += 1
                else:
                    nums_2_index += 1

        else:

            median_index = (total_length - 1) / 2

            while keep_merging:
                try:
                    current_num_1 = nums1[nums_1_index]
                except IndexError:
                    current_num_1 = max_number
                try:
                    current_num_2 = nums2[nums_2_index]
                except IndexError:
                    current_num_2 = max_number

                if current_num_1 <= current_num_2:
                    current_merged_num = current_num_1
                    bump_num_1 = True
                else:
                    current_merged_num = current_num_2
                    bump_num_1 = False
                
                if nums_1_index + nums_2_index == median_index:
                    return current_merged_num

                if bump_num_1:
                    nums_1_index += 1
                else:
                    nums_2_index += 1

    def findMedianSortedArrays(self, nums1, nums2):
        """
        A much faster method for finding the median of two sorted lists in Python

        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        merged_array = nums1 + nums2
        merged_array.sort()
        merged_len = len(merged_array)
        middle_index = int(merged_len / 2)

        if merged_len % 2 != 0:
            return float(merged_array[middle_index])
        else:
            return .5 * (merged_array[middle_index-1] + merged_array[middle_index])

