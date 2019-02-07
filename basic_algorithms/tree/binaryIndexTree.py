# the advantages of Binary Indexed Tree over Segment are,
# requires less space and very easy to implement
# complexity: O(log n) for both update and query


class BinaryIndexTree:
    def __init__(self, nums):
        self.tree = self.createTree(nums, len(nums))

    def createTree(self, nums, n):
        tree = [0] * (n+1)
        for i in range(n):
            self.update(tree, i, n, nums[i])
        return tree

    def update(self, tree, i, n, val):
        # the val is the number that is going to be added to nums[i]
        i += 1
        while i <= n:
            tree[i] += val
            i += i & (-i)    # update the index of the parent in the update view

        return

    def query(self, tree, i):
        # returns the sum of s[0...i], inclusive
        s = 0
        i += 1
        while i > 0:
            s += tree[i]
            i -= i & (-i) # update the index of the parent in the query view

        return s

nums = [1,2,3,4,5,6]
bitTree = BinaryIndexTree(nums)
print bitTree.query(bitTree.tree, 3)

bitTree.update(bitTree.tree, 2, len(nums), 5)
print bitTree.query(bitTree.tree, 3)
