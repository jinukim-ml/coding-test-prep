from typing import List
import heapq

class Twitter:
    def __init__(self):
        self.subscribtion = {} # val users followed by user (include themself)
        self.tweets = {}
        self.postnum = 0
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId] = self.tweets.get(userId, []) + [(self.postnum, tweetId)]
        self.postnum -= 1
        if userId not in self.subscribtion:
            self.subscribtion[userId] = set([userId])

    def getNewsFeed(self, userId: int) -> List[int]:
        # max heap -> recent tweet gets more higher key
        pool = []
        if userId not in self.subscribtion:
            return
        
        for user in self.subscribtion[userId]:
            if user in self.tweets:
                pool += self.tweets[user]
        
        heapq.heapify(pool)
        res, cnt = [], 0
        while pool and cnt < 10:
            res.append(heapq.heappop(pool)[1])
            cnt += 1
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.subscribtion:
            self.subscribtion[followerId] = set()
            self.subscribtion[followerId].add(followerId) # incldue themself
        self.subscribtion[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.subscribtion and followeeId in self.subscribtion[followerId]:
            self.subscribtion[followerId].remove(followeeId)