class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        # solution: running sum
        running_sum = 0
        res = [0]
        highest = 0 
        for g in gain:
            running_sum += g
            highest = max(highest, running_sum)
            res.append(running_sum)
        
        return highest
