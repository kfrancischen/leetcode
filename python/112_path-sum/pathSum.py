# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
        return self.dfs(root, sum)

    def dfs(self, node, sum):
        if not node:
            if sum == 0:
                return True
            else:
                return False
        if not node.left:
            return self.dfs(node.right, sum - node.val)
        if not node.right:
            return self.dfs(node.left, sum - node.val)

        return self.dfs(node.left, sum - node.val) or self.dfs(node.right, sum - node.val)
