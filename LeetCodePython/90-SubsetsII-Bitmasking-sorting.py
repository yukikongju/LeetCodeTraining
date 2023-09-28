#  https://leetcode.com/problems/subsets-ii/

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # solution: Bitwise masking + sort

        # --- find all subsets
        n = len(nums)
        subsets = set()
        for mask in range(pow(2, n)):
            subset = []
            for j in range(n):
                bit = mask & 1
                if bit: subset.append(nums[j])
                mask >>= 1
            subset.sort()
            subsets.add(tuple(subset))

        # --- remove dupplicates
        return [subset for subset in subsets]
        
        
