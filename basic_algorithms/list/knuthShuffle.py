from random import randint
def knuthShuffle(nums):
    for i in range(len(nums) -1, -1, -1):
        j = randint(0, i)
        nums[i], nums[j] = nums[j], nums[i]


nums = [i for i in range(0, 10)]
knuthShuffle(nums)
print nums
