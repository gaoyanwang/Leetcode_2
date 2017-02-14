class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        val1, val2 = n, n
        while True:
            val1 = self.helper(val1)
            val2 = self.helper(self.helper(val2))
            if val2 == 1:
                return True
            if val2 == val1:
                return False

    def helper(self, n):
        ret = 0
        while n != 0:
            num_square = (n % 10) * (n % 10)
            ret = ret + num_square
            n = n / 10
        return ret

# Time: O(n)
# Space: O(1)
