#  https://leetcode.com/problems/last-stone-weight/description/

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # solution: maxHeap

        # --- build maxHeap
        maxHeap = []
        for stone in stones:
            heapq.heappush(maxHeap, -stone)

        # --- play the game: smash two stones together
        while len(maxHeap) >= 2:
            stone1 = heapq.heappop(maxHeap)
            stone2 = heapq.heappop(maxHeap)

            diff = stone1 - stone2
            if diff < 0:
                heapq.heappush(maxHeap, diff)

        # --- 
        return -maxHeap[0] if len(maxHeap) == 1 else 0

        
