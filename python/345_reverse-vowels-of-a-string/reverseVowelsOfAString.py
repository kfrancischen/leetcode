class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s or len(s) == 1:
            return s
        s = list(s)
        pointer_1 = 0
        pointer_2 = len(s) -  1
        vowels = ['a','e','i','o','u','A','E','I','O','U']
        while pointer_1 < pointer_2:
            if s[pointer_1] in vowels and s[pointer_2] in vowels:
                s[pointer_1], s[pointer_2] = s[pointer_2], s[pointer_1]
                pointer_1 += 1
                pointer_2 -= 1
            if s[pointer_1] not in vowels:
                pointer_1 += 1
            if s[pointer_2] not in vowels:
                pointer_2 -= 1
        return "".join(s)

mytest = Solution()
s = "ai"
print mytest.reverseVowels(s)
