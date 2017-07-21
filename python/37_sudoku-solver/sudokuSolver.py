class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board or len(board[0]) != 9:
            return
        for i in range(0, 9):
            board[i] = list(board[i])

        self.solveBoard(board)


    def solveBoard(self, board):
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == '.':
                    for choice in "123456789":
                        if self.isValidSudoku(board, i, j, choice):
                            board[i][j] = choice

                        if self.solveBoard(board):
                            return True
                        else:
                            board[i][j] = '.'
                return False
        return True


    def isValidSudoku(self, board, i, j, choice):
        for row in range(0, 9):
            if board[row][j] == choice:
                return False

        for col in range(0, 9):
            if board[i][col] == choice:
                return False

        for row in range(0,3):
            for col in range(0, 3):
                if board[(i/3)*3 + row][(j/3)*3 + col] == choice:
                    return False
        return True

mytest = Solution()
s = ["..9748...","7........",".2.1.9...","..7...24.",".64.1.59.",".98...3..","...8.3.2.","........6","...2759.."]
mytest.solveSudoku(s)
print s
