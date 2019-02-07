# the easiest way is to make a note of the digits that has been used O(n) extra space
# the buckets needs to be cleared every time

from copy import deepcopy
def radixSort(nums):

    level = 1
    digits = deepcopy(nums)
    while sum(digits):
        buckets = {i:[] for i in range(0, 10)}
        getDigits(digits, nums, buckets, level)
        nums[:] = []
        for val in buckets.values():
            nums += val
        digits = [nums[i] / 10**level for i in range(len(nums))] # one needs to update digits every time
        level += 1
    return nums


def getDigits(digits, nums, buckets, level):
    for i in range(len(nums)):
        buckets[digits[i] % 10].append(nums[i])



nums = [7,6,5,141,3,2,121]
print radixSort(nums)
