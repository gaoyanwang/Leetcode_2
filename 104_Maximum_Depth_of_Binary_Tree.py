# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

# Space: O(n)
# Time: O(n)

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        count = 0

        if root is None:
            return count

        to_check = [root]
        while len(to_check) > 0:
            count = count + 1
            cur = []
            for e in to_check:
                if e.left is not None:  # None is also an element
                    cur.append(e.left)
                if e.right is not None:
                    cur.append(e.right)
            to_check = cur  # if last level is all none, nothing will be added

        return count

# Space: O(n)
# Time: O(n)
