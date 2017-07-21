from collections import defaultdict
class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        letters = defaultdict(list)
        for i in range(len(s)):
            letters[s[i]].append(i)

        maxLength = 0
        for letter in letters:
            curLength = self.findLength(letters[letter], len(s), k)
            maxLength = max(maxLength, curLength)
        return maxLength

    def findLength(self, positions, n, k):
        maxLength, i, j = 0, 0, 0
        queue = []
        while i < n:
            if j < len(positions) and positions[j] - positions[0] == i:
                queue.append(i)
                j += 1
            else:
                if k == 0:
                    while queue and queue[0] != '*':
                        queue.pop(0)
                    if queue:
                        queue.pop(0)
                        k = 1
                if k > 0:
                    queue.append('*')
                    k -= 1
            i += 1

            maxLength = max(maxLength, len(queue))
        return maxLength


mytest = Solution()
s = "IMNJJTRMJEGMSOLSCCQICIHLQIOGBJAEHQOCRAJQMBIBATGLJDTBNCPIFRDLRIJHRABBJGQAOLIKRLHDRIGERENNMJSDSSMESSTR"
k = 2
print mytest.characterReplacement(s, k)
