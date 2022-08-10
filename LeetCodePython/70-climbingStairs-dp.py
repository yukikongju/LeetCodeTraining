class Solution:
    def climbStairs(self, n: int) -> int:
        if n in [1,2]:
            return n
        
        choices = [0 for _ in range(n + 1)]
        choices[1] = 1
        choices[2] = 2
        
        for i in range(3, len(choices)):
            choices[i] = choices[i-1] + choices[i-2]
        
        return choices[n]
        

