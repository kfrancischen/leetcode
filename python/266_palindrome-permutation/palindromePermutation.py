from collections import Counter
class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        counter = Counter(s)
        num_odd = 0
        for key in counter:
            if counter[key] % 2 == 1:
                num_odd += 1
            if num_odd > 1:
                return False
            
        return True