class Solution:
    # @param {string[]} strs
    # @return {string}
    def longestCommonPrefix(self, strs):
        # empty list or only have one element
        if len(strs) == 0:
            return ""
        elif len(strs) == 1:
            return strs[0]

        # Normal case
        ret = ""
        for i in range(len(strs[0])):  # use first element of strs as base
            for e in strs[1:]:
                if len(e) < i + 1 or e[i] != strs[0][i]:
                    return ret
            ret = ret + strs[0][i]
        return ret
#  Time: O(n*m)
#  Space: O(1)
