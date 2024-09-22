#  https://leetcode.com/problems/find-three-consecutive-integers-that-sum-to-a-given-number/description/ 
#  got TLE

class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        # solution: hard sliding window O(n)

        # base case: less than [0,1,2]
        if num < 3:
            return []

        WINDOW_LENGTH = 3
        sol = []
        csum = 3
        current = 3
        while csum < num:
            prev, suiv = current - WINDOW_LENGTH + 1, current + 1
            csum += suiv - prev
            current += 1
        
        return [] if csum != num else [n for n in range(current - WINDOW_LENGTH, current)]
