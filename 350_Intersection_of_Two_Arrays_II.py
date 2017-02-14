class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        d = {}
        for e in nums1:
            if e not in d:
                d[e] = 1
            else:
                d[e] += 1
        ret = []
        for e in nums2:
            if e in d and d[e] > 0:
                d[e] -= 1
                ret.append(e)
        return ret
# Time: O(n)
# Space:O(n)
