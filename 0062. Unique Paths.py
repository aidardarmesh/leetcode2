from typing import *

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def get_paths(board, i, j):
            if not (0 <= i < n and 0 <= j < m):
                return 0
            
            return board[i][j]
        
        dp = [[0 for _ in range(m)] for __ in range(n)]
        
        for j in range(m):
            dp[n-1][j] = 1
        
        for i in range(n):
            dp[i][m-1] = 1
        
        for i in range(n-2, -1, -1):
            for j in range(m-2, -1, -1):
                dp[i][j] = get_paths(dp, i, j+1) + get_paths(dp, i+1, j)
        
        return dp[0][0]
