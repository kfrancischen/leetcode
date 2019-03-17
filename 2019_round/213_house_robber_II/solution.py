class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        money_1 = self.getMoney(nums[2:-1]) + nums[0] # rob the first one
        money_2 = self.getMoney(nums[1:-2]) + nums[-1] # rob the last one
        money_3 = self.getMoney(nums[1:-1]) # rob neither of them

        return max(money_1, money_2, money_3)


    def getMoney(self, nums):
        if not nums:
            return 0
        money =  [0] * len(nums)
        for i in range(0, len(nums)):
            if i == 0:
                money[i] = nums[i]
            elif i == 1:
                money[i] = max(nums[i], nums[i - 1])
            else:
                money[i] = max(money[i - 2] + nums[i], money[i - 1])

        return money[-1]