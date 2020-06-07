from typing import *

class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        n, S = len(stones), sum(stones)
        S2 = S // 2
        dp = [[False for _ in range(S2+1)] for __ in range(n+1)]
        max_S = 0

        for i in range(n+1):
            dp[i][0] = True
        
        for i in range(1, n+1):
            for s in range(1, S2+1):
                if dp[i-1][s] or (s >= stones[i-1] and dp[i-1][s-stones[i-1]]):
                    dp[i][s] = True
                    max_S = max(max_S, s)
        
        return abs(S - 2*max_S)

s = Solution()

assert s.lastStoneWeightII([2,7,4,1,8,1]) == 1
assert s.lastStoneWeightII([8,2,4,4,8]) == 2
assert s.lastStoneWeightII([31,26,33,21,40]) == 5
