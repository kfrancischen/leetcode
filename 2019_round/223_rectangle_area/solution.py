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
        left_corner = [max(A, E), max(B, F)]
        right_corner = [min(C, G), min(D, H)]
        cross = 0
        if left_corner[0] < right_corner[0] and left_corner[1] < right_corner[1]:
            cross = (right_corner[0] - left_corner[0]) * (right_corner[1] - left_corner[1])
        return (C - A) * (D - B) + (G - E) * (H - F) - cross