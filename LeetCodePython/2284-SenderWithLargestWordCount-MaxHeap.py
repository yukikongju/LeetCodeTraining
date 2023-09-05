#  https://leetcode.com/problems/sender-with-largest-word-count/description/

class Solution:
    def largestWordCount(self, messages: List[str], senders: List[str]) -> str:
        # solution: maxHeap

        # --- words count for each senders
        senders_dict = defaultdict(int)
        for message, sender in zip(messages, senders):
            num_words = len(message.split(' '))
            senders_dict[sender] += num_words
        
        # --- maxHeap
        maxHeap = []
        for sender, count in senders_dict.items():
            heapq.heappush(maxHeap, (-count, sender))
        
        # --- find sender with largest word count
        largest_count = maxHeap[0][0]
        res = []
        while maxHeap:
            count, sender = heapq.heappop(maxHeap)
            if count == largest_count:
                res.append(sender)
            else: 
                break
        
        # if there are several senders with the largest word count, choose the one with lexicographically largest name
        return res[-1]
        
