# Solution 1: Dictionary
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        d = {}
        # Add elements to d
        for i in range(0, len(s)):
            if s[i] not in d:
                d[s[i]] = 1
            else:
                d[s[i]] = d[s[i]] + 1
        # Remove elements to d
        for i in range(0, len(t)):
            if t[i] not in d or d[t[i]] < 1:
                return False
            else:
                d[t[i]] = d[t[i]] - 1
        return True

# Time: O(n)
# Space: O(n)
