# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        if root.left is None:
            return self.minDepth(root.right) + 1
        if root.right is None:
            return self.minDepth(root.left) + 1
        return min(self.minDepth(root.left), self.minDepth(root.right)) + 1
# Space: worst case, unbalanced tree O(n), balanced O(logn), same to depth
# Time: O(n)

#  Iterative
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        count = 0
        if root is None:
            return count
        to_check = [root]
        while len(to_check) is not None:
            count = count + 1
            cur = []
            for e in to_check:
                if e.left is None and e.right is None:
                    return count
                if e.left is not None:
                    cur.append(e.left)
                if e.right is not None:
                    cur.append(e.right)
            to_check = cur
        return count
# Space: worst case, unbalanced tree O(n), balanced O(logn), same to depth
# Time: O(n)
