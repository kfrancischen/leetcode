class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        if len(board) == 0 or len(board[0]) == 0:
            return

        for i in range(len(board)):
            for j in range(len(board[0])):
                neighbor = self.getNeighbor(board, i, j)
                if board[i][j] == 0:
                    if neighbor == 3:
                        board[i][j] = 2
                else:
                    if neighbor == 2 or neighbor == 3:
                        board[i][j] = 3
        for i in range(len(board)):
            for j in range(len(board[0])):
                board[i][j] >>= 1


    def getNeighbor(self, board, row, column):
        num = 0
        for i in range(row - 1, row + 2):
            for j in range(column - 1, column + 2):
                if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
                    continue
                if i == row and j == column:
                    continue
                num += board[i][j] & 1
        return num