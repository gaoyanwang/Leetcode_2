class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)

        self.reverse(nums, n - k % n, n - 1)
        print nums
        self.reverse(nums, 0, n - k % n - 1)
        print nums
        self.reverse(nums, 0, n - 1)
        print nums

    def reverse(self, l, front, back):
        while front < back:
            l[front], l[back] = l[back], l[front]
            front = front + 1
            back = back - 1
# Time:O(n)
# Space:O(1)
