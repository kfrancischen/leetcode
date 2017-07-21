# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.maxSum = float('-inf')
        self.maxPathDown(root)
        return self.maxSum

    def maxPathDown(self, root):
        if not root:
            return 0

        left = max(0, self.maxPathDown(root.left))
        right = max(0, self.maxPathDown(root.right))
        self.maxSum = max(self.maxSum, left + right + root.val)
        return max(left, right) + root.val
