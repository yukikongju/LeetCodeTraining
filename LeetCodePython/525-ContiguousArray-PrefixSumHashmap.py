#  https://leetcode.com/problems/contiguous-array/description/

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        # solution: prefix sum
        
        prefix_sum = 0
        longest = 0
        index_dct = {0: -1}
        for i, num in enumerate(nums):
            # compute prefix sum
            d = 1 if num == 1 else -1
            prefix_sum += d

            # compute longest contiguous array at index i
            if prefix_sum in index_dct:
                longest = max(longest, i - index_dct[prefix_sum])
            else:
                index_dct[prefix_sum] = i
        return longest
            
