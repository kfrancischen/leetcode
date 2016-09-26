class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        def compare(a, b):
            return b[0] - a[0] if a[0] != b[0] else a[1] - b[1]
        sortedQueue = sorted(people, cmp=compare)
        result = []
        for person in sortedQueue:
            result.insert(person[1], person)
        return result

mytest = Solution()
s = [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
print mytest.reconstructQueue(s)
