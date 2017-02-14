class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry = 1
        for i in range(len(digits) - 1, -1, -1):
            tmp = digits[i]
            digits[i] = (tmp + carry) % 10
            carry = (tmp + carry) // 10
            if carry == 0:
                return digits
        return [1] + digits
# Time: O(n)
# Space: O(1)
