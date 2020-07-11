from typing import *

class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        dp = {}
        
        def dfs(arr, i, d):
            if dp.get(i):
                return dp[i]
            
            res = 1
            
            for j in range(i-1, max(-1, i-d-1), -1):
                if arr[j] >= arr[i]:
                    break
                
                res = max(res, 1 + dfs(arr, j, d))
            
            for j in range(i+1, min(len(arr), i+d+1), 1):
                if arr[j] >= arr[i]:
                    break
                
                res = max(res, 1 + dfs(arr, j, d))
            
            dp[i] = res
            
            return dp[i]
        
        ans = 1
        
        for i in range(len(arr)):
            ans = max(ans, dfs(arr, i, d))
        
        return ans
