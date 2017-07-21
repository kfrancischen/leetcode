class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        stack = []
        preorder = preorder.split(',')
        for item in preorder:
            stack.append(item)

            while len(stack) > 2 and stack[-1] == '#' and stack[-2] == '#':
                if stack[-3] == '#':
                    return False
                stack.pop()
                stack.pop()
                stack.pop()
                stack.append('#')
        return len(stack) == 1 and stack[0] == '#'

mytest = Solution()
s = "1,#,#,#,#"
print mytest.isValidSerialization(s)
