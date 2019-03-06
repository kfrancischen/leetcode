class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for i in range(len(tokens)):
            if tokens[i] not in '+-*/':
                stack.append(tokens[i])
            else:
                val_1 = int(stack.pop())
                val_2 = int(stack.pop())
                val = self.operation(val_2, val_1, tokens[i])
                stack.append(val)


        return int(stack.pop())
    
    def operation(self, val1, val2, op):
        if op == '+':
            return val1 + val2
        if op == '-':
            return val1 - val2

        if op == '*':
            return val1 * val2
        else:
            sign = 1
            if val1 * val2 < 0:
                sign = -1
            return abs(val1) / abs(val2) * sign