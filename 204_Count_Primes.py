import math
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 3:
            return 0

        l = [1] * (n + 1)
        t = int(math.sqrt(n)) + 1
        for i in range(2, t):
            if l[i] == 1:
                j = i
                while i * j < n:
                    l[i * j] = 0
                    j = j + 1

        return sum(l) - 3
# Time: O(n*loglogn)
# Space: O(n)
