# 053_Maximum_Subarray
# Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

# For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
# the contiguous subarray [4,-1,2,1] has the largest sum = 6.
import sys
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ret = - sys.maxint - 1
        cur = 0
        for i in range(0, len(nums)):
        	cur = cur + nums[i]
        	ret = max(ret, cur)
        	if cur < 0:  # important, if > 0, contibute to longest
        		cur = 0  # if < 0, trim off
       	return ret
# Time: O(n)
# Space: O(1)
# 如何找出这串数字？
#  从0开始如果出现的是连续的负值，不包括这些数字，最大的subarray一定是正数开始的
#  如果开始出现的正值，继续出现正值，ret越来越大，一旦出现负值，ret变小，但是最大的已经保存好，
 # 如果cur变成负数，说明后半部分出现了太多的负数，此时后半部分不可能对以后有贡献。整个已经出现的部分都无贡献了
 此时应该重新cur记起来，subarray有了新的起点