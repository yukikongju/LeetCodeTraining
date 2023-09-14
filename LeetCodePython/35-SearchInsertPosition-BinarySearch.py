#  https://leetcode.com/problems/search-insert-position/

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # solution: binary search

        start, end = 0, len(nums)-1
        while start <= end:
            mid = (start+end) // 2

            if nums[mid] == target:
                return mid
            elif target < nums[mid]:
                end = mid-1
            elif target > nums[mid]:
                start = mid+1
        
        return start
        
