from collections import Counter
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        counter = Counter(s)
        hasOdd = False
        result = 0
        for key in counter.keys():
            if counter[key] % 2 == 0:
                result += counter[key]

            else:
                result += counter[key] - 1
                hasOdd = True

        return result + 1 if hasOdd else result

mytest = Solution()
s = "abccccdd"
print mytest.longestPalindrome(s)
