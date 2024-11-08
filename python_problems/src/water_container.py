class Solution:
    def maxArea1(self, height):

        max_area = 0
        for left_bound_index, left_value in enumerate(height):
            right_heights = height[left_bound_index+1:]
            for right_bound_index, right_value in enumerate(right_heights):
                right_bound_index += left_bound_index + 1
                width = right_bound_index - left_bound_index
                min_height = min(left_value, right_value)
                area = width * min_height
                if area > max_area:
                    max_area = area
        return max_area


    def maxArea(self, height):
        """
        Find the maximum area defined by the elements in the list

        Iterate through the list,
        moving the left boundary to the right if the right boundary value is higher,
        and the right boundary left if the left boundary is higher.
        This process continues until the current area is greater than what could possibly be attained,
        by looking at the current width and the largest height and comparing that to the current max area.
        :param height:
        :return:
        """
        max_area = 0
        left_bound = 0
        right_bound = len(height) - 1
        loop = True
        max_height = max(height)
        while loop:
            left_value = height[left_bound]
            right_value = height[right_bound]
            this_area = min(left_value, right_value) * (right_bound - left_bound)
            if this_area > max_area:
                max_area = this_area

            if left_value >= right_value:
                right_bound -= 1
            else:
                left_bound += 1

            if max_area >= max_height * (right_bound - left_bound):
                break

        return max_area
