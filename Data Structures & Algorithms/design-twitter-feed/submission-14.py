class Twitter:

    def __init__(self):
        self.post = defaultdict(list)        # CHANGE: defaultdict kills the init branching
        self.following = defaultdict(set)
        self.postCount = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.postCount += 1
        self.post[userId].append((self.postCount, tweetId))   # no if/else needed

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        posts = self.post[userId][:]         # safe now — missing user → []
        heapq.heapify(posts)

        for followingId in self.following[userId]:
            for post in self.post[followingId][-10:]:
                heapq.heappush(posts, post)

        while len(posts) > 10:          # trim as you go
            heapq.heappop(posts)

        while posts:
            _, item = heapq.heappop(posts)
            res.append(item)

        res.reverse()                        # min-heap popped ascending → reverse for recent-first
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)   # defaultdict auto-creates

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)