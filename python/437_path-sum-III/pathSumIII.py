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
        :rtype: int
        """
        if not root:
            return 0
        queue = [(root, [0, root.val])]
        count = 1
        result = 0
        while queue:
            node, pathSumList = queue.pop(0)
            count -= 1
            for i in range(len(pathSumList)):
                if pathSumList[i] == sum:
                    if sum == 0 and i == 0:
                        continue
                    result += 1
            if node.left:
                newPath = [0]
                for num in pathSumList:
                    newPath.append(num + node.left.val)
                queue.append((node.left, newPath))
            if node.right:
                newPath = [0]
                for num in pathSumList:
                    newPath.append(num + node.right.val)
                queue.append((node.right, newPath))

            if count == 0 and queue:
                count = len(queue)

        return result
