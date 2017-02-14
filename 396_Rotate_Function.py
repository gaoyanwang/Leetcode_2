class Solution(object):
    def maxRotateFunction(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if len(A) == 0:
            return 0
        base = 0
        for i in range(len(A)):
            base += i * A[i]
        ret = base
        sumA = sum(A)
        for i in range(1, len(A)):
            base += sumA - len(A) * A[len(A) - i]
            ret = max(ret, base)
        return ret
# Time: O(n)
# Space: O(1)
