# 060_Permutation_Sequence
# The set [1,2,3,…,n] contains a total of n! unique permutations.

# By listing and labeling all of the permutations in order,
# We get the following sequence (ie, for n = 3):

# "123"
# "132"
# "213"
# "231"
# "312"
# "321"
# Given n and k, return the kth permutation sequence.

# Note: Given n will be between 1 and 9 inclusive.
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ret = []
        if nums is None or len(nums) == 0:
        	return ret
        used = [False for i in range(0, len(nums))]
        self.helper(ret, [],[], num)
        return ret
    def helper(ret,item,used,num):
    	if len(item) == len(num):
    		ret.add(item)
    		return
    	for i in range(0, len(num)):
    		if used[i] ==  False:
    			item.add(nums[i])
    			used[i] = True
    			helper(ret, item, used, num)
    			used[i] = False
    			item.pop()

