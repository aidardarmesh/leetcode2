from typing import *

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        START, END = 0, 1
        
        intervals.sort(key=lambda x: x[0])
        
        res = []
        for start, end in intervals:
            if res and res[-1][END] >= start:
                res[-1][END] = max(res[-1][END], end)
            else:
                res.append([start, end])
        
        return res
