# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.dfs(root) != -1

    def dfs(self, root):
        if not root:
            return 0
        d1 = self.dfs(root.left)
        if d1 == -1:
            return -1

        d2 = self.dfs(root.right)
        if d2 == -1:
            return -1

        return -1 if abs(d1 - d2) > 1 else max(d1, d2) + 1
