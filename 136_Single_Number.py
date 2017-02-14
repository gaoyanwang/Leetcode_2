class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None or len(nums) == 0:
        	return 0
        ret = 0
        for e in nums:
        	ret ^= e
        return ret

# Time: O(n)
# Space: O(1)