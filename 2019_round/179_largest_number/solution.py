class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        if not nums or sum(nums) == 0:
            return '0'

        def comp_rule(s1, s2):
            if s1+s2 < s2+s1:
                return -1
            if s1+s2 > s2+s1:
                return 1
            return 0

        return ''.join(sorted([str(num) for num in nums], cmp = comp_rule, reverse = True))


        