# 12. Integer to Roman   QuestionEditorial Solution  My Submissions
# Total Accepted: 84340
# Total Submissions: 199664
# Difficulty: Medium
# Contributors: Admin
# Given an integer, convert it to a roman numeral.

# Input is guaranteed to be within the range from 1 to 3999.
class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        string = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X',
        / 'IX', 'V', 'IV', 'I']
        ret = []
        i = 0
        while num > 0:
            if num >= val[i]:  # '=' is important
                ret.append(string[i])
                num -= val[i]
            else:
                i = i + 1
        return ''.join(ret)  # list to str
# Time: O(n)
# Space: O(1)
# 90, 40, 9, 4, avoid more than three repeats