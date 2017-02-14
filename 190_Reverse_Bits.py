class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        ans = 0
        for i in range(32):
            ans <<= 1  # last digit of ans is '0'
            ans = ans | (n & 1)  # Put 1 or 0 to the last digits of ans
            n >>= 1  # get next digit to evaluate to the last position
        return ans
# Time: O(n)
# Space: O(1)