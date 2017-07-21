class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        self.table = {"1":["*"], "2":["a","b","c"], "3":["d", "e", "f"], "4":["g", "h", "i"], \
         "5":["j","k","l"], "6":["m", "n", "o"], "7":["p", "q", "r", "s"], "8":["t", "u", "v"], "9":["w","x","y","z"]}
        result = []
        if not digits:
            return result
        self.backTracking(digits, result, 0)
        return result

    def backTracking(self, digits, result, start):
        if start == len(digits) - 1:
            result.extend(self.table[digits[start]])
            return
        self.backTracking(digits, result, start + 1)
        letters = self.table[digits[start]]
        length = len(result)
        for i in range(0, length):
            for letter in letters:
                result.append(letter + result[i])
        for i in range(0, length):
            result.remove(result[0])


mytest = Solution()
digits = "123"
print mytest.letterCombinations(digits)
