class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        minCandy = 1
        candies = [1] * len(ratings)
        for i in range(0, len(ratings) - 1):
            if ratings[i] < ratings[i + 1]:
                candies[i+1] = 1 + candies[i]
        for i in range(len(ratings) - 1, 0, -1):
            if ratings[i] < ratings[i-1]:
                candies[i-1] = max(candies[i-1], candies[i] + 1)
                
        return sum(candies)


mytest = Solution()
ratings = [0,3,4,2,4,6,3,2,1]
print mytest.candy(ratings)
