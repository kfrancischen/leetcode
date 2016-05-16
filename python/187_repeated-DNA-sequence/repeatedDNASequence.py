class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        result = []
        hashTable = {}
        for i in range(0, len(s) - 9):
            substring = s[i:i+10]
            if substring not in hashTable:
                hashTable[substring] = 1
            else:
                hashTable[substring] += 1
            if hashTable[substring] == 2:
                result.append(substring)

        return result

mytest = Solution()
s = "AAAAAAAAAAAA"
print mytest.findRepeatedDnaSequences(s)
