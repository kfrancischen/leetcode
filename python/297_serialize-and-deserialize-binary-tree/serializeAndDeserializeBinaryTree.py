# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ''
        result = str(root.val)
        stack = [root]
        count = 1
        while count != 0:
            node = stack.pop(0)
            count -= 1
            if node.left:
                stack.append(node.left)
                result += ',' + str(node.left.val)
            else:
                result += ',' + 'null'
            if node.right:
                stack.append(node.right)
                result += ',' + str(node.right.val)
            else:
                result += ',' + 'null'
            if count == 0 and stack:
                count = len(stack)
        return result


    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if len(data) == 0:
            return None
        valList = data.split(',')
        if valList[0] == 'null':
            return None
        root = TreeNode(int(valList.pop(0)))
        stack = [root]
        while valList:
            node = stack.pop(0)
            left = valList.pop(0)
            right = valList.pop(0)
            if left != 'null':
                node.left = TreeNode(int(left))
                stack.append(node.left)
            if right != 'null':
                node.right = TreeNode(int(right))
                stack.append(node.right)
        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
