class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = s.split()
        result = []
        for word in words[::-1]:
            word = word.lstrip().rstrip()
            result.append(result)

        return ' '.join(result)
