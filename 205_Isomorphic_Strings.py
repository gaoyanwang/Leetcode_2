class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        l1 = [-1] * 256
        l2 = [-1] * 256
        for i in range(0, len(s)):
            if l1[ord(s[i])] == -1 and l2[ord(t[i])] == -1:
                l1[ord(s[i])], l2[ord(t[i])] = i, i
            elif l1[ord(s[i])] != l2[ord(t[i])]:
                return False
        return True

# Time: O(n)
# Space: O(n)
