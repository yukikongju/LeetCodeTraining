class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # solution: binary search, but we want to find 
        # note: when we split in half, one half will we sorted and the other half won't
        # we can find the sorted half by checking if nums[left] < nums[mid]
        # 6,7,0,1,2,3,4,5

        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid 
            elif nums[left] <= nums[mid]: # left is the sorted half
                if nums[left] <= target <= nums[mid]:
                    right = mid - 1
                else: 
                    left = mid + 1
            else: # right is the sorted half
                if nums[mid] <= target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1
        
