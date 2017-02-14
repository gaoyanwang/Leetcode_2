class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n <= 0:
            raise ValueError(" input is not valid!")
        ret = ""
        while n > 0:
            n = n - 1
            c = chr(ord('A') + n % 26)
            n = n / 26
            ret = str(c) + ret
        return ret

# Time: O(logn)
# Space: O(1)
