class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = [0 for i in range(26)]
        for i in range(len(s)):
            l[ord(s[i]) - ord('a')] += 1
        for i in range(0, len(s)):
            if l[ord(s[i]) - ord('a')] == 1:
                return i
        return -1
# Time: O(n)
# Space:O(1)
