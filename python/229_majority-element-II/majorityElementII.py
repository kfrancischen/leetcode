class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        count_1 = 0
        count_2 = 0
        candidate_1 = 0
        candidate_2 = 0
        for i in range(0, len(nums)):
            if count_1 == 0:
                candidate_1 = nums[i]
                count_1 = 1

            elif nums[i] == candidate_1:
                count_1 += 1

            elif count_2 == 0:
                candidate_2 = nums[i]
                count_2 = 1

            elif nums[i] == candidate_2:
                count_2 += 1

            else:
                count_1 -= 1
                count_2 -= 1

        count_1 = 0
        count_2 = 0
        print candidate_1, candidate_2
        for i in range(0, len(nums)):
            if nums[i] == candidate_1:
                count_1 += 1
            elif nums[i] == candidate_2:
                count_2 += 1

        if count_1 > len(nums) / 3:
            result.append(candidate_1)
        if count_2 > len(nums) / 3:
            result.append(candidate_2)
        return result

mytest = Solution()
s = [2,2,9,3,9,3,9,3,9,3,9,3,9]
print mytest.majorityElement(s)
