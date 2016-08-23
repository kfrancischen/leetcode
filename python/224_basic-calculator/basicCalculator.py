class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        items = []
        curString = ''
        for char in s:
            if char == ' ':
                continue
            if char in '()+-':
                if curString != '':
                    items.append(curString)
                items.append(char)
                curString = ''
            else:
                curString += char
        if curString != '':
            items.append(curString)

        stack = []
        for item in items:
            if item in '(+-':
                stack.append(item)
            elif item == ')':
                num1 = int(stack.pop())
                stack.pop()
                while stack and stack[-1] != '(':
                    operator = stack.pop()
                    preNum = int(stack.pop())
                    num1 = self.compute(operator, preNum, num1)
                stack.append(str(num1))
            # if are numbers
            else:
                curNum = int(item)
                while stack and stack[-1] != '(':
                    operator = stack.pop()
                    preNum = int(stack.pop())
                    curNum = self.compute(operator, preNum, curNum)
                stack.append(str(curNum))

        stack.reverse()
        while len(stack) != 1:
            num1 = int(stack.pop())
            operator = stack.pop()
            num2 = int(stack.pop())
            stack.append(str(self.compute(operator, num1, num2)))

        return int(stack[0])

    def compute(self, operator, num1, num2):
        if operator == '+':
            return num1 + num2
        else:
            return num1 - num2



mytest = Solution()
s = "(2-(2-3))"
print mytest.calculate(s)
