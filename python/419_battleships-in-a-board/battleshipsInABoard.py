class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        if not board or not board[0]:
            return 0
        m, n = len(board), len(board[0])
        visited = [[False] * n for _ in range(m)]
        result = 0
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'X' and visited[i][j] == False:
                    self.dfs(board, i, j, m, n, visited)
                    result += 1

        return result

    def dfs(self, board, i, j, m, n, visited):
        visited[i][j] == True
        while i < m - 1:
            if board[i+1][j] == 'X':
                visited[i+1][j] = True
                i+=1
            else:
                break

        while j < n - 1:
            if board[i][j+1] == 'X':
                visited[i][j+1] = True
                j += 1
            else:
                break

mytest = Solution()
board = ["X..X","...X","...X"]
print mytest.countBattleships(board)
