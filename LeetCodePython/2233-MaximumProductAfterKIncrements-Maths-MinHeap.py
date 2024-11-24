#  https://leetcode.com/problems/maximum-product-after-k-increments/

class Solution:
    def maximumProduct(self, nums: List[int], k: int) -> int:
        # solution: min Heap => O(k)
        # intuition: always increment smallest number
        # let x > y. 
        # if x++ => (x+1) * y = xy + y
        # if y++ => x * (y+1) = xy + x
        # => (xy + y < xy + x)

        ## initialize heap
        heap = []
        for num in nums:
            heapq.heappush(heap, num)
        
        ## increment smallest number iteratively using heap
        while k > 0:
            c = heapq.heappop(heap)
            heapq.heappush(heap, c+1)
            k -= 1
        
        ## compute product
        product = 1
        mod =  (10**9+7)
        while len(heap) > 0:
            c = heapq.heappop(heap)
            product = ((product % mod) * (c % mod)) % mod
        return product

        
