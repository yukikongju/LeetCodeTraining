#  Link: https://leetcode.com/problems/merge-intervals/

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Sol: sort by first O(nlogn) and compare last entry with next occurence
        # choices: (1) overlap (2) no overlap (3) subset
        intervals.sort(key = lambda x: x[0])
        merged = [intervals[0]]
        last_start = merged[-1][0]
        
        for start, end in intervals[1:]:
            last_end = merged[-1][1]
            if start <= last_end: 
                merged[-1][1] = max(last_end, end)
            else:
                merged.append([start, end])
        
        return merged
        


