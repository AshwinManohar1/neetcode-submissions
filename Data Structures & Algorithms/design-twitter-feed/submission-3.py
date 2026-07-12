from typing import List

class Twitter:

    def __init__(self):
        self.users = {}       # userId -> list of (count, tweetId)
        self.follow_list = {} # followerId -> SET of followeeIds (prevents duplicates)
        self.count = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.users:
            self.users[userId] = []
        self.count += 1
        self.users[userId].append((self.count, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        # Always start with the user themselves (wrapped in a set)
        total_followers_to_show = {userId}
        
        # FIX 1: Check follow_list independently from self.users
        if userId in self.follow_list:
            # .update() merges elements from the follow set into our total set
            total_followers_to_show.update(self.follow_list[userId])
            
        posts = []
        for followers_id in total_followers_to_show:
            follower_posts = self.users.get(followers_id, [])
            posts.extend(follower_posts)

        sorted_posts = sorted(posts, key=lambda x: x[0], reverse=True)

        # FIX 3: Slice the array to return only the top 10 results
        return [post[1] for post in sorted_posts[:10]]

    def follow(self, followerId: int, followeeId: int) -> None:
        # Prevent a user from following themselves
        if followerId == followeeId:
            return

        # FIX 2: Use a set instead of a list to completely ignore duplicate follow calls
        if followerId not in self.follow_list:
            self.follow_list[followerId] = set()

        self.follow_list[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        # Safe check to see if the user actually follows them before removing
        if followerId in self.follow_list and followeeId in self.follow_list[followerId]:
            self.follow_list[followerId].remove(followeeId)
