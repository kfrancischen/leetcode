from collections import Counter
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        ransomCounter = Counter(ransomNote)
        magazineCounter = Counter(magazine)
        for item in ransomCounter:
            if item not in magazineCounter or ransomCounter[item] > magazineCounter[item]:
                return False

        return True

mytest = Solution()
ransomNote = 'a'
magazine = 'ab'
print mytest.canConstruct(ransomNote, magazine)
