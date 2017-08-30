from collections import defaultdict
class Solution(object):
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        dic = defaultdict(list)
        for string in strings:
            base = self.helper(string)
            dic[base].append(string)
            
        return dic.values()
        
        
    def helper(self, string):
        diff = ord(string[0]) - ord('a')
        result = ''
        for i in range(len(string)):
            newChar = ord(string[i]) - diff
            if newChar >= ord('a'):
                result += chr(newChar)
            else:
                result += chr(newChar + 26)
        
        return ''.join(result)