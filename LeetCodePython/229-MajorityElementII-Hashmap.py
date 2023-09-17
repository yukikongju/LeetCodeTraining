#  https://leetcode.com/problems/majority-element-ii/

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # solution: hashmap

        # ---
        n = len(nums)
        third = n / 3
        counts_dict = defaultdict(int)
        for num in nums:
            counts_dict[num] += 1

        # ---
        res = []
        for num, count in counts_dict.items():
            if count > third:
                res.append(num)
        return res
        
