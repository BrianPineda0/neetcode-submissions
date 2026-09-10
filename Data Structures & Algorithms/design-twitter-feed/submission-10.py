class Twitter:

    def __init__(self):

        self.post = {}
        self.following = {}
        self.postCount = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.postCount += 1

        if userId not in self.post:
            self.post[userId] = []
            self.post[userId].append((self.postCount, tweetId))
            self.following[userId] = set()
        
        else:
            self.post[userId].append((self.postCount, tweetId))

        

    def getNewsFeed(self, userId: int) -> List[int]:

        res = []

        posts = self.post[userId][:] 

        k = 10

        heapq.heapify(posts)
        
        for followingId in self.following[userId]:

            tenMostRecent = self.post[followingId][-10:]

            for post in tenMostRecent:
                heapq.heappush(posts, post)

            while len(posts) > 10:
                heapq.heappop(posts)

        while len(posts) > 10:
            heapq.heappop(posts)

        while posts:
            prior, item = heapq.heappop(posts)
            res.append(item)

        if res:
            res.reverse()

        return res

        
        

    def follow(self, followerId: int, followeeId: int) -> None:
        
        if followerId not in self.following:
            self.post[followerId] = []
            self.following[followerId] = set()
            self.following[followerId].add(followeeId)

        else:
            self.following[followerId].add(followeeId)

        if followeeId not in self.following:
            self.post[followeeId] = []
            self.following[followeeId] = set()

    def unfollow(self, followerId: int, followeeId: int) -> None:

        self.following[followerId].discard(followeeId)
        
