class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        list = []
        parentheses = ['(',')','{','}','[',']']
        matchTable = {')':'(', ']':'[', '}':'{'}
        for str in s:
            if str not in parentheses:
                continue
            if str == '(' or str == '[' or str == '{':
                list.append(str)
            else:
                if len(list) == 0 or matchTable[str] != list.pop():
                    return False

        return len(list) == 0

mytest = Solution()
s = "(){{{{{((123))}}}}}"
print mytest.isValid(s)
