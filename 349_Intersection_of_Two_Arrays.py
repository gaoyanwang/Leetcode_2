class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1 = set(nums1)
        nums2 = list(set(nums2))
        ret = []
        for e in nums2:
            if e in nums1:
                ret.append(e)
        return ret
# Time: O(n)
# Space: O(n)
