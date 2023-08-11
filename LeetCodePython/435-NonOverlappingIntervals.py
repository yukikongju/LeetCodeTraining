class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # solution: 

        # --- sort
        intervals.sort(key=lambda x: x[0])

        # --- 
        counts = 0
        last_end = intervals[0][1]

        for next_start, next_end in intervals[1:]:
            if next_start < last_end: # case 2: overlap
                counts += 1
                last_end = min(last_end, next_end) # need to choose min in case one interval is inside the other
            else: # case 1: no overlap
                last_end = next_end
        
        return counts

