class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """

        result = []
        left = 0
        right = 0
        if len(nums) == 1:
            result.append(str(nums[0]))

        for i in range(0, len(nums) - 1):
            if nums[i+1]  - nums[i] == 1:
                right += 1
                if right != len(nums) - 1:
                    continue

            if left != right:
                string = str(nums[left]) + "->" + str(nums[right])
            else:
                string = str(nums[left])
            result.append(string)
            right += 1
            left = right
            if right == len(nums) - 1 and nums[right] - nums[right - 1] != 1:
                result.append(str(nums[len(nums) - 1]))
        return result

mytest = Solution()
s = [0,1,2,4,5]
print mytest.summaryRanges(s)
