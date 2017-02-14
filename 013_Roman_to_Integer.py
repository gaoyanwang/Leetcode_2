class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        ROMAN = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100,
                 'D': 500, 'M': 1000}

        ret = ROMAN[s[0]]
        for i in range(1, len(s)):
            if ROMAN[s[i]] > ROMAN[s[i - 1]]:
                ret = ret - 2 * ROMAN[s[i - 1]]
            ret = ret + ROMAN[s[i]]
        return ret

# Space = O(1)
# Time = O(n)
