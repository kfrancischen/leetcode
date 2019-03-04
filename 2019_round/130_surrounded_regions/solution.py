class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return
        for i in range(0, len(board)):
            for j in range(0, len(board[0])):
                if i == 0 or i == len(board) - 1 or j == 0 or j == len(board[0]) - 1:
                    self.dfs(board, i, j)
        for i in range(0, len(board)):
            for j in range(0, len(board[0])):
                if board[i][j] == '*':
                    board[i][j] = 'O'
                else:
                    board[i][j] = 'X'
                    
    def dfs(self, board, i, j):
        if board[i][j] == 'X' or board[i][j] == '*':
            return
        board[i][j] = '*'
        if i + 1 < len(board) - 1:
            self.dfs(board, i + 1, j)
        if i - 1 > 0:
            self.dfs(board, i - 1, j)
        if j + 1 < len(board[0]) - 1:
            self.dfs(board, i, j + 1)
        if j - 1 > 0:
            self.dfs(board, i, j - 1)
            