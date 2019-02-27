
class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        result = []
        solution = ""
        self.backTracking(s, result, solution, 0, 0)
        return result

    def backTracking(self, s, result, solution, idx, count):
        if count > 4:
            return
        if count == 4 and idx == len(s):
            result.append(solution)
        for i in range(1, 4):
            if idx + i > len(s):
                break
            string = s[idx:idx + i]
            if (string[0] == "0" and len(string) > 1) or (i == 3 and int(string) >= 256):
                continue
            newSolution = solution + string if count == 3 else solution + string + "."
            self.backTracking(s, result, newSolution, idx + i, count + 1)