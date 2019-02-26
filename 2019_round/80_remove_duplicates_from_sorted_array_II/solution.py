class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        first_pointer = 0
        second_pointer = 1
        length = 1

        while second_pointer < len(nums):
            if nums[second_pointer] != nums[first_pointer]:
                nums[length] = nums[second_pointer]
                length += 1
                first_pointer = second_pointer

            else:
                if second_pointer - first_pointer < 2:
                    nums[length] = nums[second_pointer]
                    length += 1
            second_pointer += 1

        return length
