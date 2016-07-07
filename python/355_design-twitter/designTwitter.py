class Twitter(object):

    def __init__(self):

        # Global timestamp
        self.timestamp = 1
        # Users table
        self.user_data = {}

    def postTweet(self, userId, tweetId):

        if userId not in self.user_data:
            # Each userId has a tweets list (10 items at most) and a set of followees (include itself)
            self.user_data[userId] = collections.deque(), {userId}

        # Discard outdated tweet
        if len(self.user_data[userId][0]) == 10:
            self.user_data[userId][0].pop()

        self.user_data[userId][0].appendleft((-self.timestamp, tweetId))
        self.timestamp += 1

    def getNewsFeed(self, userId):

        # Use a heap to store all tweets from followees and pick the 10 most recent ones
        if userId not in self.user_data:
            return []

        heap = []
        for uid in self.user_data[userId][1]:
            if uid in self.user_data:
                for tweet in self.user_data[uid][0]:
                    heapq.heappush(heap, tweet)

        res = []
        while len(res) < 10 and heap:
            res.append(heapq.heappop(heap)[1])
        return res


    def follow(self, followerId, followeeId):

        if followerId not in self.user_data:
            self.user_data[followerId] = collections.deque(), {followerId}

        self.user_data[followerId][1].add(followeeId)


    def unfollow(self, followerId, followeeId):

        if followerId not in self.user_data:
            return

        if followerId != followeeId:
            self.user_data[followerId][1].discard(followeeId)



# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
