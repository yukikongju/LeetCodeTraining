#  https://leetcode.com/problems/subsets/

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # solution: Bitwise O(n^2)
        # (1) generate all bit from 0 to 2^n -1
        # (2) generate subset using mask
        # mask >>= 1 is a right shift

        # ---
        n = len(nums)
        subsets = []
        for mask in range(pow(2, n)):
            subset = []
            for j in range(n):
                bit = mask & 1
                if bit == 1: subset.append(nums[j])
                mask >>= 1
            subsets.append(subset)
        
        return subsets


