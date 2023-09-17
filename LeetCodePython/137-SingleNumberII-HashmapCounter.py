#  https://leetcode.com/problems/single-number-ii/

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # solution: Hashmap Counter

        # ---
        counts_dict = defaultdict(int)
        for num in nums:
            counts_dict[num] += 1
        
        # --- 
        for num, count in counts_dict.items():
            if count == 1:
                return num
