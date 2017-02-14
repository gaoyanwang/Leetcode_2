# 16. 3Sum Closest   
# Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

#     For example, given array S = {-1 2 1 -4}, and target = 1.

#     The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # Convert Java Solution 1/1
        if nums is None or len(nums) < 3:
            return None
        nums.sort()
        closest = nums[0] + nums[1] + nums[2] - target
        for i in range(0, len(nums) - 2):
            cur = self.twoSum(nums, i + 1, target - nums[i])
            if abs(cur) < abs(closest):
                closest = cur
        return closest + target
    def twoSum(self, nums, left, target):
        right = len(nums) - 1
        closest = nums[left] + nums[right] - target  # initialization
        while left < right:
            if nums[left] + nums[right] == target:
                return 0
            # check and updated
            cur = nums[left] + nums[right] - target
            if abs(cur) < abs(closest):
                closest = cur
            # check and move

            elif nums[left] + nums[right] < target:
                left += 1
            else:
                right -= 1
        return closest

# Time: O(n * n)
# Space: O(1)
