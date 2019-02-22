# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from copy import deepcopy
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        result = [[root.val]]
        count = 1
        stack = [root]
        level = []
        while stack:
            node = stack.pop(0)
            count -= 1
            if node.left:
                stack.append(node.left)
                level.append(node.left.val)
            if node.right:
                stack.append(node.right)
                level.append(node.right.val)

            if count == 0 and stack:
                print(level)
                count = len(stack)
                result.append(deepcopy(level))
                level = []

        return result