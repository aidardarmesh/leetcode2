from typing import *

class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        if not stones:
            return 0
        
        smashed_stones = {stones[0]}
        
        for i in range(1, len(stones)):
            temp = set()
            
            for smashed in smashed_stones:
                temp.add(abs(smashed - stones[i]))
                temp.add(smashed + stones[i])
            
            smashed_stones = temp
        
        return min(smashed_stones)
