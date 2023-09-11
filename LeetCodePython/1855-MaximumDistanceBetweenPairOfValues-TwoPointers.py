#  https://leetcode.com/problems/maximum-distance-between-a-pair-of-values/description/

class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        # solution: two pointers

        # --- 
        m, n = len(nums1), len(nums2)
        distance_max = 0
        i, j = 0, 0
        while (i<m) and (j<n):
            if (i<=j) and (nums1[i] <= nums2[j]):
                distance_max = max(j-i, distance_max)
                print(i, j)
                j += 1
            elif (j<i):
                j += 1
            elif (nums1[i] > nums2[j]):
                i += 1

        
        return distance_max
