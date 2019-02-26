class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        def dfs(i, j, m, n, word, visited):
            
            if len(word) == 0:
                return True
            
            if i >= m or j >= n or i < 0 or j < 0 or visited[i][j] or board[i][j] != word[0]:
                return False
            else:
                visited[i][j] = True
                result = dfs(i+1, j, m, n, word[1:], visited) or dfs(i, j+1, m, n, word[1:], visited) or dfs(i-1, j, m, n, word[1:], visited) or dfs(i, j-1, m, n, word[1:], visited)
                visited[i][j] = False
                return result
                    
            
        
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                visited = [[False] * n for _ in range(m)]
                if dfs(i, j, m, n, word, visited):
                    return True
                
        return False