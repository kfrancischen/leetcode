# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        stack = [(1, root)]
        maxLen = 1
        while stack:
            preLen, node = stack.pop()
            if node.left:
                if node.left.val == node.val + 1:
                    stack.append((preLen + 1, node.left))
                    maxLen = max(maxLen, preLen + 1)
                else:
                    stack.append((1, node.left))
            if node.right:
                if node.right.val == node.val + 1:
                    stack.append((preLen + 1, node.right))
                    maxLen = max(maxLen, preLen + 1)
                else:
                    stack.append((1, node.right))
                    
        return maxLen