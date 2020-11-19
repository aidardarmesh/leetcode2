from typing import *

class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        def bfs(start_i, start_j, end_i, end_j):
            queue = collections.deque()
            queue.append((start_i, start_j))
            visited = set()
            visited.add((start_i, start_j))
            moves = 0
            while queue:
                size = len(queue)
                for _ in range(size):
                    i, j = queue.popleft()
                
                    if i == end_i and j == end_j:
                        return moves
                    
                    dirs = [
                        (i-2,j+1),
                        (i-1,j+2),
                        (i+1,j+2),
                        (i+2,j+1),
                        (i+2,j-1),
                        (i+1,j-2),
                        (i-1,j-2),
                        (i-2,j-1)
                    ]
                    
                    for ni, nj in dirs:
                        if not (ni,nj) in visited:
                            queue.append((ni,nj))
                            visited.add((ni,nj))
                moves += 1
            
            return -1
        
        return bfs(0, 0, x, y)
