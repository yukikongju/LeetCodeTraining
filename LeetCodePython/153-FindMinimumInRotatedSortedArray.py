class Solution:
    def findMin(self, nums: List[int]) -> int:
        # solution: binary search
        # one half will always be sorted. track the minimum

        target = float('inf')
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[left] <= nums[mid]:
                if nums[mid] <= nums[right]: # it's sorted
                    return nums[left]
                else:
                    left = mid + 1 
            else: 
                right = mid 
        return left
            
