#  https://leetcode.com/problems/max-consecutive-ones-iii/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # solution: sliding window
        # (1) if 1: end += 1
        # (2) if 0 and flips => flips += 1; end += 1
        # (3) if 0 but no flips => start += 1 ; flips += 1 if last == 0 else 0


        # ---
        start = 0
        longest = 0
        for end in range(len(nums)):
            if nums[end] == 0:
                k -= 1
            
            if (k<0):
                if (nums[start]) == 0: k += 1
                start += 1
            longest = max(longest, end - start + 1)

        return longest
