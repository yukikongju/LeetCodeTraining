#  https://leetcode.com/problems/subarray-sum-equals-k/

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # solution: prefix sum + hasmap => O(n)
        # sum(i, j) = sum(0, j) - sum(0, i)

        count = 0
        prefix_sum = 0
        frequency_dct = {0: 1}
        for num in nums:
            # compute prefix sum
            prefix_sum += num

            # use hashmap frequency to update the count
            if (prefix_sum - k) in frequency_dct:
                count += frequency_dct[prefix_sum - k]
            
            # update the count
            if prefix_sum in frequency_dct:
                frequency_dct[prefix_sum] += 1
            else:
                frequency_dct[prefix_sum] = 1
            
        return count
        
