class Solution(object):
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        r = sum(nums)
        l = max(nums)
        if m == 1:
            return r

        while l <= r:
            mid = l + (r - l) / 2
            if self.valid(mid, nums, m):
                r = mid - 1
            else:
                l = mid + 1

        return l

    def valid(self, mid, nums, m):
        count, total = 1, 0
        for num in nums:
            total += num
            if total > mid:
                total = num
                count += 1
                if count > m:
                    return False


        return True

mytest = Solution()
nums = [1,2,3,4,5]
m = 2
print mytest.splitArray(nums, m)
