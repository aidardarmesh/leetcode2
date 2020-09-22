from typing import *

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        import heapq
        
        n = len(matrix)
        heap = [(matrix[0][0], 0, 0)]
        visited = {(0,0)}
        
        while heap:
            val, i, j = heapq.heappop(heap)
            k -= 1
            
            if k == 0:
                return val
            
            for ni, nj in [(i+1,j),(i,j+1)]:
                if 0 <= ni < n and 0 <= nj < n and not (ni,nj) in visited:
                    heapq.heappush(heap, (matrix[ni][nj],ni,nj))
                    visited.add((ni,nj))
        
        return -1
