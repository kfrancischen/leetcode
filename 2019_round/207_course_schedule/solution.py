class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        self.info = [[] for _ in range(0, numCourses)]
        for item in prerequisites:
            self.info[item[0]].append(item[1])

        courses = [i for i in range(0, numCourses)]
        visited = [0] * numCourses
        for i in range(0, numCourses):
            if not self.visit(i, visited):
                return False
        return True


    def visit(self, course, visited):
        if visited[course] == -1:# -1 means it is being visited
            return False
        if visited[course] == 1: # 1 means it has been visited
            return True

        visited[course] = -1

        required = self.info[course]
        for val in required:
            if not self.visit(val, visited):
                return False
        visited[course] = 1
        return True


        
test = Solution()
numCourses = 2
prerequisites = [[1, 0]]
print test.canFinish(numCourses, prerequisites)
