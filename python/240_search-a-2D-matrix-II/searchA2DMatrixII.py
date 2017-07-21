class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return Falser
        for i in range(0, len(matrix)):
            columnIdx = self.binarySearch(matrix[i], target)
            print columnIdx
            if matrix[i][columnIdx] == target:
                return True
        return False

    def binarySearch(self, list, target):
        left = 0
        right = len(list) - 1

        while left + 1 < right:
            mid = (left + right) / 2
            if target == list[mid]:
                return mid
            if target < list[mid]:
                right = mid
            elif list[mid] < target:
                left = mid
        return left if target < list[right] else right

mytest = Solution()
s = [[5],[6]
]

target = 6
print mytest.searchMatrix(s, target)
