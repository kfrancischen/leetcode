class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        stringList = str.split()
        hashTable_str = {}
        hashTable_pat = {}
        if len(pattern) != len(stringList):
            return False
        for i in range(0, len(pattern)):
            if stringList[i] not in hashTable_str:
                hashTable_str[stringList[i]] = pattern[i]
            if pattern[i] not in hashTable_pat:
                hashTable_pat[pattern[i]] = stringList[i]
            if hashTable_str[stringList[i]] != pattern[i] or hashTable_pat[pattern[i]] != stringList[i]:
                return False
        return True

mytest = Solution()
pattern = "abba"
str = "dog cat cat fish"
print mytest.wordPattern(pattern, str)
