def partition(nums, l, h):
    pivot = nums[h]
    i = l
    for j in range(l, h):
        if nums[j] <= pivot:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
    nums[i], nums[h] = nums[h], nums[i]
    return i

def quickSort(nums, l, h):
    if l < h:
        p = partition(nums, l, h)
        quickSort(nums, l, p-1)
        quickSort(nums, p+1, h)

nums = [5,4,3,2,1]
quickSort(nums, 0, len(nums) - 1)
print nums
