class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        if endWord not in wordList:
            return 0
        forward, backward, n, r = {beginWord}, {endWord}, len(beginWord), 2
        while forward and backward:
            if len(forward) > len(backward):
                forward, backward = backward, forward

            next = set()
            for word in forward:
                for i, char in enumerate(word):
                    first, second = word[:i], word[i + 1:]
                    for item in string.ascii_lowercase:
                        candidate = first + item + second
                        if candidate in backward:
                            return r

                        if candidate in wordList:
                            wordList.remove(candidate)
                            next.add(candidate)
            forward = next
            r += 1
        return 0