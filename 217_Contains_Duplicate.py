class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        from sets import Set

        distinct = Set()
        for e in nums:
            if e in distinct:
                return True
            else:
                distinct.add(e)
        return False

# Time: O(n)
# Space: O(n)
