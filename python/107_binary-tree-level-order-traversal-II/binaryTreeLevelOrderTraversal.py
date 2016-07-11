# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        stack = [root]
        count = 1
        result = [[root.val]]
        while stack:
            node = stack.pop(0)
            count -= 1
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
            if count == 0:
                result += [[x.val for x in stack]] if stack else []
                count = len(stack)
        result.reverse()
        return result
