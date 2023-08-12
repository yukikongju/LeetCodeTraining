#  https://leetcode.com/problems/missing-number/description/

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # 
        n = len(nums)
        num_set = set(nums)

        for num in range(n+1):
            if num not in num_set:
                return num

