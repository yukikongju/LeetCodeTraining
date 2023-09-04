#  https://leetcode.com/problems/increasing-triplet-subsequence/description/

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        # solution: Greedy

        # --- 
        first = second = float('inf')
        for num in nums:
            if num <= first:
                first = num
            elif num <= second:
                second = num
            else:
                return True
        return False

