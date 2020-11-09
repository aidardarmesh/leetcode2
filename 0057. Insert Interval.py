from typing import *

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        START, END = 0, 1
        
        def merge(intervals):
            res = []
            for start, end in intervals:
                if res and res[-1][END] >= start:
                    res[-1][END] = max(res[-1][END], end)
                else:
                    res.append([start, end])
            
            return res
        
        intervals.append(newInterval)
        for i in range(len(intervals)-1, 0, -1):
            if intervals[i][START] < intervals[i-1][START]:
                intervals[i], intervals[i-1] = intervals[i-1], intervals[i]
        
        return merge(intervals)
