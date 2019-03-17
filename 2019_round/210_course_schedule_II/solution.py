from collections import defaultdict
class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        edge_map = defaultdict(list)
        for edge in prerequisites:
            edge_map[edge[0]].append(edge[1])


        result = []
        visited = [0] * numCourses
        for i in range(numCourses):
            if not self.dfs(visited, i, result, edge_map):
                return []

        return result



    def dfs(self, visited, val, result, edge_map):
        if visited[val] == -1:
            return False

        if visited[val] == 1:
            return True

        visited[val] = -1
        for course in edge_map[val]:
            if not self.dfs(visited, course, result, edge_map):
                return False
            
        result.append(val)
        visited[val] = 1
        return True

test = Solution()
numCourses = 4
prerequisites = [[1,0],[2,0],[3,1],[3,2]]
print test.findOrder(numCourses, prerequisites)