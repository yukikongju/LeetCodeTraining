#  https://leetcode.com/problems/design-twitter/

# Solution: maxHeap
# - Followers/Following will be a set; posts will be a queue; newsfeed will be a heap
# - To generate the newsfeed, we first generate the candidates 
#   by looking at followees last K items and we then use maxHeap 
#   to build the nesfeed
# - heapify is O(n) vs sorting is O(n log n)

class Twitter:

    def __init__(self):
        self.timestamp = 0
        self.user_tweets = defaultdict(list) # (timestamp, tweetId)
        self.user_follows = defaultdict(set)
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.user_tweets[userId].append((self.timestamp, tweetId))
        self.timestamp += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        # take the last 10 posts of each followee + last 10 post of user
        candidates = []
        if userId in self.user_follows: # if userId follows anybody
            for followee in self.user_follows[userId]:
                candidates.extend(self.user_tweets[followee][-10:])
        if userId in self.user_tweets: # if userId has tweeted
            candidates.extend(self.user_tweets[userId][-10:])
        
        # build newfeeds with maxHeap
        candidates = [(-timestamp, tweetId) for timestamp, tweetId in candidates]
        heapq.heapify(candidates)
        newsfeed = []
        while candidates and len(newsfeed) < 10:
            _, tweetId = heapq.heappop(candidates)
            newsfeed.append(tweetId)
        return newsfeed
        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.user_follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if (followerId != followeeId) and (followeeId in self.user_follows[followerId]):
            self.user_follows[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
