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
        if not root.left and not root.right and root.val == sum:
            return [[root.val]]

        left_result = self.pathSum(root.left, sum - root.val)
        right_result = self.pathSum(root.right, sum - root.val)

        path = []
        for result in left_result:
            path.append([root.val] + result)
        for result in right_path:
            path.append([root.val] + result)

        return path

