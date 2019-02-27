# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.validBST(root, float('-inf'), float('inf'))

    def validBST(self, root, minVal, maxVal):
        if not root:
            return True
        if root.val >= maxVal or root.val <= minVal:
            return False
        return self.validBST(root.left, minVal, root.val) and self.validBST(root.right, root.val, maxVal)