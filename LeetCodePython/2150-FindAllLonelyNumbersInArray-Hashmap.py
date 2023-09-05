#  https://leetcode.com/problems/find-all-lonely-numbers-in-the-array/description/

class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        # sol1: sorting
        # sol2: hashmap

        # --- init frequency dict
        seen = set()
        freq_dict = defaultdict(int)
        for num in nums:
            freq_dict[num] += 1
            seen.add(num)
        
        # --- 
        res = []
        for num in nums:
            if (freq_dict[num] == 1) and (num-1 not in seen) and (num+1 not in seen):
                res.append(num)

        # ---
        return res        
        
