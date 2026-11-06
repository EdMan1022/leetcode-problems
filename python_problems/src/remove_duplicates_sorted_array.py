class Solution(object):
    def removeDuplicates(self, nums):
        """
        Removes all duplicate numbers from the input array in place

        Since nums is sorted, if n + 1 isn't greater than n, it's a duplicate and can be removed.
        Just have to iterate through the array, if n+1 is == n then remove it
        and check n+1 again (in case it's a sequence of multiple dupes)
        :type nums: List[int]
        :rtype: int
        """
        n_index = 0
        max_n = len(nums) - 1
        while n_index < max_n:
            dupes_cleared = False
            n_num = nums[n_index]
            while not dupes_cleared:
                try:
                    next_num = nums[n_index + 1]
                    if next_num == n_num:
                        nums.pop(n_index + 1)
                        max_n -= 1  # decrement upper limit by 1 since we removed an element
                    else:
                        dupes_cleared = True
                except IndexError:
                    dupes_cleared = True
            n_index += 1
        return max_n + 1