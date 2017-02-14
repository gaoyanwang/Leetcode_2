# 18. 4Sum   
# Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

# Note: The solution set must not contain duplicate quadruplets.

# For example, given array S = [1, 0, -1, 0, -2, 2], and target = 0.

# A solution set is:
# [
#   [-1,  0, 0, 1],
#   [-2, -1, 1, 2],
#   [-2,  0, 0, 2]
# 18. 4Sum   
# Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

# Note: The solution set must not contain duplicate quadruplets.

# For example, given array S = [1, 0, -1, 0, -2, 2], and target = 0.

# A solution set is:
# [
#   [-1,  0, 0, 1],
#   [-2, -1, 1, 2],
#   [-2,  0, 0, 2]
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if nums is None or len(nums) < 4:
            return []
        nums.sort()

        # iterate
        i = 0
        right = len(nums) - 3
        ret_4_sum = []

        while i < right:
            cur4 = [([nums[i]] + element) for element in self.threeSum(nums, i + 1, target - nums[i])]
            ret_4_sum = ret_4_sum + cur4
            i += 1
            while i < right and nums[i] == nums[i - 1]:
                i = i + 1
        return ret_4_sum

    # fuction of threeSum
    def threeSum(self, nums, left, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        i = left
        right = len(nums) - 2
        ret_3_sum = []

        while i < right:
            cur3 = [([nums[i]]+ element) for element in self.twoSum(nums, i + 1, target - nums[i])]
            ret_3_sum = ret_3_sum + cur3
            i += 1
            while i < right and nums[i] == nums[i - 1]:
                i = i + 1
        return ret_3_sum

    # function of twoSum
    def twoSum(self, nums, left, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        right = len(nums) - 1
        ret_2_sum = []
        while left < right:

            if nums[left] + nums[right] == target:
                cur2 = []
                cur2.append(nums[left])
                cur2.append(nums[right])
                ret_2_sum.append(cur2)
                left += 1
                right -= 1
                # make sure uniqueness

                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
            elif nums[left] + nums[right] > target:
                right -= 1
            else:
                left += 1
        return ret_2_sum

#  Time: O(n*n*n)
#  Space:O(1) #???