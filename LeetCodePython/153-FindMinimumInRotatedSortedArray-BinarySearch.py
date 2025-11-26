#  https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/submissions/1839902080/
class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Solution: Binary Search
        # We need to find the pivot point where the array was rotated
        # [big numbers] [small numbers]
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (right + left) // 2

            if nums[left] < nums[right]: # ordered
                return nums[left]
            
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        return nums[left]
