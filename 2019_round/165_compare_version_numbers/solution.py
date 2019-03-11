class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        version1_nums = [int(val) for val in version1.split('.')]
        version2_nums = [int(val) for val in version2.split('.')]

        max_len = min(len(version1_nums), len(version2_nums))
        for i in range(max_len):
            if version1_nums[i] > version2_nums[i]:
                return 1
            elif version1_nums[i] < version2_nums[i]:
                return -1

        if len(version1_nums) > max_len and sum(version1_nums[max_len:]) > 0:
            return 1
        if len(version2_nums) > max_len and sum(version2_nums[max_len:]) > 0:
            return -1

        return 0
