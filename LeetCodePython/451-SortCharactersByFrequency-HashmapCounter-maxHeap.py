#  https://leetcode.com/problems/sort-characters-by-frequency/

class Solution:
    def frequencySort(self, string: str) -> str:
        # solution: Hashmap counter + maxHeap

        # --- build letters counts
        counts_dict = defaultdict(int)
        for s in string:
            counts_dict[s] += 1
        
        # --- build maxHeap
        maxHeap = []
        for num, count in counts_dict.items():
            heapq.heappush(maxHeap, (-count, num))
        
        # --- build final string
        t = ""
        while maxHeap:
            count, num = heapq.heappop(maxHeap)
            count *= -1

            t += num * count

        return t
        
