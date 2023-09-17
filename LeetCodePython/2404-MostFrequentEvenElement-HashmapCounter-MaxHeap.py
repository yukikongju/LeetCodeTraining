#  https://leetcode.com/problems/most-frequent-even-element/

class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        # solution: Hasmap Counter + MaxHeap 

        # --- counter
        counts_dict = defaultdict(int)
        for num in nums:
            if num % 2 == 0:
                counts_dict[num] += 1
        
        # --- building maxHeap 
        max_heap = []
        for num, count in counts_dict.items():
            heapq.heappush(max_heap, (-count, num))

        # ---
        if len(max_heap) == 0:
            return -1

        # --- getting all numbers with max_count
        max_count, _ = max_heap[0]
        res = []
        while max_heap:
            count, num = heapq.heappop(max_heap)
            if count == max_count:
                res.append(num)

        # --- sorting results
        res.sort()
        return res[0]
        
