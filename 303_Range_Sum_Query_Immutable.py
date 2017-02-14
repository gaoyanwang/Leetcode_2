class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.sum_list = []
        element = 0
        for i in range(0, len(nums)):
            element = element + nums[i]
            self.sum_list.append(element)
        
    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        if i == 0:
            ret = self.sum_list[j]
        else:
            ret = self.sum_list[j] - self.sum_list[i - 1]
        return ret


# Your NumArray object will be instantiated and called as such:
# numArray = NumArray(nums)
# numArray.sumRange(0, 1)
# numArray.sumRange(1, 2)

# Time O(1), Amortized
# Space: O(n)
