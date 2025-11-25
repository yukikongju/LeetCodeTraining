class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # solution: minHeap - optimized
        # heapify = sorting; pop heap until k elements left
        # ex: [1, 2, 3, 4, 5, 6]; returns 5

        heap = nums[:k]
        heapq.heapify(heap)
        for num in nums[k:]:
            if num > heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap, num)
        
        return heap[0]
