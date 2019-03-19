from copy import deepcopy
class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        str_list = []
        cur_str = ''
        for i in range(len(s)):
            if s[i] == ' ':
                continue
            if s[i] in '+-*/':
                str_list.append(int(cur_str))
                str_list.append(s[i])
                cur_str = ''
            else:
                cur_str += s[i]

        if cur_str:
            str_list.append(int(cur_str))

        result_1 = []
        cnt = 0
        while cnt < len(str_list):
            if str_list[cnt] == '*':
                last_val = result_1.pop()
                result_1.append(last_val * str_list[cnt + 1])
                cnt += 2
            elif str_list[cnt] == '/':
                last_val = result_1.pop()
                result_1.append(last_val / str_list[cnt + 1])
                cnt += 2
            else:
                result_1.append(str_list[cnt])
                cnt += 1

        result = []
        cnt = 0
        while cnt < len(result_1):
            if result_1[cnt] == '+':
                last_val = result.pop()
                result.append(last_val + result_1[cnt + 1])
                cnt += 2
            elif result_1[cnt] == '-':
                last_val = result.pop()
                result.append(last_val - result_1[cnt + 1])
                cnt += 2
            else:
                result.append(result_1[cnt])
                cnt += 1

        return result[-1]





test = Solution()
s =" 3+5 / 2 "
print test.calculate(s)
