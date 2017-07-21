class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        numOfChar = 256
        visited = [-1] * numOfChar
        if s == "":
            return 0
            
        currentLength = 1
        maxLength = 1
        visited[ord(s[0])] = 0

        for index in range(1, len(s)):
            character = s[index]
            if visited[ord(character)] == -1 or currentLength + visited[ord(character)] < index:
                currentLength += 1
            else:
                if currentLength > maxLength:
                    maxLength = currentLength

                currentLength = index - visited[ord(character)]

            visited[ord(character)] = index

        if currentLength > maxLength:
            maxLength = currentLength

        return maxLength


s1 = "abcd"
s2 = "abcabcbb"
mytest = Solution()
print mytest.lengthOfLongestSubstring(s1)
print mytest.lengthOfLongestSubstring(s2)
