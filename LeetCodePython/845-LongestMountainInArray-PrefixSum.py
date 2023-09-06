#  https://leetcode.com/problems/longest-mountain-in-array/solutions/3047278/two-python-solution-with-o-n-time-o-n-space-and-second-with-o-1-space/

class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        # solution: 
        # explanation: https://leetcode.com/problems/longest-mountain-in-array/solutions/3047278/two-python-solution-with-o-n-time-o-n-space-and-second-with-o-1-space/

        # --- compute num of smaller - left to right
        n = len(arr)
        smallers = [0 for _ in range(n)]
        s = 0
        for i in range(1, n):
            if arr[i-1] < arr[i]:
                s += 1
                smallers[i] = s
            else: 
                s = 0
        

        # --- compute num of bigger - right to left
        biggers = [0 for _ in range(n)]
        b = 0
        for i in range(n-1, 0, -1):
            if arr[i-1] > arr[i]:
                b += 1
                biggers[i-1] = b
            else: b = 0
        
        print(smallers)
        print(biggers)
        
        # --- compute biggest mountain
        mountain = [s+b+1 if s and b else 0 for s, b in zip(smallers, biggers)]
        return max(mountain)
