from collections import defaultdict
class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        counts = defaultdict(int)
        result = []
        for i in range(len(s)):
            if i + 10 > len(s):
                break
            else:
                counts[s[i:i+10]] += 1

                if counts[s[i:i+10]] == 2:
                    result.append(s[i:i+10])


        return result

        