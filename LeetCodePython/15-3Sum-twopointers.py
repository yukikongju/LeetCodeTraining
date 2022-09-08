#  Link: https://leetcode.com/problems/3sum/

# Reformulation: 


# Solution: iterate through each element and sliding windows on following subarray
# [NeetCode Solution](https://www.youtube.com/watch?v=jzZsG8n2R9A)

# Time Complexity: O(nlogn) + O(n^2) = O(n^2)

# Follow Up: Can we find 4 numbers such that their sum is 0?

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        results = []
        nums.sort()
        
        for i, val in enumerate(nums):
            if i > 0 and val == nums[i-1]: # make sure that same number is not calculated twice (duplicates)
                continue
            left, right = i+1, len(nums) -1
            
            while left < right: 
                three_sum = val + nums[left] + nums[right]
                if three_sum > 0:
                    right -= 1
                elif three_sum < 0:
                    left +=1
                else: # three_sum == 0
                    results.append([val, nums[left], nums[right]])
                    left += 1
                    while nums[left] == nums[left -1] and left < right: # make sure that we don't compute same number again
                        left += 1
        
        return results
                    
        
