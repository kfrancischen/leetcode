class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 0:
            return 0

        if len(nums) == 1:
            return nums[0]

        if len(nums) == 2:
            return nums[0] + nums[1]

        nums = sorted(nums)
        output = nums[0] + nums[1] + nums[2]
        for i in range(0, len(nums)-1):
            j = i + 1
            k = len(nums) - 1
            while j != k:
                sum = nums[i] + nums[j] + nums[k]
                if sum > target:
                    k -= 1
                else:
                    j += 1

                if abs(output - target) > abs(sum - target):
                    output = sum


        return output