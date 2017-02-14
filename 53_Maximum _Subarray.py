public class Solution {
	public int maxSubArray(int[] nums) {
		if (nums == null || nums.length == 0) {
			return 0;
		}
		int ret = Integer.MIN_VALUE;
		int cur = 0;
		for (int i = 0; i < nums.length; i++) {
			cur += nums[i];
			ret = Math.max(ret, cur);
			if (cur < 0) {
				cur = 0;
			}
		}
		return ret;
	}
}

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == []:
            return None
        ret = -sys.maxint - 1
        cur = 0
        for i in range(len(nums)):
        	cur += nums[i]
        	ret = max(ret, cur)
        	if cur < 0:
        		cur = 0
        return ret