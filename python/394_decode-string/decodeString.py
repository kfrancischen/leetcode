class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        for i in range(len(s)):
            char = s[i]
            if char == ']':
                curString = ''
                while stack and stack[-1] != '[':
                    curString += stack.pop()
                curString = curString[::-1]
                stack.pop() # pop the [
                num = ''
                while stack and stack[-1] in '0123456789':
                    num += stack.pop() # pop the number
                num = int(num[::-1])
                stack += curString * num
            else:
                stack.append(char)
        return ''.join(stack)


mytest = Solution()
s = "2[abc]13[d]ef"
print mytest.decodeString(s)
