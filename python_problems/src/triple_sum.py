class Solution:


    def threeSum(self, nums):
        sorted_nums = sorted(nums)
        num_length = len(nums)
        left_index = 0
        zero_subsets = list()
        previous_left_value = None

        while True:
            left_value = sorted_nums[left_index]
            previous_middle_value, previous_right_value = None, None
            compare_left_value = -1 * left_value

            right_index = num_length - 1

            middle_index = left_index + 1

            if left_value != previous_left_value:
                while True:
                    right_value = sorted_nums[right_index]
                    middle_value = sorted_nums[middle_index]
                    sub_sum = middle_value + right_value
                    if middle_value != previous_middle_value and right_value != previous_right_value:
                        if sub_sum == compare_left_value:
                            zero_subsets.append([left_value, middle_value, right_value])
                    if sub_sum <= compare_left_value:
                        middle_index += 1
                        previous_middle_value = middle_value
                    else:
                        right_index -= 1
                        previous_right_value = right_value
                    if middle_index == right_index:
                        break

            left_index += 1
            previous_left_value = left_value

            if left_index == middle_index:
                break
            if left_index + 1 == right_index:
                break

        return zero_subsets

    def threeSumm(self, nums):
        """
        Returns the list of unique 3-member subsets from num that sum to 0


        :param num:
        :return:
        """
        sorted_num = sorted(nums)
        num_length = len(nums) - 3
        left_index = -1
        zero_subsets_set = set()
        zero_subsets = list()

        left_loop = True
        while left_loop:
            left_index += 1
            left_value = sorted_num[left_index]
            compare_left_value = -1 * left_value
            half_left_value = compare_left_value / 2
            right_loop = True
            right_index = len(sorted_num) - 1
            right_value = sorted_num[right_index]

            while right_loop:
                middle_loop = True
                middle_index = right_index - 1
                middle_value = sorted_num[middle_index]

                while middle_loop:
                    right_sum = middle_value + right_value
                    if right_sum == compare_left_value:
                        current_subset = [left_value, middle_value, right_value]
                        current_subset_string = str(current_subset)
                        if current_subset_string not in zero_subsets_set:
                            zero_subsets_set.add(current_subset_string)
                            zero_subsets.append(current_subset)

                    elif right_sum < compare_left_value:
                        break
                    middle_index -= 1
                    if middle_index == left_index:
                        break
                    middle_value = sorted_num[middle_index]

                right_index -= 1
                right_value = sorted_num[right_index]
                if right_index == left_index + 1:
                    break
                if right_value < half_left_value:
                    break

            if left_index == num_length:
                left_loop = False

        return zero_subsets
