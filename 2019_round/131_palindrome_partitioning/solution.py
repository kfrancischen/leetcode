class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        if not s:
            return []
        if len(s) == 1:
            return [[s]]
        result = []
        for i in range(1, len(s)+1):
            if s[:i] == s[:i][::-1]:
                right_results = self.partition(s[i:])
                if right_results:
                    for right_result in right_results:
                        result.append([s[:i]] + right_result)
                else:
                    result.append([s[:i]])
                    
        return result
        