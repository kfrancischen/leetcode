from collections import defaultdict
class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        result = 0
        for i in range(len(points)):
            dic = defaultdict(int)
            for j in range(len(points)):
                dx = points[i][0] - points[j][0]
                dy = points[i][1] - points[j][1]
                dic[dx**2 + dy**2] += 1

            for key in dic:
                result += dic[key] * (dic[key] - 1)


        return result


mytest = Solution()
nums = [[0,0],[1,0],[2,0]]
print mytest.numberOfBoomerangs(nums)
