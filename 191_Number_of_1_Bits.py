class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        ret = 0
        for i in range(32):
			if n & 1:
				ret = ret + 1
        	n >>= 1
        return ret

class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        while n > 0:
            n = n & (n - 1)
            count = count + 1
        return count
# Time: O(n)
# Space: O(1)