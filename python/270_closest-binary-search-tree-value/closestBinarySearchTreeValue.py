# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import sys
class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        if root is None:
            return sys.maxsize
        left_close = self.closestValue(root.left, target)
        right_close = self.closestValue(root.right, target)
        if abs(left_close - target) < abs(right_close - target) and abs(left_close - target) < abs(root.val - target):
            return left_close
        if abs(right_close - target) < abs(left_close - target) and abs(right_close - target) < abs(root.val - target):
            return right_close
        if abs(root.val - target) < abs(left_close - target) and abs(root.val - target) < abs(right_close - target):
            return root.val