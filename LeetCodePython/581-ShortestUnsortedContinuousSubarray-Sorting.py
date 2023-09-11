#  https://leetcode.com/problems/shortest-unsorted-continuous-subarray/description/

class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        # solution: sorting - O(nlogn)

        # --- get sorted array
        sorted_nums = nums.copy()
        sorted_nums.sort()

        # --- left pointer: 
        n = len(nums)
        start, end = 0, n-1
        while (start < n) and (nums[start] == sorted_nums[start]):
            start += 1
            
        # --- right pointer:
        while (end >= 0) and (nums[end] == sorted_nums[end]):
            end -= 1
        
        print(start, end)

        return end-start+1 if end>=start else 0

        
