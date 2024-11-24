#  https://leetcode.com/problems/maximum-length-of-repeated-subarray/description/

class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        # Solution: Longest common substring - DP
        # https://leetcode.com/problems/maximum-length-of-repeated-subarray/
        # dp[i][j] = dp[i-1][j-1] + 1 if nums1[i-1] == nums2[j-1] else 0

        m, n = len(nums1), len(nums2)
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        ans = 0 
        for i in range(1, m+1):
            for j in range(1, n+1):
                dp[i][j] = dp[i-1][j-1] + 1 if nums1[i-1] == nums2[j-1] else 0
                ans = max(ans, dp[i][j])
        return ans
                
