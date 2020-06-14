from typing import *

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        n = len(grid)
        m = len(grid[0])
        cnt = 0
        
        def bfs(i,j):
            from collections import deque
            
            deq = deque()
            deq.append((i,j))
            
            while deq:
                i,j = deq.popleft()
                
                for ni,nj in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]:
                    if 0 <= ni < n and 0 <= nj < m and grid[ni][nj] == '1':
                        grid[ni][nj] = '0'
                        deq.append((ni,nj))
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    bfs(i,j)
                    cnt += 1
        
        return cnt
