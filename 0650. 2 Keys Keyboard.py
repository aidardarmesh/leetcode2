from typing import *

class Solution:
    def minSteps(self, n: int) -> int:
        if n == 1:
            return 0
        
        dp = [0]*(n+1)
        dp[2] = 2
        
        for i in range(2, n+1):
            ans = i
            
            for j in range(i-1, 1, -1):
                if i % j == 0:
                    ans = min(ans, dp[j] + i // j)
            
            dp[i] = ans
        
        return dp[n]
