# this is taken from leetcode P307 about sum range query
# complexity: O(log n) for both update and query
class Node:
    def __init__(self, start, end):
        self.start = start   # the start index of the interval in the nums (inclusive)
        self.end = end  # the end index of the interval in the nums (inclusive)
        self.total = 0  # the sum of nums in the interval
        self.left = None    # left child
        self.right = None   # right child


class SegmentTree:
    def __init__(self, nums):
        self.nums = nums
        self.root = self.createTree(0, len(nums) - 1)

    def createTree(self, l, r):
        if l > r:
            return None
        if l == r:
            n = Node(l, r)
            n.total = self.nums[l]
            return n

        mid = (l + r) / 2
        root = Node(l, r)
        root.left = self.createTree(l, mid)
        root.right = self.createTree(mid + 1, r)
        root.total = root.left.total + root.right.total

        return root

    def update(self, root, i, val):
        if root.start == root.end:
            root.total = val
            return
        mid = (root.start + root.end) / 2
        if i <= mid:
            self.update(root.left, i, val)
        else:
            self.update(root.right, i, val)
        root.total = root.left.total + root.right.total # after update, update the total of the root

    def query(self, root, i, j):
        if root.start == i and root.end == j:
            return root.total
        mid = (root.start + root.end) / 2
        if j <= mid:                        # seperate by the mid index
            return self.query(root.left, i, j)
        elif i >= mid + 1:
            return self.query(root.right, i, j)
        else:           # a mixture of left side and right side
            return self.query(root.left, i, mid) + self.query(root.right, mid + 1, j)


nums = [1,2,3,4,5]
segmentTree = SegmentTree(nums)
print segmentTree.root.total
print segmentTree.query(segmentTree.root, 0, 3)

segmentTree.update(segmentTree.root, 0, 4)
print segmentTree.root.total
print segmentTree.query(segmentTree.root, 0, 3)
