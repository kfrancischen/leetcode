# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.q = []
        self.all_left_into_stack(root)
        

    def next(self):
        """
        @return the next smallest number
        :rtype: int
        """
        cur = self.q.pop()
        self.all_left_into_stack(cur.right)
        return cur.val
        

    def hasNext(self):
        """
        @return whether we have a next smallest number
        :rtype: bool
        """
        return len(self.q) != 0
        
    def all_left_into_stack(self, root):
        while root:
            self.q.append(root)
            root = root.left


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()