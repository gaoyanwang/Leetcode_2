class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Special
        if n == 1:
            return 1
        if n == 2:
            return 2

        # n > 2
        ret = [0] * n
        ret[0] = 1
        ret[1] = 2
        for i in range(2, n):
            ret[i] = ret[i - 2] + ret[i - 1]
        return ret[n - 1]

# Space = O(n)
# time = Time (n)

class Solution(object):
    def climbStairs2(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Special
        if n == 1:
            ret = 1
        if n == 2:
            ret = 2

        # n > 2
        prior1 = 1
        prior2 = 2
        for i in range(3, n + 1):
            ret = prior1 + prior2
            prior1 = prior2
            prior2 = ret
        return ret

# Space = O(1)
# Time = Time (n)
