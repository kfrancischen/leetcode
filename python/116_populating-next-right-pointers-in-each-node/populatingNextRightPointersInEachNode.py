# Definition for binary tree with next pointer.
class TreeLinkNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution(object):
    def connect(self, root):
        """
        :type root: TreeLinkNode
        :rtype: nothing
        """
        if not root:
            return
        stack = [root]
        level = 0
        while stack:
            curLength = len(stack)
            for i in range(0, curLength):
                if i != curLength - 1:
                    stack[i].next = stack[i + 1]
                else:
                    stack[i].next = None
                if stack[i].left:
                    stack.append(stack[i].left)
                if stack[i].right:
                    stack.append(stack[i].right)
            stack = stack[2 ** level:]
            level += 1

n0 = TreeLinkNode(0)
n1 = TreeLinkNode(1)
n2 = TreeLinkNode(2)
n3 = TreeLinkNode(3)
n4 = TreeLinkNode(4)
n5 = TreeLinkNode(5)
n6 = TreeLinkNode(6)
n0.left = n1
n0.right = n2
n1.left = n3
n1.right = n4
n2.left = n5
n2.right = n6
mytest = Solution()
mytest.connect(n0)
