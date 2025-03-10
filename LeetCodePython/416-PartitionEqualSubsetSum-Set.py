#  https://leetcode.com/problems/partition-equal-subset-sum/

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # solution: 1D DP - 
        # intuition: compute sum; decision: take or not take the number; keep track of previous subset sum
        # brute-force: compute all subsets => n!
        # recursive solution: 

        # --- 
        total = sum(nums)
        subsets = set()
        
        for num in nums:
            tmp = set()
            for s in subsets:
                if s == total - s:
                    return True
                tmp.add(s + num)
            for t in tmp:
                subsets.add(t)
            subsets.add(num)
        
        return False

        
        
