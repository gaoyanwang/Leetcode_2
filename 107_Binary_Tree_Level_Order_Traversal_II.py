
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ret = []

        if root is None:
            return ret

        to_check = [root]
        while len(to_check) > 0:
            cur = []
            l = []
            for e in to_check:
                l.append(e.val)
                if e.left is not None:  # None is also an element
                    cur.append(e.left)
                if e.right is not None:
                    cur.append(e.right)
            to_check = cur  # if last level is all none, nothing will be added
            ret.append(l)
        ret.reverse()  # list.reverse(): Reverse the elements of the list
        return ret     # in place

# Space: O(n)
# Time: O(n)
