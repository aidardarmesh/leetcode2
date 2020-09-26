from typing import *

import heapq

class MedianFinder:

    def __init__(self):
        self.max_heap = []
        self.min_heap = []

    def addNum(self, num: int) -> None:
        if len(self.max_heap) == 0:
            heapq.heappush(self.max_heap, -num)
            return
        
        if len(self.min_heap) == 0:
            heapq.heappush(self.min_heap, num)
            return
        
        if num <= -self.max_heap[0]:
            heapq.heappush(self.max_heap, -num)
        else:
            heapq.heappush(self.min_heap, num)
        
        len_diff = len(self.max_heap) - len(self.min_heap)
        if len_diff > 1:
            heapq.heappush(self.min_heap, -self.max_heap[0])
            heapq.heappop(self.max_heap)
        elif len_diff <= -1:
            heapq.heappush(self.max_heap, -self.min_heap[0])
            heapq.heappop(self.min_heap)
        
        if -self.max_heap[0] > self.min_heap[0]:
            max_left = -heapq.heappop(self.max_heap)
            min_right = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -min_right)
            heapq.heappush(self.min_heap, max_left)

    def findMedian(self) -> float:
        if len(self.max_heap) > len(self.min_heap):
            return -self.max_heap[0]
        
        return (-self.max_heap[0] + self.min_heap[0]) / 2
