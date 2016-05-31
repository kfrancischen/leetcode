class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        overlay = min(D-B, H-F, max(D-F,0), max(H-B,0)) * min(C-A, G-E, max(C-E,0), max(G-A,0))

        area_1 = abs(A - C) * abs(B - D)
        area_2 = abs(E - G) * abs(F - H)

        return area_1 + area_2 - overlay


mytest = Solution()
A = -3
B = 0
C = 3
D = 4
E = 0
F = -1
G = 9
H = 2
print mytest.computeArea(A, B, C, D, E, F, G, H)
