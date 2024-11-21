class Solution:
    def minMoves(self, nums: List[int]) -> int:
        # solution: math
        # sum: sum all numbers; minNum: min(nums) ; n = len(nums)
        # sum + m * (n-1) = x * n ; x = minNum + m => the minimum number will get incremented every move
        # sum + m * (n-1) = (minNum + m) * n
        # sum + mn - m = minNum * n + mn
        # sum - m = minNum * n => m = sum - minNum * n

        return sum(nums) - min(nums) * len(nums)
        
