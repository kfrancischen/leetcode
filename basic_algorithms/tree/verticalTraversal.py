class TreeNode:
    def __init__(self, x):
        self.value = x
        self.left = None
        self.right = None


def findMax(node, minimum, maximum, span):
    if not node:
        return
    if span < minimum[0]:
        minimum[0] = span
    elif span > maximum[0]:
        maximum[0] = span

    findMax(node.left, minimum, maximum, span - 1)
    findMax(node.right, minimum, maximum, span + 1)

def verticalLine(node, lineNum, span):
    if not node:
        return None
    if span == lineNum:
        print node.value

    verticalLine(node.left, lineNum, span - 1)
    verticalLine(node.right, lineNum, span + 1)

def verticalOrder(root):
    minimum, maximum = [0], [0]
    findMax(root, minimum, maximum, 0)
    for i in range(minimum[0], maximum[0] + 1):
        verticalLine(root, i, 0)

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
verticalOrder(n1)
