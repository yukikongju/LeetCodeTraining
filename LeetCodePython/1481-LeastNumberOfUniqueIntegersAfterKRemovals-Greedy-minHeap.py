#  https://leetcode.com/problems/least-number-of-unique-integers-after-k-removals/description/

class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        # solution: Greedy + MinHeap
        # we remove number starting from the numbers with the least counts

        # --- get each number counts
        counts_dict = defaultdict(int)
        for num in arr:
            counts_dict[num] += 1
        
        # --- build minHeap
        minHeap = [] # (count, num)
        for num, count in counts_dict.items():
            heapq.heappush(minHeap, (count, num))

        # --- Greedy: remove elements from lowest counts to biggest count
        while k > 0:
            count, num = heapq.heappop(minHeap)
            
            if k >= count:
                k -= count
            elif k < count:
                k = 0
                count -= k
                heapq.heappush(minHeap, (count, num))

        # ---
        return len(minHeap)
