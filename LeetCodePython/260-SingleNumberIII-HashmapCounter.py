#  https://leetcode.com/problems/single-number-iii/

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        # solution: Hasmap Counter

        # --- base case:
        n = len(nums)
        if n == 2:
            return nums

        # ---
        counts_dict = defaultdict(int)
        for num in nums:
            counts_dict[num] += 1
        
        # ---
        res = []
        for num, count in counts_dict.items():
            if count == 1:
                res.append(num)
        return res
        
