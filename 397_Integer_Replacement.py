class Solution(object):
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        ret = 0
        while n != 1:
            if n & 1 == 0:  # last digit is 0
                n = n >> 1
            elif n == 3 or ((n >> 1) & 1) == 0:
                n -= 1
            else:
                n += 1
            ret += 1
        return ret
# Time: O(logn)
# Space: O(1)
