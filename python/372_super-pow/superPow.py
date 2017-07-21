class Solution(object):
    def superPow(self, a, b):
        """
        :type a: int
        :type b: List[int]
        :rtype: int
        """
        if a % 1337 == 0:
            return 0
        p = 0
        for i in b:
            p = (p * 10 + i) % 1140
        if p == 0:
            p += 1140
        return pow(a, p, 1337)

mytest = Solution()
a = 4
b = [1,0,0]
print mytest.superPow(a,b)
