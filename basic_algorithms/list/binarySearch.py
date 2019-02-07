def binarySearch(nums, target):
    l = 0
    r = len(nums) - 1
    while l <= r:
        mid = (l + r) / 2
        if nums[mid] == target:
            return True
        elif target < nums[mid]:
            r = mid - 1
        elif nums[mid] < target:
            l = mid + 1
    return False


nums = [1,3,4,5,7,8,8,10]
target = 8
print binarySearch(nums, target)
