#  https://leetcode.com/problems/minimum-time-difference/description

class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        # solution: 
        # 1. sort time O(nlogn)
        # 2. compute minute difference O(n) 
        # edge case: last time - first time 
        
        # 
        timePoints.sort(reverse = False)

        # - 
        def get_time_difference(t1: str, t2: str) -> int: # consider both side
            """
            """
            
            def get_minutes(t: str):
                # given t="HH:MM" return the amount of minutes
                h, m = t.split(':')
                return 60 * int(h) + int(m)
            
            if t1 > t2:
                return get_time_difference(t2, t1)
            
            return min(get_minutes(t2) - get_minutes(t1), 24*60 + get_minutes(t1) - get_minutes(t2))
        
        # 
        diffs = []
        prev = timePoints[0]
        for time in timePoints[1:]:
            diffs.append(get_time_difference(prev, time))
            prev = time
        diffs.append(get_time_difference(timePoints[0], timePoints[-1]))
        
        return min(diffs)

