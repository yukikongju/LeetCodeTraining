#  https://leetcode.com/problems/majority-element/

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # solution: Hashmap

        # ---
        n = len(nums)
        half = n /2
        counts_dict = defaultdict(int)
        for num in nums:
            counts_dict[num] += 1
        
        # ---
        res = []
        for num, count in counts_dict.items():
            if count > half:
                res.append(num)
        return res[0]
        
