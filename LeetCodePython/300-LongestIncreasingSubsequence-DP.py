#  https://leetcode.com/problems/longest-increasing-subsequence/submissions/1551044239/

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # solution: 1D DP
        # intuition: iterate through each position and answer the question "what's the longest substring from this position"
        # write-up: https://leetcode.com/problems/longest-increasing-subsequence/solutions/1326308/c-python-dp-binary-search-bit-segment-tree-solutions-picture-explain-o-nlogn/

        n = len(nums)
        dp = [1 for _ in range(n)]
        
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)
