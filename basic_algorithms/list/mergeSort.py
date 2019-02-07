from copy import deepcopy
def merge(nums, p, q, r):
    array = []
    i = j = 0
    while i < q - p + 1 and j < r - q:
        if nums[i + p] < nums[j + q + 1]:
            array.append(nums[i + p])
            i += 1
        else:
            array.append(nums[j + q + 1])
            j += 1
    array.extend(nums[(i+p):(q+1)])
    array.extend(nums[(j+q+1):(r+1)])
    nums[p:(r+1)] = deepcopy(array)


def mergeSort(nums, p, r):
    if p < r:
        q = (p + r) / 2
        mergeSort(nums, p, q)
        mergeSort(nums, q + 1, r)
        merge(nums, p, q, r)

    return

nums = [5,4,3,2,1]
mergeSort(nums, 0, len(nums) - 1)
print nums
