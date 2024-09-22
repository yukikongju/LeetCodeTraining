#  https://leetcode.com/problems/maximum-consecutive-floors-without-special-floors/

class Solution:
    def maxConsecutive(self, bottom: int, top: int, special: List[int]) -> int:
        # solution:

        # base case
        if top - bottom + 1 == len(special):
            return 0
        
        # compute max difference between floors
        special.sort()
        longest = 0
        for i in range(len(special)-1):
            longest = max(longest, special[i+1] - special[i] - 1)
        
        # special case: bottom to 1 floor and last floor to top
        diff_first = special[0] - bottom if bottom != special[0] else 0
        longest = max(longest, diff_first)

        diff_last = top - special[-1] if top != special[-1] else 0
        longest = max(longest, diff_last)

        return longest        

