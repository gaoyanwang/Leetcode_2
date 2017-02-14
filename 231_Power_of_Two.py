
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n != 0 and n & (n - 1) == 0:
            return True
        return False
# Time: O(1)
# Space: O(1)
