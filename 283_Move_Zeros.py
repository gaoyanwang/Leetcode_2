class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        l = nums
        i = 0
        j = 0
        while j < len(nums):
            if l[j] != 0:
                if l[i] == 0:
                    l[j], l[i] = l[i], l[j]
                i = i + 1
            j = j + 1
# Time:  O(n)
# Space: O(1)
