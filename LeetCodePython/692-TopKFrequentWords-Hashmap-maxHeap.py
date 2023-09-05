#  https://leetcode.com/problems/top-k-frequent-words/description/

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        # solution: hashmap

        # --- dict count O(n)
        counts_dict = defaultdict(int)
        for word in words:
            counts_dict[word] += 1

        # --- maxHeap
        maxHeap = []
        for word, count in counts_dict.items():
            heapq.heappush(maxHeap, (-count, word))
        

        # ---
        results = []
        while maxHeap:
            _, word = heapq.heappop(maxHeap)
            results.append(word)

        # ---
        return results[:k]

