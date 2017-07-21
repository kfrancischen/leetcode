class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        visited = [0] * numCourses
        result = []
        self.info = [[] for _ in range(0, numCourses)]
        for item in prerequisites:
            self.info[item[0]].append(item[1])

        course = [i for i in range(0, numCourses)]
        for i in range(0, numCourses):
            if not self.dfs(visited, i, result):
                return []

        return result


    def dfs(self, visited, index, result):
        if visited[index] == -1:
            return False
        if visited[index] == 1:
            return True
        visited[index] = -1
        required = self.info[index]
        for val in required:
            if not self.dfs(visited,val, result):
                return False

        result.append(index)
        visited[index] = 1
        return True
