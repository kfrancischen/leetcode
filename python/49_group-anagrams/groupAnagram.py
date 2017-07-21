class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        stringTable = {}
        for string in strs:
            string = string.lower()
            newString = ''.join(sorted(string))
            if newString not in stringTable:
                stringTable[newString] = [string]
            else:
                stringTable[newString].append(string)

        result = []
        for value in stringTable.values():
            result.append(sorted(value))

        return result

mytest = Solution()
s = ["eat", "tea", "tan", "ate", "nat", "bat"]
print mytest.groupAnagrams(s)
