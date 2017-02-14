class Solution:
    # @param {integer} x
    # @return {integer}
    def reverse(self, x):
        ret = 0
        INT_MAX = 2147483647
        INT_MIN = -2147483648

        if x == INT_MIN:  # Process special number first, ** KEY step
            return 0

        original_x = x
        x = abs(x)
        while x != 0:
            # Extreme case: out of boundary
            if ret > (INT_MAX - x % 10) / 10.0:  # ** KEY step
                return 0
            else:
                ret = ret * 10 + x % 10
            x = x // 10

        # Two cases
        if original_x > 0:
            return ret
        else:
            return ret * (-1)

# Time: O(logn)
# Space: O(1)
