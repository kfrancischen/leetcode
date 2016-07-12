# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        path = 0
        result = []
        self.backTracking(root, result, path)
        return sum(result)

    def backTracking(self, root, result, path):
        if not root:
            return
        if root.left == None and root.right == None:
            result.append(path * 10 + root.val)
            return
        self.backTracking(root.left, result, path * 10 + root.val)
        self.backTracking(root.right, result, path * 10 + root.val)
