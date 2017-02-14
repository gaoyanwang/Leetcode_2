class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        while num > 9:
            ret = 0
            while num > 0:
                dig = num % 10
                ret = ret + dig
                num = num / 10
            num = ret
        return num
# Time: O(logn)
# Space: O(1)
