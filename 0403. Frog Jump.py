from typing import *

class Solution:
    def canCross(self, stones: List[int]) -> bool:
        ladder = {}
        for x in stones:
            ladder[x] = set()
        
        ladder[0].add(0)
        
        for x in stones:
            for k in ladder[x]:
                for step in [k-1, k, k+1]:
                    if step > 0 and x+step in ladder:
                        ladder[x+step].add(step)
        
        return len(ladder[stones[-1]]) > 0
