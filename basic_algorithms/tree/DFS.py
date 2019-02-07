class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
'''
def DFS(root, result):
    if not root:
        return
    result.append(root.val)
    if root.left:
        DFS(root.left, result)
    if root.right:
        DFS(root.right, result)
'''
def DFS(root):
    result = []
    if not root:
        return result
    path = str(root.val) + '+'
    callDFS(root, result, path)
    return result

def callDFS(root, result, path):
    if root.left == None and root.right == None:
        result.append(path[:-1])
    if root.left:
        callDFS(root.left, result, path + str(root.left.val) + '+')
    if root.right:
        callDFS(root.right, result, path + str(root.right.val) + '+')

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
result = []
print DFS(n1)
