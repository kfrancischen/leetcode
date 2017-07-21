class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        output = []
        i = 0
        j = 1
        while i < len(nums)-3:
            if i != 0 and nums[i - 1] == nums[i]:
                i += 1
                continue
            j = i + 1

            while j < len(nums) - 2:
                if j != i + 1 and nums[j-1] == nums[j]:
                    j += 1
                    continue

                k = j + 1
                l = len(nums) - 1
                while k < l:
                    print i, j, k, l
                    sum = nums[i] + nums[j] + nums[k] + nums[l]
                    if sum < target:
                        k += 1
                    elif sum > target:
                        l -= 1
                    else:
                        output.append([nums[i], nums[j], nums[k], nums[l]])

                        k += 1
                        while k < len(nums) and nums[k - 1] == nums[k]:
                            k += 1
                j += 1
            i += 1



        return output


mytest = Solution()
s = [-4, -1, -1, 0, 1, 2]
target = -1
print mytest.fourSum(s, target)
