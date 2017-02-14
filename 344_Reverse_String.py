class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)
        return ''.join(reversed(s))

class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        t = []
        for i in range(len(s) -1, -1, -1):
            t.append(s[i])
        return ''.join(t)
# Time: O(n)
# Space: O(n)