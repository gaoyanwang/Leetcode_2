# 35. Search Insert Position   
# Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

# You may assume no duplicates in the array.

# Here are few examples.
# [1,3,5,6], 5 → 2
# [1,3,5,6], 2 → 1
# [1,3,5,6], 7 → 4
# [1,3,5,6], 0 → 0

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if nums == []:
            return None
        l = 0
        r = len(nums) - 1

        while l <= r:
            middle = (l + r) / 2
            if nums[middle] == target:
                return middle
            elif nums[middle] < target:
                l += 1
            else:
                r -= 1
        return l  # nums[l] is always larger than target

# Time : O(logn)
# Space: O(1)
