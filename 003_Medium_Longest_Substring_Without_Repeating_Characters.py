# #
# Given a string, find the length of the longest substring without repeating characters.

# Examples:

# Given "abcabcbb", the answer is "abc", which the length is 3.

# Given "bbbbb", the answer is "b", with the length of 1.

# Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
# #

# Solution 1: Set
from sets import Set
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == '':
            return 0

        l = 0
        r = 0
        set_x = Set()
        max_len = 0

        while r < len(s):
            if s[r] not in set_x:
                set_x.add(s[r])
                r = r + 1
                max_len = max(max_len, r - l)  # update maxLen
            else:
                while s[l] != s[r]:
                    set_x.remove(s[l])
                    l = l + 1
                set_x.remove(s[l])
                l = l + 1
        return max_len
# Time: O(n)
# Space: O(n)

# Solution 2: 256 ASC numbers
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rty

        """
        if len(s) == 0:
            return 0

        ref = [-1 for i in range(0, 256)]
        maxLen = 0
        l = 0
        r = 0
        while r < len(s):
            index = ord(s[r])  # position in the ref array

            if ref[index] >= l:
                l = ref[index] + 1

            ref[index] = r
            maxLen = max(r - l + 1, maxLen)  # updates
            r = r + 1
        return maxLen

# Time: O(n)
# Space:O(1)
