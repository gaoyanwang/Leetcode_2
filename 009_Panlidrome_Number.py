class Solution:
    # @param {integer} x
    # @return {boolean}
    def isPalindrome(self, x):
        if x < 0:
            return False

        INT_MAX = 2147483647
        ret = 0
        origin_x = x
        while x != 0:
            if ret > (INT_MAX - x % 10) / 10:
                return False  # ret * 10 + x % 10 > INT_MAX
            else:
                ret = ret * 10 + x % 10
                x = x // 10

        return origin_x == ret


# Solution 2
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False

        factor = 1
        x2 = x
        while x2 != 0:
            factor = factor * 10
            x2 = x2 // 10
        factor = factor / 10

        while x != 0:
            if x // factor == x % 10:
                x = x % factor // 10
                factor = factor // 100
            else:
                return False
        return True

# Time: O(logn)
# Space: O(1)
