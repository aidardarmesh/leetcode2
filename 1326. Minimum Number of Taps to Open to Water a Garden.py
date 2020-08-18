from typing import *

class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        max_range = [0]*(n+1)
        
        for i, tap in enumerate(ranges):
            left, right = max(0, i-tap), min(n, i+tap)
            max_range[left] = max(max_range[left], right)
        
        max_curr = max_pos = max_range[0]
        jumps = 1
        
        for i in range(1, len(ranges)):
            if max_curr < i:
                jumps += 1
                max_curr = max_pos
            
            max_pos = max(max_pos, max_range[i])
            
            if max_pos == i and i != len(ranges)-1:
                return -1
        
        return jumps
