# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return None  # ??
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root

# Ieterative Method
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return None
        queue = collections.deque()
        queue.append(root)  # root address as an element
        while len(queue) > 0:
            node = queue.popleft()
            if node.left is not None:  # "None" should not be added
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
            node.left, node.right = node.right, node.left
        return root
# Time: O(n)
# Space: O(n)
