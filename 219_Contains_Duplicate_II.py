class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        d = {}
        for i in range(0, len(nums)):
            if nums[i] in d:
                if i - d[nums[i]] <= k:
                    return True
            d[nums[i]] = i
        return False

# Time: O(n)
# Space: O(n)
