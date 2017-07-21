# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if not root:
            return []
        result = []
        solution = []
        self.backTracking(result, solution, root, sum)
        return result


    def backTracking(self, result, solution, node, sum):
        if not node:
            return
        if node.left == None and node.right == None and sum == node.val:
            result.append(solution + [node.val])
            return
        self.backTracking(result, solution + [node.val], node.left, sum - node.val)
        self.backTracking(result, solution + [node.val], node.right, sum - node.val)
