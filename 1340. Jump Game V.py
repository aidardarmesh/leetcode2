from typing import *

class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        n = len(arr)
        dp = [1]*n
        
        for i in range(n):
            for j in range(i-d, i):
                if j < 0 or arr[j] >= arr[i]:
                    break
                
                dp[i] = max(dp[i], dp[j]+1)
            
            for j in range(i+1, i+d+1):
                if j >= n or arr[j] >= arr[i]:
                    break
                
                dp[i] = max(dp[i], dp[j]+1)
        
        return max(dp)
