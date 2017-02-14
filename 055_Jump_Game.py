# 055_Jump_Game 
# Given an array of non-negative integers, you are initially positioned at the
# first index of the array.

# Each element in the array represents your maximum jump length at that position.

# Determine if you are able to reach the last index.

# For example:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        ret = 0
        for i in range(0, len(nums)):
            if ret < i:
                return False
            if ret >= len(nums) - 1:
                return True
            ret = m ax(ret, i + nums[i])
        return True  # i reach end, means get to end
# Time: O(n)
# Space: O(1)
