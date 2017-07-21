class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n <= 0:
            return []
        result = [str(i) for i in range(1, n + 1)]
        for i in range(n/3):
            result[3 * i + 2] = 'Fizz'

        for i in range(n/5):
            result[5*i + 4] = 'Buzz' if result[5*i + 4] != 'Fizz' else 'FizzBuzz'


        return result

mytest = Solution()
n = 15
print mytest.fizzBuzz(n)
