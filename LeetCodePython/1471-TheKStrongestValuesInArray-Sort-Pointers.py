#  https://leetcode.com/problems/the-k-strongest-values-in-an-array/description/

class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        # solution: pointers + sort => O(n) + O(nlogn)

        # --- base case
        n = len(arr)
        if n == 1 and k == 1:
            return arr        

        # --- sort and find median
        arr.sort()
        idx_median = (len(arr) - 1) // 2
        m = arr[idx_median]

        # --- add strongest from the left
        res = []
        left, right = 0, n-1
        while left <= right:
            strongest_left, strongest_right = abs(arr[left] - m), abs(arr[right] - m)
            if strongest_left > strongest_right:
                res.append(arr[left])
                left += 1
            elif strongest_left < strongest_right:
                res.append(arr[right])
                right -= 1
            else:
                if arr[left] > arr[right]:
                    res.append(arr[left])
                    left += 1
                else:
                    res.append(arr[right])
                    right -= 1
        
        # 
        return res if k == n else res[:k]

        
