class Solution:
    # @return a boolean
    def isValid(self, s):
        # stack problem
        l = []
        left = '([{'
        right = ')]}'

        # loop over every character in s
        for i in range(0, len(s)):
            if s[i] in left:
                l.append(s[i])
            else:
                if l == []:
                    return False
                elif left.index(l[-1]) != right.index(s[i]):  # neat trick
                    return False
                else:
                    l.pop()

        # if the loop finished with comparing all characters, the list
        # need to be empty to be true

        if l == []:
            return True
        else:
            return False
# Time: O(n)
# Space: O(n)
