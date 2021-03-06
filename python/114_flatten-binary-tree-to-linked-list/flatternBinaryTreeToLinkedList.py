# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if not root:
            return None
        self.flatten(root.right)
        if root.left:
            self.flatten(root.left)
            right, root.right, root.left = root.right, root.left, None
            p = root.right
            while p and p.right:
                p = p.right
            p.right = right
