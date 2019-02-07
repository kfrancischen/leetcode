def countingSort(nums, k):
    count = [0] * (k + 1)
    result = [0] * len(nums)
    for i in range(0, len(nums)):
        count[nums[i]] += 1

    total = 0
    for i in range(0, k + 1):
        nextTotal = count[i]
        count[i] = total
        total += nextTotal

    for i in range(0, len(nums)):
        result[count[nums[i]]] = nums[i]
        count[nums[i]] += 1

    return result

nums = [5,4,3,2,1,1]
print countingSort(nums, max(nums))
