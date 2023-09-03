#  https://leetcode.com/problems/monotone-increasing-digits/description/

class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        # solution: Greedy

        # base case: smaller than 10
        if n < 10:
            return n

        # --- traverse right to left: if current bigger than previous, decrement and all digits after to 9
        nums = list(map(int, str(n)))
        n = len(nums)
        for i in range(n-1, 0, -1):
            if nums[i] < nums[i-1]:
                nums[i-1] -= 1
                for j in range(i, n):
                    nums[j] = 9
        
        # --- remove all zeroes in front
        # while nums and nums[0] == 0:
        #     nums.pop(0)

        # --- convert to integer
        return int(''.join(map(str, nums)))

