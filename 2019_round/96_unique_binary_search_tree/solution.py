class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        cache = [-1] * (n + 1)
        def countTree(n, cache):
            if n == 0 or n == 1:
                return 1
            if cache[n] != -1:
                return cache[n]

            numOfTree = 0
            for i in range(0, n):
                numOfTree += countTree(i, cache) * countTree(n - 1 - i, cache)
            cache[n] = numOfTree
            return numOfTree
        
        return countTree(n, cache)
