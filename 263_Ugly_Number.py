class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        while num % 2 == 0:
            num = num / 2
        while num % 3 == 0:
            num = num / 3
        while num % 5 == 0:
            num = num / 5
        return num == 1
# Time: O(logn)
# Space: O(1)
