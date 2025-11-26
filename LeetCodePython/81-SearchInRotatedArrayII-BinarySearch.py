#  https://leetcode.com/problems/search-in-rotated-sorted-array-ii/
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        # Solution: Binary Search
        # Strategy:
        # - one half will always be sorted => we search in the sorted half
        # - if we find duplicates values, we need to skip

        left, right = 0, len(nums) - 1
        while (left <= right):
            mid = (left + right) // 2

            if nums[mid] == target:
                return True
            
            if nums[left] == nums[mid]:
                left += 1
                continue
            
            if nums[left] <= nums[mid]: # left half is sorted
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else: # right half is sorted 
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        
        return False

