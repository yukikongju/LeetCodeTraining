#  https://leetcode.com/problems/number-of-longest-increasing-subsequence/description/

class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        # solution: 1D DP - LIS
        # brute-force: check if all substrings are strictly increasing
        # intuition: at each index, look at the longest substring that can be formed => O(n^2)
        # decision: take or not take - keep track of longest and counts
        # https://www.youtube.com/watch?v=Tuc-rjJbsXU

        if not nums:
            return 0
        n = len(nums)
        m, dp, counts = float('-inf'), [1] * n, [1] * n

        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    if dp[i] < dp[j] + 1:
                        dp[i], counts[i] = dp[j] + 1, counts[j]
                    elif dp[i] == dp[j] + 1:
                        counts[i] += counts[j]
            m = max(m, dp[i])

        return sum([c for l, c in zip(dp, counts) if l == m])
            

