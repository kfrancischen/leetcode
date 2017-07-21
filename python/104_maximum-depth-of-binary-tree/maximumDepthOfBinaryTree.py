# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        stack = []
        if not root:
            return 0
        stack.append(root)
        count = 1
        depth = 0
        while stack:
            node = stack.pop(0)
            count -= 1
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
            if count == 0:
                count = len(stack)
                depth += 1
        return depth
