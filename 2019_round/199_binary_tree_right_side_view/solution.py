# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
            
        stack = [root]
        count = 1
        result = []
        while stack:
            node = stack.pop(0)
            count -= 1
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
            if count == 0:
                result.append(node.val)
                if stack:
                    count = len(stack)

            
        return result
        