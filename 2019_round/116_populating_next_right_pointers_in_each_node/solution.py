"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return None

        count = 1
        stack = [root]
        while stack:

            node = stack.pop(0)
            count -= 1
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

            if count == 0 and stack:
                for i in range(len(stack) - 1):
                    stack[i].next = stack[i+1]
                count = len(stack)
        return root