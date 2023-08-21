#  https://leetcode.com/problems/peak-index-in-a-mountain-array/description/

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        # solution: binary search - O(log n)
        # (1) if arr[i] < arr[i-1] => mountain must be at left
        # (2) if arr[i] > arr[i-1] => mountain must be right

        first, last = 0, len(arr)-1
        while first <= last:
            mid = (first + last) // 2

            if (arr[mid] > arr[mid-1]) and (arr[mid] > arr[mid+1]):
                return mid
            elif (arr[mid] < arr[mid-1]):
                last = mid
            else:
                first = mid+1
        
        return -1


