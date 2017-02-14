#
# 11_Container_With_Most_Water

# Given n non-negative integers a1, a2, ..., an, where each represents a point
# at coordinate (i, ai). n vertical lines are drawn such that the two endpoints
# of line i is at (i, ai) and (i, 0). Find two lines, which together with 
# x-axis forms a container, such that the container contains the most water.

# Note: You may not slant the container.

# #
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) < 2:
            return 0
        l = 0
        r = len(height) - 1
        ret = 0
        while l < r:
            area = min(height[l], height[r]) * (r - l)
            ret = max(ret, area)  # updates in every situation
            if height[l] < height[r]:
                l = l + 1
            else:
                r = r - 1
        return ret
# Time: O(n)
# Space: O(1)
