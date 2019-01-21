class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        current_length, max_length = 1, 1
        num_of_char = 256
        visited = [-1] * num_of_char
        visited[ord(s[0])] = 0

        for i in range(1, len(s)):
            character = s[i]
            if visited[ord(character)] == -1 or current_length + visited[ord(character)] < i:
                current_length += 1
            else:
                max_length = max(max_length, current_length)
                current_length = i - visited[ord(character)]

            visited[ord(character)] = i

        return max(max_length, current_length)
