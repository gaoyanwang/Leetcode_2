# #
# 15. 3Sum 

# Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

# Note: The solution set must not contain duplicate triplets.

# For example, given array S = [-1, 0, 1, 2, -1, -4],

# A solution set is:
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]
# #
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # Convert Java Solution 1/1
        ret = []
        if nums is None or len(nums) <= 2:
            return ret
        nums.sort()

        for i in range(len(nums) - 1, 1, -1):
            if i < len(nums) - 1 and nums[i] == nums[i + 1]:
                continue
            curRet = self.twoSum(nums, i - 1, -nums[i])
            ret = ret + curRet
        return ret

    def twoSum(self, nums, right, target):
        left = 0
        curRet = []
        while left < right:
            if nums[left] + nums[right] == target:
                list1 = []
                list1.append(nums[left])
                list1.append(nums[right])
                list1.append(-target)
                curRet.append(list1)
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
            elif nums[left] + nums[right] < target:
                left += 1
            else:
                right -= 1
        return curRet

# Time: O(n * n)
# Space: O(1)




