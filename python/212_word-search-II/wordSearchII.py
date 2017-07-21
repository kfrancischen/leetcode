class TrieNode(object):
    def __init__(self):
        self.word = None
        self.children = {}

class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        root = self.root
        for char in word:
            root = root.children.setdefault(char, TrieNode())
        root.word = word

class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        if not board:
            return []
        tree = Trie()
        for word in words:
            tree.insert(word)
        m, n, r = len(board), len(board[0]), []
        for i, row in enumerate(board):
            for j, _ in enumerate(row):
                self.search(i, j, tree.root, board, m, n, r)
        return r

    def search(self, i, j, root, board, m, n, r):
        char = board[i][j]
        if not (char and char in root.children):
            return

        board[i][j], root = None, root.children[char]

        if root.word:
            r.append(root.word)
            root.word = None

        for x,y in ((0, -1), (-1, 0), (0, 1), (1, 0)):
            ii, jj = i + x, j + y
            if 0 <= ii < m and 0 <= jj < n:
                self.search(ii, jj, root, board, m, n, r)

        board[i][j] = char

mytest = Solution()
words = ["oath","pea","eat","rain"]
boards = [
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
print mytest.findWords(boards, words)
