from typing import *

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        time = 0
        cnt = {}
        
        for task_id in tasks:
            cnt[task_id] = cnt.get(task_id, 0) + 1
        
        import heapq
        heap = []
        for task_id, num in cnt.items():
            heapq.heappush(heap, -num)
        
        while heap:
            temp = []
            
            for i in range(n+1):
                if heap:
                    task = heapq.heappop(heap)
                    task += 1

                    if task != 0:
                        temp.append(task)
                
                time += 1
                
                if not heap and not temp:
                    break
            
            while temp:
                heapq.heappush(heap, temp.pop())
        
        return time

