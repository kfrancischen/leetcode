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
        if not root:
            return 0
        result = 0
        stack = [[root, root.val]]
        while stack:
            node, val = stack.pop(0)
            if node.left:
                stack.append([node.left, val * 10 + node.left.val])
            if node.right:
                stack.append([node.right, val * 10 + node.right.val])
                
            if not node.left and not node.right:
                result += val
        return result