class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: Set[str]
        :rtype: int
        """
        wordList.add(endWord)
        stack = [(beginWord,1)]
        length = 1
        while stack:
            node, length = stack.pop(0)
            if node == endWord:
                return length
            for i in range(len(node)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    nextWord = node[:i] + c + node[i+1:]
                    if nextWord in wordList:
                        wordList.remove(nextWord)
                        stack.append((nextWord, length + 1))
        return 0



mytest = Solution()
begin = 'hit'
end = 'cog'
wordList = ["hot","dot","dog","lot","log"]
print mytest.ladderLength(begin, end, wordList)
