import heapq
from copy import deepcopy


class Twitter:

    def __init__(self):
        self.follower_map = dict()
        self.tweet_map = dict()
        self.count = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.count -= 1
        if self.tweet_map.get(userId):
            self.tweet_map[userId].append([self.count, tweetId])
        else:
            self.tweet_map[userId] = [[self.count, tweetId]]

    def getNewsFeed(self, userId: int):
        # get all the followers list
        followers_list = set()

        if self.follower_map.get(userId):
            followers_list = deepcopy(self.follower_map[userId])

        followers_list.add(userId)
        # get all the tweets from the userId and its followers
        pq = []

        for idx in followers_list:
            for tweets in self.tweet_map.get(idx, []):
                heapq.heappush(pq, tweets)
        i = 0
        result = []
        while pq and i < 10:
            result.append(heapq.heappop(pq)[1])
            i += 1

        return result

    def follow(self, followerId: int, followeeId: int) -> None:

        if self.follower_map.get(followerId):
            self.follower_map[followerId].add(followeeId)
        else:
            self.follower_map[followerId] = set([followeeId])

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if self.follower_map.get(followerId):
            try:
                self.follower_map[followerId].remove(followeeId)
            except KeyError as e:
                pass


# Your Twitter object will be instantiated and called as such:
obj = Twitter()
obj.postTweet(1, 5)
obj.postTweet(1, 3)
obj.postTweet(1, 101)
obj.postTweet(1, 13)
obj.postTweet(1, 10)
obj.postTweet(1, 2)
obj.postTweet(1, 94)
obj.postTweet(1, 505)
obj.postTweet(1, 333)
obj.postTweet(1, 22)
obj.postTweet(1, 11)
print(obj.getNewsFeed(1))

# obj.follow(2,1)
# obj.postTweet(2,6)
# print(obj.getNewsFeed(2))
# obj.unfollow(2,1)
# print(obj.getNewsFeed(2))
