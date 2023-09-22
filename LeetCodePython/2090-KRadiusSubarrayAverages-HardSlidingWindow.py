#  https://leetcode.com/problems/k-radius-subarray-averages/

class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        # solution: Hard Sliding Window

        # --- init
        n = len(nums)
        res = [-1 for _ in range(n)]

        # --- base case
        if k == 0:
            return nums
        if 2*k >= n: 
            return res

        # ---
        current_sum = sum(nums[:2*k+1]) 
        res[k] = current_sum // (2*k+1)

        for i in range(k+1, n-k):
            current_sum += nums[i+k] - nums[i-k-1]
            # print(i, nums[i+k], nums[i-k-1], current_sum)
            res[i] = current_sum // (2*k+1)

        return res

        
