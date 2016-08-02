from copy import deepcopy
class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        solution = [['.'] * n for i in range(0, n)]
        result = []
        self.backTracking(solution, result, n, 0)
        return result

    def backTracking(self, solution, result, n, start):
        if start == n:
            copy = []
            for row in solution:
                copy.append(''.join(row))
            result.append(deepcopy(copy))
            return

        for i in range(0, n):
            if solution[start][i] == '.' and self.isvalid(solution, n, start, i):
                solution[start][i] = 'Q'
                self.backTracking(solution, result, n, start + 1)
                solution[start][i] = '.'

    def isvalid(self, solution, n, i, j):
        for row in range(0, n):
            if solution[row][j] == 'Q':
                return False

        for col in range(0, n):
            if solution[i][col] == 'Q':
                return False

        row = i
        col = j
        while row < n and col < n:
            if solution[row][col] == 'Q':
                return False
            row += 1
            col += 1

        row = i
        col = j
        while row < n and col >= 0:
            if solution[row][col] == 'Q':
                return False
            row += 1
            col -= 1

        row = i
        col = j
        while row >= 0 and col < n:
            if solution[row][col] == 'Q':
                return False
            row -= 1
            col += 1

        row = i
        col = j
        while row >= 0 and col >= 0:
            if solution[row][col] == 'Q':
                return False
            row -= 1
            col -= 1

        return True

mytest = Solution()
n = 4
print mytest.solveNQueens(n)
