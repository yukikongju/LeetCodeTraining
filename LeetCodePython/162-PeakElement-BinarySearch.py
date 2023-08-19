#  https://leetcode.com/problems/find-peak-element/description/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # O(log n): binary search

        # ---
        start, end = 0, len(nums) -1
        while start <= end:
            mid = (start+end)//2

            # check if left greater than mid
            if (mid>0) and (nums[mid] < nums[mid-1]):
                end = mid-1

            # check if greater than right
            elif (mid<len(nums)-1) and (nums[mid] < nums[mid+1]):
                start=mid+1
            else:
                return mid

