from collections import defaultdict
class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        d = defaultdict(list)
        for flight in tickets:
            d[flight[0]] += flight[1],
        self.route = ["JFK"]

        def dfs(start = "JFK"):
            if len(self.route) == len(tickets) + 1:
                return self.route
            myDsts = sorted(d[start])
            for dst in myDsts:
                d[start].remove(dst)
                self.route += dst,
                worked = dfs(dst)
                if worked:
                    return worked
                self.route.pop()
                d[start] += dst,
        return dfs()

mytest = Solution()
s = [["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]
print mytest.findItinerary(s)
