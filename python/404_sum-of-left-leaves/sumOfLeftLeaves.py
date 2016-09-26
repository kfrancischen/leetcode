# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        stack = [root]
        count = 1
        result = 0
        while stack:
            node = stack.pop(0)
            count -= 1
            if node.left:
                stack.append(node.left)
                if not node.left.left and not node.left.right:
                    result += node.left.val
            if node.right:
                stack.append(node.right)
            if count == 0 and stack:
                count = len(stack)
        return result
