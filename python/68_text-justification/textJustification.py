class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        for word in words:
            if len(word) > maxWidth:
                return []
        result = []
        self.justify(result, words, maxWidth)
        lastLine = result[-1]
        lastLine = ' '.join(lastLine.split())
        result[-1] = lastLine + ' ' * (maxWidth - len(lastLine))
        return result

    def justify(self, result, words, maxWidth):
        if not words:
            return
        wordList = [words[0]]
        string = words[0]
        summation = len(words[0])
        for word in words[1:]:
            if summation + len(word) + len(wordList) <= maxWidth:
                wordList.append(word)
                summation += len(word)
            else:
                break

        if len(wordList) == 1:
            string += ' ' * (maxWidth - len(wordList[0]))
        else:
            aveSpace = (maxWidth - summation) / (len(wordList) - 1)
            extraSpace = maxWidth - summation - aveSpace * (len(wordList) - 1)
            for word in wordList[1:]:
                if extraSpace > 0:
                    string += ' ' * (aveSpace + 1) + word
                    extraSpace -= 1
                else:
                    string += ' ' * aveSpace + word

        result.append(string)
        self.justify(result, words[len(wordList):], maxWidth)

mytest = Solution()
s = ["This", "is", "an", "example", "of", "text", "justification."]
L = 13
print mytest.fullJustify(s, L)
