from typing import *

class Solution:
    def longestIncreasingPath(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        dp = {}
        
        def dfs(grid, i, j, n, m, dp):
            if dp.get((i,j)):
                return dp[(i,j)]
            
            res = 1
            
            for ni,nj in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]:
                if 0 <= ni < n and 0 <= nj < m and grid[ni][nj] > grid[i][j]:
                    res = max(res, 1 + dfs(grid, ni, nj, n, m, dp))
            
            dp[(i,j)] = res
            
            return res
        
        n, m = len(grid), len(grid[0])
        ans = 1
        
        for i in range(n):
            for j in range(m):
                ans = max(ans, dfs(grid, i, j, n, m, dp))
        
        return ans
