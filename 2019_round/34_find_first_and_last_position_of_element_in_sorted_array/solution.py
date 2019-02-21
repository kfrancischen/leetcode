class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) == 1 and nums[0] == target:
            return [0, 0]
        def get_left_boundary(nums, target):
            left, right = 0, len(nums) - 1
            while left < right:
                mid = (left + right) / 2
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            if nums[left] == target:
                return left
            if left < len(nums) - 1 and nums[left + 1] ==  target:
                return left + 1

        def get_right_boundary(nums, target):
            left, right = 0, len(nums) - 1
            while left < right:
                mid = (left + right) / 2
                if nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            if nums[right] == target:
                return right
            if right > 0 and nums[right-1] == target:
                return right - 1

        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) / 2
            if nums[mid] == target:
                left_boundary = get_left_boundary(nums[:mid + 1], target)
                right_boudary = get_right_boundary(nums[mid:], target)
                return [left_boundary, right_boudary + mid]
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return [-1, -1]

test = Solution()
nums = [1,2,3,3,3,3,4,5,9]
target = 3
print(test.searchRange(nums=nums, target=target))