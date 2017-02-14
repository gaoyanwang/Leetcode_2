# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Recursive
class Solution(object):
    def helper(self, leftNode, rightNode):
        if leftNode is None and rightNode is None:
            return True
        elif leftNode is None or rightNode is None:
            return False
        return leftNode.val == rightNode.val and \
            self.helper(leftNode.right, rightNode.left) and \
            self.helper(rightNode.right, leftNode.left)

    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        return self.helper(root.left, root.right)
# Space: worst case, unbalanced tree O(n), balanced O(logn), same to depth
# Time: O(n)

# Interative
class Solution2(object):
    def isSymmetric(self, root):
        if root is None:
            return True
        queue = []
        queue.append((root.left, root.right))  # root.left is a tree or val?
        while len(queue) > 0:
            l, r = queue.pop(0)
            if l is None and r is None:
                continue  # Go to execute " while len(queue) > 0? "
            if l is None or r is None:
                return False
            if l.val != r.val:
                return False
            queue.append((l.left, r.right))
            queue.append((l.right, r.left))
        return True
# Space: worst case, unbalanced tree O(n), balanced O(logn), same to depth
# Time: O(n)