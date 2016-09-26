class Solution(object):
    def lastRemaining(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = n
        start = 1
        end = n
        direction = 1
        gap = 2
        while start < end:
            if direction:
                if (end-start) % gap == 0:
                    end -= gap / 2
                start = start + gap / 2
                direction = 0
            else:
                if (end - start) % gap == 0:
                    start = start + gap / 2
                end = end - gap/2
                direction = 1
            gap *= 2
        return start


mytest = Solution()
n = 100
print mytest.lastRemaining(n)
