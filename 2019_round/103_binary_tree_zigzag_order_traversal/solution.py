# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from copy import deepcopy
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        
        stack = [root]
        result = [[root.val]]
        count = 1
        direction = 0
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
                count = len(stack)
                if direction == 0:
                    result.append(deepcopy(level[::-1]))
                else:
                    result.append(deepcopy(level))
                level = []
                    
                direction = 1 - direction
        return result