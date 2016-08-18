from collections import defaultdict
class Solution(object):
    def findLadders(self, beginWord, endWord, wordlist):
        """
        :type beginWord: str
        :type endWord: str
        :type wordlist: Set[str]
        :rtype: List[List[int]]
        """
        wordlist.add(endWord)
        level = {beginWord}
        parents = defaultdict(set)
        while level and endWord not in parents:
            nextLevel = defaultdict(set)
            for node in level:
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    for i in range(0, len(beginWord)):
                        nextWord = node[:i] + c + node[i+1:]
                        if nextWord in wordlist and nextWord not in parents:
                            nextLevel[nextWord].add(node)
            level = nextLevel
            parents.update(nextLevel)

        result = [[endWord]]
        while result and result[0][0] != beginWord:
            result =[[p] + r for r in result for p in parents[r[0]]]
        return result


mytest = Solution()
begin = 'hit'
end = 'cog'
wordList = set(["hot","dot","dog","lot","log"])
print mytest.findLadders(begin, end, wordList)
