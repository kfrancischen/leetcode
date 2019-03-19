class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        result = []
        if not nums:
            return result

        last_val = nums[0]
        for i in range(1, len(nums)):
            if nums[i] - nums[i-1] == 1:
                continue
            else:
                if nums[i-1] == last_val:
                    result.append(str(last_val))

                else:
                    result.append(str(last_val) + '->' + str(nums[i-1]))
                last_val = nums[i]

        if nums[-1] == last_val:
            result.append(str(last_val))
        else:
            result.append(str(last_val) + '->' + str(nums[-1]))

        return result


test = Solution()
nums = [0, 1, 2, 4, 5, 7, 8]
print test.summaryRanges(nums)
