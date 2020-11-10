from typing import *

class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        import heapq
        
        heap = []
        x_origin, y_origin = 0, 0
        
        for i in range(K):
            x, y = points[i][0], points[i][1]
            dist = (x_origin-x)**2 + (y_origin-y)**2
            heapq.heappush(heap, (-dist, x, y))
        
        for i in range(K, len(points)):
            x, y = points[i][0], points[i][1]
            dist = (x_origin-x)**2 + (y_origin-y)**2
            if dist < -heap[0][0]:
                heapq.heappop(heap)
                heapq.heappush(heap, (-dist, x, y))
        
        return [[x,y] for dist, x, y in heap]
