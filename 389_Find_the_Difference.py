class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        ret = 0
        for i in range(len(s)):
            ret = ret ^ ord(s[i])
        for i in range(len(t)):
            ret = ret ^ ord(t[i])
        return chr(ret)
# Time: O(n)
# Space: O(1)
