# this file contains the morris traversal for inorder, preorder, and postorder traversal
# time complexity O(n) and space complexity O(1)

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

#=============================================================#
def inorder(root):
    cur = root
    pre = None
    result = []
    while cur:
        if not cur.left:
            result.append(cur.val)
            cur = cur.right
        else:
            prev = cur.left
            while prev.right and prev.right != cur:
                prev = prev.right

            if not prev.right:
                prev.right = cur
                cur = cur.left
            else:
                prev.right = None
                result.append(cur.val)
                cur = cur.right

    return result

#=============================================================#
def preorder(root):
    cur, pre = root, None
    result = []
    while cur:
        if not cur.left:
            result.append(cur.val)
            cur = cur.right
        else:
            prev = cur.left
            while prev.right and prev.right != cur:
                prev = prev.right
            if not prev.right:
                result.append(cur.val)
                prev.right = cur
                cur = cur.left
            else:
                prev.right = None
                cur = cur.right
    return result

#=============================================================#
def reverse(start, end):
    if start == end:
        return
    x, y = start, start.right
    while True:
        z = y.right
        y.right = x
        x = y
        y = z
        if x == end:
            break

def printReverse(start, end, result):
    reverse(start, end)
    p = end
    while True:
        result.append(p.val)
        if p == start:
            break
        p = p.right

def postorder(root):
    result = []
    dummy = TreeNode(0)
    dummy.left = root
    cur, pre = dummy, None
    while cur:
        if not cur.left:
            cur = cur.right
        else:
            prev = cur.left
            while prev.right and prev.right != cur:
                prev = prev.right
            if not prev.right:
                prev.right = cur
                cur = cur.left
            else:
                printReverse(cur.left, prev, result)
                prev.right = None
                cur = cur.right

    return result



#=============================================================#
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
print inorder(n1)
print preorder(n1)
print postorder(n1)
