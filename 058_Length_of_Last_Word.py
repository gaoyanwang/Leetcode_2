class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        ret = 0
        i = len(s) - 1
        # Remove space
        while i >= 0 and s[i] == " ":
            i = i - 1
        # Count chacters till meet space or the head of the string
        j = i
        while j >= 0 and s[j] != " ":
            j -= 1
        return i - j
# Time: O(n)
# Space: O(1)
