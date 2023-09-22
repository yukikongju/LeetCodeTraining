#  https://leetcode.com/problems/subarray-product-less-than-k/

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        # solution: Sliding Window

        # ---
        start, current_product = 0, 1
        num_subarrays = 0 
        for i, num in enumerate(nums):
            current_product *= num
            if current_product < k:
                num_subarrays += i - start + 1
            else: 
                while (start <= i) and (current_product >= k):                   
                    current_product /= nums[start]
                    start += 1
                num_subarrays += i - start + 1      
        
        return num_subarrays

