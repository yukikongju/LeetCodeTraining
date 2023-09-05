https://leetcode.com/problems/k-closest-points-to-origin/description/

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # solution: minHeap

        # --- calculate euclidean distances for each pair of points + build maxHeap
        minHeap = []
        for x, y in points:
            dist = math.sqrt(x**2 + y**2)
            heapq.heappush(minHeap, (dist, x, y))

        # ---
        res = []
        while k > 0 and minHeap:
            _, x, y = heapq.heappop(minHeap)
            res.append([x, y])
            k -= 1
        
        return res

        
