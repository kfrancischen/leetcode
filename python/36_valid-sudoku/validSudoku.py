class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        check_row = [[0 for i in range(0,9)] for j in range(0,9)]
        check_col = [[0 for i in range(0,9)] for j in range(0,9)]
        check_box = [[0 for i in range(0,9)] for j in range(0,9)]

        for i in range(0, 9):
            for j in range(0, 9):
                if board[i][j] == '.':
                    continue
                num = int(board[i][j]) - 1
                k = i/3 * 3 + j/3
                if check_row[i][num] or check_col[j][num] or check_box[k][num]:
                    return False
                check_row[i][num] = 1
                check_col[j][num] = 1
                check_box[k][num] = 1
        return True

mytest = Solution()
s = [".87654321","2........","3........","4........","5........","6........","7........","8........","9........"]
print mytest.isValidSudoku(s)
