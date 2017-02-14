# 049_Group_Anagrams
# Contributors: Admin
# Given an array of strings, group anagrams together.

# For example, given: ["eat", "tea", "tan", "ate", "nat", "bat"], 
# Return:

# [
#   ["ate", "eat","tea"],
#   ["nat","tan"],
#   ["bat"]
# ]
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        # initialize a dictionary
        d = {}
        ret = []

        # Take each element
        for string in strs:
            # convert each string to a list, sort, convert to string
            cur = list(string)
            cur.sort()
            cur = ''.join(cur)  # list could not be used as key of dict
            # if it not in dictionary, add
            if cur not in d:
                d[cur] = [string]
            # if in, append
            else:
                d[cur].append(string)
        # sort each key of the dictionary, append
        for e in d:
            d[e].sort()
            ret.append(d[e])
        return ret
# Time: (nklogk), sorting bigO is nlogn
# Space: (nk) k is the length of str
