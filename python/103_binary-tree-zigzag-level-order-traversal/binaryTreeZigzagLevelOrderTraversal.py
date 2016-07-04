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
        if root == None:
            return []
        stack = []
        result = []
        stack.append(root)
        result.append([root.val])
        level = 2
        nodesNextLevel = []
        nodesNextLevelVal = []
        while len(stack) != 0:
            node = stack.pop()
            if level % 2 == 0:
                if node.right != None:
                    nodesNextLevel.append(node.right)
                    nodesNextLevelVal.append(node.right.val)
                if node.left != None:
                    nodesNextLevel.append(node.left)
                    nodesNextLevelVal.append(node.left.val)
            else:
                if node.left != None:
                    nodesNextLevel.append(node.left)
                    nodesNextLevelVal.append(node.left.val)
                if node.right != None:
                    nodesNextLevel.append(node.right)
                    nodesNextLevelVal.append(node.right.val)

            if len(stack) == 0 and len(nodesNextLevel) != 0:
                stack = deepcopy(nodesNextLevel)
                result.append(deepcopy(nodesNextLevelVal))
                nodesNextLevel = []
                nodesNextLevelVal = []
                level += 1
        return result
