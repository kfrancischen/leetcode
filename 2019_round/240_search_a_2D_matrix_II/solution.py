class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False
        for i in range(0, len(matrix)):
            columnIdx = self.binarySearch(matrix[i], target)
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

test = Solution()
matrix = [
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
target = 5
print test.searchMatrix(matrix, target)
