# 34. Search for a Range 
# Given a sorted array of integers, find the starting and ending position of a given target value.

# Your algorithm's runtime complexity must be in the order of O(log n).

# If the target is not found in the array, return [-1, -1].

# For example,
# Given [5, 7, 7, 8, 8, 10] and target value 8,
# return [3, 4].
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Cornor case
        if nums is None or len(nums) < 1:
            return [-1, -1]
        # find start at left 
        l = 0
        r = len(nums) -  1
        while l <= r:
            m = (l + r) / 2
            if nums[m] < target:
                l = m + 1
            else:
                r = m - 1
        start = l
        # find end at right
        r = len(nums) - 1
        while l <= r:
            m = (l + r) / 2
            if nums[m] > target:
                r = m - 1
            else:
                l = m + 1
        end = r
        # if does not exist target
        if start > end:
            return [-1, -1]
        
        return [start, end]

# Time: O(longn)
# Space: O(1)