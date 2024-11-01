#  https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii/description/

class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        # solution: Prefix Sum + Sort 
        # if the array is sorted, we use the binary search to find the middle element. 
        # the middle element will the value of each element in nums
        # sol = prev_sum + post_sum; value = nums[middle]

        # sort
        nums.sort()

        # compute the middle number
        n = len(nums)
        middle = n // 2
        
        # compute prefix sum
        prefix_sum = [0]
        for num in nums:
            prefix_sum.append(prefix_sum[-1] + num)
        
        # compute number of moves
        total_sum = prefix_sum[-1]
        val = nums[middle]
        prev_sum = val * middle - prefix_sum[middle]
        post_sum = (total_sum - prefix_sum[middle]) - val * (n - middle)
        return prev_sum + post_sum
        
