class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        result = []
        i = 0
        exist = False
        while True:
            common = True
            for j in range(0, len(strs)):
                if i >= len(strs[j]):
                    exist = True
                    break
                if strs[0][i] != strs[j][i]:
                    common = False
            if exist:
                break

            if common:
                result.append(strs[0][i])
            else:
                break
            i += 1

        return "".join(result) if len(result) else ""

mytest = Solution()
strs = ["aca", "cba"]
print mytest.longestCommonPrefix(strs)
