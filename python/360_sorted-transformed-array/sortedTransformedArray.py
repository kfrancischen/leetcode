class Solution(object):
    def sortTransformedArray(self, nums, a, b, c):
        """
        :type nums: List[int]
        :type a: int
        :type b: int
        :type c: int
        :rtype: List[int]
        """
        if a == 0:
            result = [ b * val + c for val in nums]
            return result if b > 0 else result[::-1]
        mid = -b / (2.0 * a)
        left, right = [], []
        for val in nums:
            if val <= mid:
                left.append( a*val**2 + b*val + c)
            else:
                right.append( a*val**2 + b*val + c )
        if a > 0:
            left = left[::-1]
        else:
            right = right[::-1]

        pointer_1 = pointer_2 = 0
        result = []
        while pointer_1 < len(left) and pointer_2 < len(right):
            if left[pointer_1] < right[pointer_2]:
                result.append(left[pointer_1])
                pointer_1 += 1
            else:
                result.append(right[pointer_2])
                pointer_2 += 1

        if pointer_1 != len(left):
            result += left[pointer_1:]
        if pointer_2 != len(right):
            result += right[pointer_2:]
            
        return result
        