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
        def helper(nums):
            if not nums:
                return [None]
            result = []
            for i in range(len(nums)):
                left_nodes = helper(nums[:i])
                right_nodes = helper(nums[i+1:])
                for left_node in left_nodes:
                    for right_node in right_nodes:
                        root = TreeNode(nums[i])
                        if left_node is not None:
                            root.left = left_node
                        if right_node is not None:
                            root.right = right_node
                        result.append(root)
            return result
        if n == 0:
            return []
        nums = range(1, n+1)
        return helper(nums)
            