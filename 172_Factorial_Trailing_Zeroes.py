class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        x = 5
        ret = 0
        while n >= x:
            ret = ret + n // x
            x = x * 5
        return ret

# Time: O(log(5,n))
# Space: O(1)
