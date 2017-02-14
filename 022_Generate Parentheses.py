# Given n pairs of parentheses, write a function to generate all combinations 
# of well-formed parentheses.

# For example, given n = 3, a solution set is:

# [
#   "((()))",
#   "(()())",
#   "(())()",
#   "()(())",
#   "()()()"
# ]
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ret = []
        if n <= 0:
            return ret
        self.helper(n, n, "", ret)
        return ret

    def helper(self, l, r, item, ret):
        if l == 0 and r == 0:
            ret.append(item)
            return 
        if l > 0:
            self.helper(l - 1, r, item + "(", ret)
        if l < r:
            self.helper(l, r - 1, item + ")", ret)