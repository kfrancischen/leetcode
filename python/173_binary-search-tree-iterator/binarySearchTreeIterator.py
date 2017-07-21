# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):
    def __init__(self, root):
        self.q=[]
        self.allLeftIntoStack(root)

    # @return a boolean, whether we have a next smallest number
    def hasNext(self):
        if not self.q:return False
        return True

    # @return an integer, the next smallest number
    def next(self):
        cur = self.q.pop()
        self.allLeftIntoStack(cur.right)
        return cur.val

    def allLeftIntoStack(self,root):
        while root:
            self.q.append(root)
            root=root.left

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())
