class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        l = str.split(" ")
        if len(pattern) != len(l):
            return False
        d1 = {}
        d2 = {}
        for i in range(0, len(pattern)):
            if pattern[i] not in d1:
                if l[i] in d2:
                    return False
                else:
                    d1[pattern[i]] = l[i]
                    d2[l[i]] = pattern[i]
            else:
                if d1[pattern[i]] != l[i]:
                    return False
        return True

# Time: O(n)
# Space: O(n)
