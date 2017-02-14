class Solution:
    # @param {string} str
    # @return {integer}
    def myAtoi(self, str):
        sign = 1
        i = 0
        INT_MAX = 2147483647
        INT_MIN = -2147483648
        ret = 0

        # Remove space
        while i < len(str):
            if str[i] == ' ':
                i = i + 1
            else:
                break

        if i < len(str) and str[i] == '+':
            i = i + 1
        elif i < len(str) and str[i] == '-':
            i = i + 1
            sign = -1

        while i < len(str):
            if str[i] in '0123456789':
                num = ord(str[i]) - ord('0')
                # (ret * 10 + num) > INT_MAX
                if sign == 1 and ret > (INT_MAX - num) / 10:
                    return INT_MAX
                # (-ret * 10 - num) < INT_MIN
                elif sign == -1 and ret > (INT_MIN + num) / (-10):
                    return INT_MIN
                ret = ret * 10 + num
                i = i + 1
            else:  # might have space in the end
                return ret * sign
        return ret * sign
    # Time: O(n)
    # Space: O(1)
