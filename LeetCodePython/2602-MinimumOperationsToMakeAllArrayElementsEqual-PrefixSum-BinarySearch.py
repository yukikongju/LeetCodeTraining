#  https://leetcode.com/problems/minimum-operations-to-make-all-array-elements-equal/description/

class Solution:
    def minOperations(self, nums: List[int], queries: List[int]) -> List[int]:
        # solution: prefixSum
        # sol[i] = sum_{j=0}^{n} |j-i|
        # prev_sum = num * idx - prefix_sum[idx]
        # post_sum = (total_sum - prefix_sum[idx]) - num * (n - idx)
        # sort values
        nums.sort()

        # compute prefix sum
        prefix_sum = [0]
        for num in nums:
            prefix_sum.append(num + prefix_sum[-1])

        # compute cost for each queries
        total_sum, n = prefix_sum[-1], len(nums)
        out = []
        for q in queries:
            idx = bisect.bisect(nums, q)
            prev_sum = q * idx - prefix_sum[idx]
            post_sum = (total_sum - prefix_sum[idx]) - q * (n - idx)
            out.append(prev_sum + post_sum)

        return out
