from typing import *

class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        res = []
        if not matrix:
            return res
        
        n, m = len(matrix), len(matrix[0])
        pac = [[False for __ in range(m)] for _ in range(n)]
        atl = copy.deepcopy(pac)
        
        pac_queue = collections.deque()
        atl_queue = copy.deepcopy(pac_queue)
        
        for i in range(n):
            pac_queue.append((i,0))
            atl_queue.append((i,m-1))
            pac[i][0] = True
            atl[i][m-1] = True
        
        for j in range(m):
            pac_queue.append((0,j))
            atl_queue.append((n-1,j))
            pac[0][j] = True
            atl[n-1][j] = True
        
        def bfs(matrix, queue, visited):
            n, m = len(matrix), len(matrix[0])
            while queue:
                i,j = queue.popleft()
                
                for ni,nj in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]:
                    if ni < 0 or ni >= n or nj < 0 or nj >= m or visited[ni][nj] or matrix[ni][nj] < matrix[i][j]:
                        continue
                    queue.append((ni,nj))
                    visited[ni][nj] = True
        
        bfs(matrix, pac_queue, pac)
        bfs(matrix, atl_queue, atl)
        
        for i in range(n):
            for j in range(m):
                if pac[i][j] and atl[i][j]:
                    res.append([i,j])
        
        return res
