#  https://leetcode.com/problems/count-good-meals/

class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        # solution: Freq Count + Hash Table
        # we want to add the complement

        # --- calculate powers - val max = 2^20 + 2^20
        powers = [2**k for k in range(22)]

        # --- 
        res = 0
        freq_dict = defaultdict(int)
        for num in deliciousness:
            for power in powers:
                res += freq_dict[power - num]
            freq_dict[num] += 1

        # ---
        return res % (10**9 + 7)
        
