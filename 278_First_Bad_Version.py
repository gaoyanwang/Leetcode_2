## The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """

        l = 1
        r = n
        while l <= r:
            mid = l + (r - l) / 2
            if isBadVersion(mid) is True:
                r = mid - 1
            else:
                l = mid + 1

        return l
# Time: O(logn)
# Space: O(1)
