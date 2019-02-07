class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def traversal(root, result):
    if not root:
        return
    traversal(root.left, result)
    traversal(root.right, result)
    result.append(root.val)

def postorderTraversal(root):
    result = []
    traversal(root, result)
    return result

def postorderTraversalIterative(root):
    result, stack = [], []
    while True:
        while root:
            stack.append(root)
            result.insert(0, root.val)
            root = root.right
        if not stack:
            return result
        node = stack.pop()
        root = node.left


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
print postorderTraversal(n1)
print postorderTraversalIterative(n1)
