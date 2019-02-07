# using a balanced tree, the union and find operation takes time logn


# first implementation, worst case O(n)
class UnionFind1:
    def __init__(self, nums):
        self.roots = [i for i in range(len(nums))]
        self.nums = nums

    def root(self, i):
        # this function finds the root of i where i blongs to
        while self.roots[i] != i:
            i = self.roots[i]

        return i
    def union(self, a, b):
        root_a = self.root(a)
        root_b = self.root(b)
        self.roots[root_a] = root_b

    def find(self, a, b):
        return self.root(a) == self.root(b)


nums = [1,2,3,4,5]
unionFind1 = UnionFind1(nums)
print unionFind1.find(1,2)
unionFind1.union(1,2)
print unionFind1.find(1,2)

unionFind1.union(3,4)
print unionFind1.find(1,3)
unionFind1.union(1,3)
print unionFind1.find(1,3)


# second implementation, balanced tree, O(lgn)
class UnionFind2:
    def __init__(self, nums):
        self.roots = [i for i in range(len(nums))]
        self.sizes = [1] * len(nums)
        self.nums = nums

    def root(self, i):
        # this function finds the root of i where i blongs to
        while self.roots[i] != i:
            i = self.roots[i]

        return i
    def union(self, a, b):
        root_a = self.root(a)
        root_b = self.root(b)
        if self.sizes[root_a] < self.sizes[root_b]:
            self.roots[root_a] = root_b
            self.sizes[root_b] += self.sizes[root_a]
        else:
            self.roots[root_b] = root_a
            self.sizes[root_a] = self.sizes[root_b]

    def find(self, a, b):
        return self.root(a) == self.root(b)

unionFind2 = UnionFind2(nums)
print unionFind2.find(1,2)
unionFind2.union(1,2)
print unionFind2.find(1,2)

unionFind2.union(3,4)
print unionFind2.find(1,3)
unionFind2.union(1,3)
print unionFind2.find(1,3)
