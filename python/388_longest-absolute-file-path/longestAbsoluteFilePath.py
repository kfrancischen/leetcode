class Solution(object):
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        inputList = input.split('\n')
        stringList = []
        for string in inputList:
            numOfTab = string.count('\t')
            stringList.append(numOfTab)
            stringList.append(string.replace('\t', ''))

        prevLevel = -1
        maxLength = 0
        curLength = 0

        pathList = []
        i = 0
        while i < len(stringList):
            while stringList[i] <= prevLevel:
                prevLevel -= 1
                preDir = pathList.pop()
                curLength -= len(preDir) + 1

            prevLevel = stringList[i]
            pathList.append(stringList[i+1])
            curLength += len(stringList[i+1]) + 1

            if '.' in stringList[i+1]:
                maxLength = max(maxLength, curLength - 1)
            i += 2
        return maxLength

mytest = Solution()
s = "dir"
print mytest.lengthLongestPath(s)
