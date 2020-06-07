from typing import *

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        import heapq

        heap = []
        intervals.sort()

        for start, end in intervals:
            if heap and heap[0] <= start:
                heapq.heappushpop(heap, end)
            else:
                heapq.heappush(heap, end)
        
        return len(heap)
