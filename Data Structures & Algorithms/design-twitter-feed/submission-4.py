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
        for followers_id in total_followers_to_show:

            follower_posts = self.users.get(followers_id, [])
            # count , tweetId
            posts.extend(follower_posts)

        sorted_posts = sorted(posts , key=lambda x: x[0], reverse=True)

        return [post[1] for post in sorted_posts[:10]]
        
    def follow(self, followerId: int, followeeId: int) -> None:

        if followerId not in self.follow_list:
            self.follow_list[followerId] = set()

        self.follow_list[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:

        if followerId in self.follow_list and followeeId in self.follow_list[followerId]:            
            self.follow_list[followerId].remove(followeeId)