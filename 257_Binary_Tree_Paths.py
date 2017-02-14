class Solution:
    # @param {TreeNode} root
    # @return {string[]}
    def binaryTreePaths(self, root):
        ret = []
        if root is None:
            return ret
        if root.left is None and root.right is None:
            ret.append(str(root.val))
            return ret

        l = binaryTreePaths(root.left)
        for i in range(0, len(l)):
            s = l[i]
            s = root.val + "->" + s
            ret.append[s]

        r = binaryTreePaths(root.right)
        for i in range(0, len(r)):
            s = l[i]
            s = root.val + "->" + s
            ret.append[s]
# Time: O(n)
# Space: O(1)
