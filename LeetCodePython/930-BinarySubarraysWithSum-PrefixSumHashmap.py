#  https://leetcode.com/problems/binary-subarrays-with-sum/description/

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        # solution: prefix sum hashmap

        count = 0
        freq_dct = {0: 1}
        psum = 0
        for num in nums:
            psum += num

            count += freq_dct.get(psum - goal, 0)
            freq_dct[psum] = freq_dct.get(psum, 0) + 1
        
        return count
        
