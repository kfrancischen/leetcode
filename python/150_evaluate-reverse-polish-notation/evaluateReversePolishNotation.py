class Solution(object):
    def evalRPN(self, tokens):
        s = []
        for t in tokens:
            if t in ["+", "-", "*", "/"]:
                b = s.pop()
                a = s.pop()
                if t == "+":
                    s.append(a + b)
                if t == "-":
                    s.append(a - b)
                if t == "*":
                    s.append(a * b)
                if t == "/":
                    s.append(int(float(a)/b))
            else:
                s.append(int(t))
        return s.pop()

mytest = Solution()
tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
print mytest.evalRPN(tokens)
