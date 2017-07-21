# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        return self.recursive(1, n)

    def recursive(self, start, end):
        treeList = []
        for i in range(start, end + 1):
            leftNodes = self.recursive(start, i - 1)
            rightNodes = self.recursive(i + 1, end)

            for leftNode in (leftNodes if len(leftNodes) else [None]):
                for rightNode in (rightNodes if len(rightNodes) else [None]):
                    root = TreeNode(i)
                    root.left, root.right = leftNode, rightNode
                    treeList.append(root)
        return treeList

    
