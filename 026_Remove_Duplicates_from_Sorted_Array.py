class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Extrem case
        if len(nums) <= 1:
            return len(nums)

        # Set two pointers, i, j
        i = 0
        j = 1
        while j < len(nums):
            if nums[j] != nums[j - 1]:  # if j found unique elements ahead
                i += 1  # i move one step and get the new value
                nums[i] = nums[j]
            j = j + 1

        return i + 1
# Time: O(n)
# Space: O(1)
