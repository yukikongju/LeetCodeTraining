class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # solution: maxHeap // minHeap

        num_iter = len(nums) if (k == 1) else len(nums)-k+1

        heapq.heapify(nums)

        for i in range(num_iter):
            min_elem = heapq.heappop(nums)
            print(i, min_elem)
        
        return min_elem

