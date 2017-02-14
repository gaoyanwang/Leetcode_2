class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) <= 1:
            return True
        i = 0
        j = len(s) - 1
        while i < j:
            while i < j and not s[i].isalnum():
                i = i + 1
            while j > i and not s[j].isalnum():
                j = j - 1
            if s[i].lower() == s[j].lower():
                i = i + 1
                j = j - 1
            else:
                return False
        return True

#  Time: O(n)
#  Space: O(1)
