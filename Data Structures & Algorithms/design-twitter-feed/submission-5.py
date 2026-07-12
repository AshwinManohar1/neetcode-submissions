class Twitter:

    def __init__(self):
        self.users = {}
        self.follow_list = {}
        self.count = 0

    def postTweet(self, userId: int, tweetId: int) -> None:

        if userId not in self.users:
            self.users[userId] = []
        self.count += 1
        self.users[userId].append((self.count , tweetId))


    def getNewsFeed(self, userId: int) -> List[int]:
        
        total_followers_to_show = {userId}
        if userId in self.follow_list:

            total_followers_to_show.update(self.follow_list[userId])
        
        
        posts = []
        min_heap = []


        for followers_id in total_followers_to_show:

            follower_posts = self.users.get(followers_id, [])

            for count , tweetId in follower_posts[-10:]:
                heapq.heappush(min_heap , (count, tweetId))

                if len(min_heap) > 10:
                    heapq.heappop(min_heap)


        news_feed = []
        while min_heap:
            count , tweetId = heapq.heappop(min_heap)
            news_feed.append(tweetId)

        return news_feed[::-1]

    def follow(self, followerId: int, followeeId: int) -> None:

        if followerId not in self.follow_list:
            self.follow_list[followerId] = set()

        self.follow_list[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:

        if followerId in self.follow_list and followeeId in self.follow_list[followerId]:            
            self.follow_list[followerId].remove(followeeId)