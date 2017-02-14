# 31. Next Permutation   QuestionEditorial Solution  My Submissions
# Total Accepted: 87474
# Total Submissions: 313720
# Difficulty: Medium
# Contributors: Admin
# Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

# If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

# The replacement must be in-place, do not allocate extra memory.

# Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
# 1,2,3 → 1,3,2
# 3,2,1 → 1,2,3
# 1,1,5 → 1,5,1

class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if nums is None or len(nums) < 2:
            return
        
        # Locate turning point 
        i = len(nums) - 2
        while i >= 0 : # left edge critical
            if nums[i] < nums[i + 1]:
                break
            i -= 1
        
        # edge case: no turing point
        if i < 0:
            self.reverseList(nums, 0)
        
        # Swap and reverse
        for j in range(len(nums) - 1, i, -1):
            if nums[j] > nums[i]:
                nums[j], nums[i] = nums[i], nums[j]
                self.reverseList(nums, i + 1)
                break

    # change list in place
    def reverseList(self, nums, l): 
        r = len(nums) - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
