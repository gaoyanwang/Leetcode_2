# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Recursive Method
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        return p.val == q.val and self.isSameTree(p.left, q.left) and \
            self.isSameTree(p.right, q.right)

# Space: worst case, unbalanced tree O(n), balanced O(logn), same to depth ????
# Time: O(n) ???? 

# Non recursive Method:
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """

        l = []
        l.append((p, q))
        while len(l) > 0:
            node1, node2 = l.pop(0)
            if node1 is None and node2 is None:
                continue  # Go to next cycle, skip rest of current cycle
            if node1 is None or node2 is None:
                return False
            if node1.val != node2.val:
                return False
            l.append((node1.left, node2.left))  # push two groups on
            l.append((node1.right, node2.right))
        return True

# Space: worst case, unbalanced tree O(n), balanced O(logn), same to depth
# Time: O(n)
