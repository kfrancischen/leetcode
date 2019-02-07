
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def BFS(root):
    if not root:
        return result

    queue = [root]
    count = 1
    result = [root.val]
    while queue:
        node = queue.pop(0)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
        count -= 1
        if count == 0:
            count = len(queue)
            result += [node.val for node in queue] if count != 0 else []
    return result
n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n4 = TreeNode(4)
n5 = TreeNode(5)
n6 = TreeNode(6)
n7 = TreeNode(7)
n1.left = n2
n1.right = n3
n2.left = n4
n2.right = n5
n3.left = n6
n3.right = n7
print BFS(n1)
