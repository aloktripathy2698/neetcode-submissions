from heapq import heapify, heappop

class Twitter:

    def __init__(self):
        self.userToTweetMap = defaultdict(list)
        self.userFollowingMap = defaultdict(set)
        self.time = 0
        
    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.userToTweetMap:
            self.userToTweetMap[userId] = []
        self.time += 1
        self.userToTweetMap[userId].append((tweetId, self.time))
        
    # time complexity = O(F * T), space complexity = O(F * T)
    def getNewsFeed(self, userId: int) -> List[int]:
        maxHeap = []
        users = self.userFollowingMap[userId] | {userId}
        tweets = []
        for user in users:
            for tweet in self.userToTweetMap[user]:
                tweetId, timeStamp = tweet
                maxHeap.append((-timeStamp, tweetId))
        heapify(maxHeap)
        feed = []
        for i in range(10):
            if maxHeap == []:
                break
            feed.append(heappop(maxHeap)[1])
        return feed       

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.userFollowingMap:
            self.userFollowingMap[followerId] = set()
        self.userFollowingMap[followerId].add(followeeId)
        
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.userFollowingMap:
            return
        if followeeId not in self.userFollowingMap[followerId]:
            return
        self.userFollowingMap[followerId].remove(followeeId)

        
