#001_Two sum
class Solution(object):
    def twoSum(self, nums, target):
        if len(nums) > 1:
            d = {}
            for i in range(0, len(nums)):
                if nums[i] not in d:
                    d[target - nums[i]] = i
                else:
                    return [i, d[nums[i]]]
        return None
# Time: O(n)
# Space: O(n)
