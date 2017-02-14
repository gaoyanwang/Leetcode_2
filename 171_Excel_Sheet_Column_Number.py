class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        ret = 0
        for i in range(0, len(s)):
            ret = ret * 26 + (ord(s[i]) - ord('A') + 1)
        return ret

# Time: O(n)
# Space:O(1)
