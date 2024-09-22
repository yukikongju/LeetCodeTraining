#  https://leetcode.com/problems/subarray-sums-divisible-by-k/

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        # solution: prefix sum O(n)
        # note: modulo property => remainder

        freq_dict = {0: 1}
        count = 0
        psum = 0
        for num in nums:
            # compute prefix sum
            psum += num

            # add the count
            remainder = psum % k
            remainder = remainder if remainder >= 0 else remainder + k
            count += freq_dict.get(remainder, 0)

            # update frequency
            freq_dict[remainder] = freq_dict.get(remainder, 0) + 1

        return count
