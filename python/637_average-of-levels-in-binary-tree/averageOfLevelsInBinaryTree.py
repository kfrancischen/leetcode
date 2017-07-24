# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        if not root:
            return []
        stack = [root]
        count, result = 1, [root.val]
        ave = 0
        while stack:
            node = stack.pop(0)
            count -= 1
            if node.left:
                stack.append(node.left)
                ave += node.left.val
            if node.right:
                stack.append(node.right)
                ave += node.right.val

            if count == 0 and stack:
                count = len(stack)
                result.append(ave*1.0 / count)
                ave = 0

        return result